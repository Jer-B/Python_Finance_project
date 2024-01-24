# English README 　[Jump to Japanese Version](#japanese)

# Portofolio Stock Simulator Web Application

## About the project

This is a website via which users can “buy” and “sell” stocks.
You will be able to manage a portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy and sell stocks with fake money (like a stocks portofolio simulator) by querying [IEX](https://iextrading.com/developer/) for stocks’ prices.
Starting with $10,000 of fake money.

## How to use

1. Look fot a stock acronym and input the number of share or for how much to buy. ie: If You are interested into Netflix, look for "NFLX".
2. You can chose to sell whatever you want if you own it.

### Usage example with screenshots

1. Register an account. Username and password. (It can be "Test" and "123")

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/register.png" width="900" alt="register">
</p>
<br/>

2. Login with your account.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/login.png" width="900" alt="Login">
</p>
<br/>

3. Here is the default page after login. The portofolio summary, with the initial amount of money.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/default_sum.png" width="900" alt="portofolio summary">
</p>
<br/>

4. On the "Quote" page, input a stock acronym. And check it's price. Doesn't work if the acronym is wrong.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/quote.png" width="900" alt="Login">
</p>
<br/>

5. On the "Buy" page, input a stock acronym and the number of share to buy. You can't buy more than you can afford.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/buy3_quote.png" width="900" alt="Login">
</p>
<br/>

6. After buying, the portofolio summary is updated. Shares are added to the portofolio, and the amount of money is updated.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/sfter_buy.png" width="900" alt="Login">
</p>
<br/>

7. On the "Sell" page, input a stock acronym and the number of share to sell. You can't sell more than you own.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/sell_3.png" width="900" alt="Login">
</p>
<br/>

8. After selling, the portofolio summary is updated. Shares are removed from the portofolio, and the amount of money is updated.

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/sell_3.png" width="900" alt="Login">
</p>
<br/>

## Understanding

- `application.py`: This file contains the code for the Flask web application. It includes one route (`/`) that handles both POST and GET requests. When the `/` route is requested via GET, it renders the `index.html` template. When requested via POST, the user is redirected back to `/` via GET.

- 'helpers.py': It has an implementation of an apology page. Notice how it ultimately renders a template, apology.html. It also happens to define within itself another function, "escape", that it simply uses to replace special characters in apologies. By defining escape inside of apology, we’ve scoped the former to the latter alone; no other functions will be able (or need) to call it.

Next in the file is login_required. a function that can return another function which checks login requirements.

Thereafter is lookup, a function that, given a symbol (e.g., NFLX), returns a stock quote for a company in the form of a dict with three keys: name, whose value is a str, the name of the company; price, whose value is a float; and symbol, whose value is a str, a canonicalized (uppercase) version of a stock’s symbol, irrespective of how that symbol was capitalized when passed into lookup.

Last in the file is usd, a short function that simply formats a float as USD (e.g., 1234.56 is formatted as $1,234.56).

- `static/styles.css`: This directory contains the CSS code for the web application. You can modify this file to customize the appearance of your application.

- `templates/index.html`: This HTML file is rendered when users visit your web application.

## Installation

To set up the required dependencies, follow these steps:
Be sure to change pip for pip3 if necessary.

1. Clone this repository to your local machine.

2. Create a virtual environment (optional but recommended):

   Using `virtualenv` (if not installed, run `pip install virtualenv`):

   ```bash
   virtualenv venv
   ```

   Or using venv (Python 3.3+):

   ```bash
   python -m venv venv
   ```

3. If using a virtual environment (Step 2), activate it:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```
4. Install the required packages from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
   This will set up the necessary packages for the project.

## Testing

To test the Flask application, run the following command in your terminal while in your the directory:

```bash
flask run
```

This will start a web server that serves the Flask application. You can then access the application by opening your web browser and navigating to http://localhost:5000.

Enjoy using this stocks simulator!

<a name="japanese"></a>

# 日本語版の README

# 株式シミュレーター

## プロジェクトについて

これはユーザーが株式を「購入」および「売却」できるウェブサイトです。
株式ポートフォリオを管理できます。このツールでは、実際の株価とポートフォリオの価値を確認できるだけでなく、[IEX](https://iextrading.com/developer/)をクエリして株価を取得し、架空のお金で株式を購入および売却することもできます（株式ポートフォリオのシミュレーターのように）。
初めに 10,000 ドルの架空のお金から始めます。

## 使い方

1. 株式の略語を探し、株式の数や購入金額を入力します。例：Netflix に興味がある場合、「NFLX」を探します。
2. 所有しているものを自由に売却することができます。

### スクリーンショット付きの使用例

1. アカウントを登録します。ユーザー名とパスワード。（「Test」と「123」でも良いです）

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/register.png" width="900" alt="登録">
</p>
<br/>

2. アカウントでログインします。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/login.png" width="900" alt="ログイン">
</p>
<br/>

3. ログイン後のデフォルトページです。ポートフォリオの概要と初期金額が表示されます。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/default_sum.png" width="900" alt="ポートフォリオ概要">
</p>
<br/>

4. 「Quote」ページでは、株の略称を入力し、その価格を確認します。略称が間違っている場合は機能しません。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/quote.png" width="900" alt="ログイン">
</p>
<br/>

5. 「Buy」ページでは、株の略称と購入する株式の数を入力します。購入できる金額を超えることはできません。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/buy3_quote.png" width="900" alt="ログイン">
</p>
<br/>

6. 購入後、ポートフォリオの概要が更新されます。株式がポートフォリオに追加され、金額が更新されます。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/sfter_buy.png" width="900" alt="ログイン">
</p>
<br/>

7. 「Sell」ページでは、株の略称と売却する株式の数を入力します。所有している株式より多くを売ることはできません。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/sell_3.png" width="900" alt="ログイン">
</p>
<br/>

8. 売却後、ポートフォリオの概要が更新されます。株式がポートフォリオから削除され、金額が更新されます。

<br/>
<p align="center">
<img src="https://github.com/Jer-B/jer-b.github.io/blob/main/assets/code_img/finance/sell_3.png" width="900" alt="ログイン">
</p>
<br/>

## 理解

- `application.py`: このファイルには Flask ウェブアプリケーションのコードが含まれています。このアプリケーションには POST リクエストと GET リクエストの両方を処理する 1 つのルート（`/`）が含まれています。`/`ルートは GET でリクエストされると`index.html`テンプレートがレンダリングされます。POST でリクエストされた場合、ユーザーは GET を介して再度`/`にリダイレクトされます。

- 'helpers.py'：これは謝罪ページの実装を持っています。注意してください、最終的にはテンプレートである 'apology.html' をレンダリングしています。また、それ自体内部に別の関数 "escape" を定義しており、謝罪文の中の特殊文字を単純に置換するために使用しています。"escape" を謝罪の中で定義することで、前者を後者にスコープ化しました。他の関数はそれを呼び出すことはできず（または必要ありません）。

次に、ファイル内に [login_required] があります。この関数はログイン要件をチェックする別の関数を返すことができます。

その後には lookup があります。この関数はシンボル（例：NFLX）を指定すると、企業の株価を含む辞書形式で返します。辞書には name（会社名を表す文字列）、price（株価を表す浮動小数点数）、symbol（株式のシンボルの正規化された大文字形式を表す文字列）の 3 つのキーがあります。lookup に渡されたシンボルの大文字化に関係なく、シンボルは正規化されます。

ファイル内の最後には usd があり、これは浮動小数点数を単純に USD としてフォーマットする短い関数です（例：1234.56 は $1,234.56 としてフォーマットされます）。

- `static/styles.css`: このディレクトリにはウェブアプリケーションの CSS コードが含まれています。このファイルをカスタマイズしてアプリケーションの外観を変更できます。

- `templates/index.html`: この HTML ファイルはユーザーがウェブアプリケーションを訪れたときにレンダリングされます。

## インストール

必要な依存関係を設定するには、次の手順に従ってください：
必要に応じて`pip`を`pip3`に変更してください。

1. このリポジトリをローカルマシンにクローンしてください。

2. 仮想環境を作成します（オプションですが推奨）：

   `virtualenv`を使用する場合（インストールされていない場合は`pip install virtualenv`を実行）：

   ```bash
   virtualenv venv
   ```

   または venv を使用する場合（Python 3.3+）：

   ```bash
   python -m venv venv
   ```

3. 仮想環境を使用する場合（ステップ 2）、それをアクティブにします：
   - Windows の場合：
   ```bash
   venv\Scripts\activate
   ```
   - macOS および Linux の場合：
   ```bash
   source venv/bin/activate
   ```
4. requirements.txt から必要なパッケージをインストールします：
   ```bash
   pip install -r requirements.txt
   ```
   これでプロジェクトの必要なパッケージが設定されます。

## テスト

Flask アプリケーションをテストするには、ディレクトリ内で次のコマンドを実行してください：

```bash
flask run
```

これにより、Flask アプリケーションを提供するウェブサーバーが起動します。その後、ウェブブラウザを開いて http://localhost:5000
にアクセスすることで、アプリケーションにアクセスできます。

この株式シミュレーターをお楽しみください！
