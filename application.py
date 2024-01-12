import os
# export API_KEY=pk_56de14d7880c468eb75d2759bccce302
#or export API_KEY=pk_058474deae3b4cf2bae811787b46caa3
# Latest API_KEY=pk_38cb223c14ca4f439855d6adee63946b
# flask run
from cs50 import SQL
import sqlalchemy
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

import urllib.parse
import psycopg2

from helpers import apology, login_required, lookup, usd



# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

#uri = os.getenv("DATABASE_URL")
#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://")
#db = SQL(uri)

# start
# added the below as part of Heroku post on Medium

#urllib.parse.uses_netloc.append("postgres")
#url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
#conn = psycopg2.connect(
 #database=url.path[1:],
 #user=url.username,
 #password=url.password,
 #host=url.hostname,
 #port=url.port
#)
#db = SQL(os.environ["DATABASE_URL"])
# end


# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Acces transactions database to return stocks owned Symbol + Company name + number of shares + price of each + total values
    portofolio = db.execute(
        "SELECT share_symbol, company_name, shares_amount, share_price, total_cost FROM transactions WHERE shares_amount != 0 AND users_id = :curr_user", curr_user=int(session['user_id']))

    # Current cash that user's own
    curr_cash = db.execute("SELECT cash FROM users WHERE id = :user_cash_id", user_cash_id=int(session['user_id']))
    show_cash = curr_cash[0]["cash"]

    # For loop for grand total
    grand_total = 0

    for total in portofolio:
        grand_total += total["total_cost"]

    # Add cash in bank to all shares sum
    grand_total += show_cash

    return render_template("index.html", portofolio=portofolio, cash=show_cash, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # current user_id + username (for transactions table) and cash of the user
    curr_user_id = db.execute("SELECT id FROM users WHERE id = :curr_user", curr_user=int(session['user_id']))
    curr_user_name = db.execute("SELECT username FROM users WHERE id = :curr_username", curr_username=int(session['user_id']))

    # Current cash that user's own
    curr_cash = db.execute("SELECT cash FROM users WHERE id = :user_cash_id", user_cash_id=int(session['user_id']))
    show_cash = curr_cash[0]["cash"]

    if request.method == "POST":

        # Lookup function from helper.py to look at any correspondance of the inputed symbol / stock prefix name
        search_quote = lookup(request.form.get("symbol"))

        # Share number inputed
        share_amount = request.form.get("shares")

        # Check if there is Quote prefix and at least 1 share bought
        if not request.form.get("symbol"):
            # flash("Input a Stock prefix to buy.")
            return apology("Input a Stock prefix to buy.", 400)
            # return render_template("buy.html", cash=show_cash)

        elif search_quote == None:
            # flash("Stock prefix doesn't exist")
            return apology("Stock prefix doesn't exist", 400)
            # return render_template("buy.html", cash=show_cash)

        elif not share_amount.isdigit() or int(share_amount) < 1:
            # flash("Select at least 1 share to buy when buying.")
            return apology("Select at least 1 share to buy when buying.", 400)
            # return render_template("buy.html", cash=show_cash)

        # total cost when buying shares
        price_sum = search_quote["price"] * int(share_amount)
        cash_left = int(curr_cash[0]["cash"]) - price_sum

        # If user have enough cash buy
        if cash_left > 0:
            # update user cash to cash_left in database
            db.execute("UPDATE users SET cash = :cash_left WHERE id = :user_cash_id",
                       cash_left=cash_left, user_cash_id=int(session['user_id']))
            flash("Order succesful!")

            # add transaction to history
            db.execute("INSERT INTO history (users_id, transaction_type, share_symbol, company_name, shares_amount, share_buy_price, share_sell_price, total_cost) VALUES (:users_id, :transaction_type, :share_symbol, :company_name, :shares_amount, :share_buy_price, :share_sell_price,:total_cost)",
                       users_id=session["user_id"], transaction_type="BUY", share_symbol=search_quote["symbol"], company_name=search_quote["name"], shares_amount=share_amount, share_buy_price=search_quote["price"], share_sell_price=0, total_cost=price_sum)

            share_owned = db.execute("SELECT share_symbol from transactions WHERE users_id = :users_id",
                                     users_id=int(session["user_id"]))
            check_owned = False
            for row in share_owned:
                print(row)
                if row["share_symbol"] == search_quote["symbol"]:
                    check_owned = True
            print(check_owned)

            # if no shares of company
            if check_owned == False:
                # add transaction to transactions table (current shares owned table)
                db.execute("INSERT INTO transactions (users_id, transaction_type, share_symbol, company_name, shares_amount, share_price, total_cost) VALUES (:users_id, :transaction_type, :share_symbol, :company_name, :shares_amount, :share_price, :total_cost)",
                           users_id=session["user_id"], transaction_type="BUY", share_symbol=search_quote["symbol"], company_name=search_quote["name"], shares_amount=share_amount, share_price=search_quote["price"], total_cost=price_sum)
                flash("Shares Bought!")
                return redirect("/")

            # if shares of same company already owned
            elif check_owned == True:
                # update existing share values of already existing same symbol
                original_amount = db.execute("SELECT shares_amount FROM transactions WHERE users_id = :users_id AND share_symbol = :share_own", users_id=int(
                    session["user_id"]), share_own=search_quote["symbol"])

                # sum existing shares with new bought ones
                update_number = 0
                for row in original_amount:
                    update_number += row["shares_amount"]

                update_number += int(share_amount)

                # update shares
                db.execute("UPDATE transactions SET shares_amount = :update_amount WHERE users_id = :users_id AND share_symbol = :share_own",
                           update_amount=update_number, users_id=int(session["user_id"]), share_own=search_quote["symbol"])
                flash("Shares Bought! Existing shares number for that company has been Updated!")
                return redirect("/")

        else:
            flash("You don't have enough cash in your bank account!")

        return render_template("buy.html", cash=show_cash)
    return render_template("buy.html", cash=show_cash)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Acces history database to return bought and sold stocks actions, Symbol + Company name + number of shares + which price for each action + total values + timestamp
    history = db.execute(
        "SELECT transaction_type, share_symbol, company_name, shares_amount, share_buy_price, share_sell_price, total_cost, date FROM history WHERE users_id = :user_id", user_id=int(session['user_id']))

    # Current cash that user's own
    curr_cash = db.execute("SELECT cash FROM users WHERE id = :user_cash_id", user_cash_id=int(session['user_id']))
    show_cash = curr_cash[0]["cash"]

    return render_template("history.html", history=history, cash=show_cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        search_quote = lookup(request.form.get("symbol"))

        if not request.form.get("symbol"):
            #flash("Enter a quote prefix.")
            return apology("Input a Stock prefix to buy.", 400)

        # Check if quote prefix exist
        elif search_quote != None:

            return render_template("quoted.html", company_name=search_quote["name"], symbol=search_quote["symbol"], price=search_quote["price"])

        else:
            # flash("Quote prefix doesn't exist.")
            return apology("Quote prefix doesn't exist.", 400)

    return render_template("quote.html")

    """Get stock quote."""

#    if request.method == "POST":

        # Ensure symbol was submitted
#        if not request.form.get("symbol"):
#            return apology("Input a Stock ticker to buy.", 400)

#        search_quote = lookup(request.form.get("symbol"))

#        if not stocks:
#            return apology("Quote ticker doesn't exist.", 400)

        # Show current price of stock requested
#        return render_template("quoted.html", company_name=search_quote["name"], symbol=search_quote["symbol"], price=search_quote["price"])

#    else:
#        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # When user submit registration
    if request.method == "POST":

        # Query database for all username
        rows = db.execute("SELECT username FROM users")
        # Check if username already exist in DB
        for row in rows:
            if row["username"] == request.form.get("username"):
                return apology("Username already exist, choose another.", 400)

        # if no username input
        if not request.form.get("username"):
            return apology("Username required", 400)

        # if no password input
        elif not request.form.get("password"):
            return apology("Password required", 400)

        # if password and confirmation doesnt match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and Password confirmation doesn't match.", 400)

        else:
            # hash password
            user_check = request.form.get("username")
            user_pass = request.form.get("password")

            password_hash = generate_password_hash(user_pass, method='pbkdf2:sha256', salt_length=8)

            # insert into user table username and hashed password
            db.execute("INSERT INTO users (username, hash) VALUEs(?, ?)", user_check, password_hash)

            flash("Registration success!")
            return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # current user_id + username (for transactions table) and cash of the user
    curr_user_id = db.execute("SELECT id FROM users WHERE id = :curr_user", curr_user=int(session['user_id']))
    curr_user_name = db.execute("SELECT username FROM users WHERE id = :curr_username", curr_username=int(session['user_id']))

    # Current cash that user's own
    curr_cash = db.execute("SELECT cash FROM users WHERE id = :user_cash_id", user_cash_id=int(session['user_id']))
    show_cash = curr_cash[0]["cash"]

    # Select owned shares
    to_sell = db.execute("SELECT share_symbol FROM transactions WHERE shares_amount != 0 AND users_id = :curr_user",
                         curr_user=int(session['user_id']))
    share_list = []
    for row in to_sell:
        share_list.append(row["share_symbol"])
        print(share_list)

    if request.method == "POST":

        # Share number inputed
        share_amount = request.form.get("shares")

        # Symbol row user id of selected symbol to sell
        symbol_sell = db.execute("SELECT id FROM transactions WHERE users_id = :user_id AND share_symbol = :selected_share", user_id=int(
            session['user_id']), selected_share=request.form.get("symbol"))

        # Select shares owned of selected symbol to sell
        share_sell = db.execute("SELECT shares_amount FROM transactions WHERE users_id = :user_id AND share_symbol = :selected_share", user_id=int(
            session['user_id']), selected_share=request.form.get("symbol"))
        check_share_sell = 0
        for row in share_sell:
            check_share_sell = row["shares_amount"]

        # Check if there is Quote prefix and at least 1 share bought
        if request.form.get("symbol") not in share_list:
            flash("Input a Stock prefix to buy.")

        elif not share_amount.isdigit() or int(share_amount) < 1 or int(share_amount) > check_share_sell:
            #flash("Invalid Share number to sell. Input at least 1 and not more than you owned.")
            return apology("Invalid Share number to sell. Input at least 1 and not more than you owned.", 400)
        else:
            # portion that sell and update database if above checks are ok

            # Lookup function from helper.py to look at any correspondance of the inputed symbol / stock prefix name
            search_quote = lookup(request.form.get("symbol"))

            # Get updated price of the quote to be multiply by number of shares to sold + calculate new total
            price_sum = search_quote["price"] * int(share_amount)
            cash_left = int(curr_cash[0]["cash"]) + price_sum

            # Update user cash database
            db.execute("UPDATE users SET cash = :cash_left WHERE id = :user_cash_id",
                       cash_left=cash_left, user_cash_id=int(session['user_id']))

            # add transaction to history
            db.execute("INSERT INTO history (users_id, transaction_type, share_symbol, company_name, shares_amount, share_buy_price, share_sell_price, total_cost) VALUES (:users_id, :transaction_type, :share_symbol, :company_name, :shares_amount, :share_buy_price, :share_sell_price,:total_cost)",
                       users_id=session["user_id"], transaction_type="SELL", share_symbol=search_quote["symbol"], company_name=search_quote["name"], shares_amount=share_amount, share_buy_price=0, share_sell_price=search_quote["price"], total_cost=price_sum)

            # update existing share values of already existing same symbol
            original_amount = db.execute("SELECT shares_amount FROM transactions WHERE users_id = :users_id AND share_symbol = :share_own", users_id=int(
                session["user_id"]), share_own=search_quote["symbol"])

            # sum existing shares with new bought ones
            update_number = 0
            for row in original_amount:
                update_number += row["shares_amount"]

            update_number -= int(share_amount)

            # if shares_amount == 0 after sell, delere row from transaction (aka portofolio)
            if update_number == 0:
                db.execute("DELETE FROM transactions WHERE users_id = :users_id AND share_symbol = :share_own",
                           users_id=int(session["user_id"]), share_own=search_quote["symbol"])
                flash("Share(s) Sold ! You don't own any other share of that company. Portofolio has been Updated!")

            # else update shares
            else:
                db.execute("UPDATE transactions SET shares_amount = :update_amount WHERE users_id = :users_id AND share_symbol = :share_own",
                           update_amount=update_number, users_id=int(session["user_id"]), share_own=search_quote["symbol"])
                flash("Shares Sold! Portofolio and History has been Updated!")

            return redirect("/")

        return render_template("sell.html", cash=show_cash, symbol_list=to_sell)

    return render_template("sell.html", cash=show_cash, symbol_list=to_sell)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
