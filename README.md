# English README　[Jump to Japanese Version](#japanese)

# Birthday Reminder Web Application

## About the project

This is a website via which users can “buy” and “sell” stocks.
You will be able to manage a portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy and sell stocks with fake money (like a stocks portofolio simulator) by querying [IEX](https://iextrading.com/developer/) for stocks’ prices.
Starting with $10,000 of fake money.

## How to use

1. Look fot a stock acronym and input the number of share or for how much to buy. ie: If You are interested into Netflix, look for "NFLX".
2. You can chose to sell whatever you want if you own it.

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
# 日本語版のREADME

# 株式シミュレーター

## プロジェクトについて

これはユーザーが株式を「購入」および「売却」できるウェブサイトです。
株式ポートフォリオを管理できます。このツールでは、実際の株価とポートフォリオの価値を確認できるだけでなく、[IEX](https://iextrading.com/developer/)をクエリして株価を取得し、架空のお金で株式を購入および売却することもできます（株式ポートフォリオのシミュレーターのように）。
初めに10,000ドルの架空のお金から始めます。

## 使い方

1. 株式の略語を探し、株式の数や購入金額を入力します。例：Netflixに興味がある場合、「NFLX」を探します。
2. 所有しているものを自由に売却することができます。

## 理解

- `application.py`: このファイルにはFlaskウェブアプリケーションのコードが含まれています。このアプリケーションにはPOSTリクエストとGETリクエストの両方を処理する1つのルート（`/`）が含まれています。`/`ルートはGETでリクエストされると`index.html`テンプレートがレンダリングされます。POSTでリクエストされた場合、ユーザーはGETを介して再度`/`にリダイレクトされます。

- 'helpers.py'：これは謝罪ページの実装を持っています。注意してください、最終的にはテンプレートである 'apology.html' をレンダリングしています。また、それ自体内部に別の関数 "escape" を定義しており、謝罪文の中の特殊文字を単純に置換するために使用しています。"escape" を謝罪の中で定義することで、前者を後者にスコープ化しました。他の関数はそれを呼び出すことはできず（または必要ありません）。

次に、ファイル内に [login_required] があります。この関数はログイン要件をチェックする別の関数を返すことができます。

その後には lookup があります。この関数はシンボル（例：NFLX）を指定すると、企業の株価を含む辞書形式で返します。辞書には name（会社名を表す文字列）、price（株価を表す浮動小数点数）、symbol（株式のシンボルの正規化された大文字形式を表す文字列）の 3 つのキーがあります。lookup に渡されたシンボルの大文字化に関係なく、シンボルは正規化されます。

ファイル内の最後には usd があり、これは浮動小数点数を単純に USD としてフォーマットする短い関数です（例：1234.56 は $1,234.56 としてフォーマットされます）。

- `static/styles.css`: このディレクトリにはウェブアプリケーションのCSSコードが含まれています。このファイルをカスタマイズしてアプリケーションの外観を変更できます。

- `templates/index.html`: このHTMLファイルはユーザーがウェブアプリケーションを訪れたときにレンダリングされます。

## インストール

必要な依存関係を設定するには、次の手順に従ってください：
必要に応じて`pip`を`pip3`に変更してください。

1. このリポジトリをローカルマシンにクローンしてください。

2. 仮想環境を作成します（オプションですが推奨）：

   `virtualenv`を使用する場合（インストールされていない場合は`pip install virtualenv`を実行）：
   ```bash
   virtualenv venv
   ```
   またはvenvを使用する場合（Python 3.3+）：
   ```bash
   python -m venv venv
   ```
3. 仮想環境を使用する場合（ステップ2）、それをアクティブにします：
   - Windowsの場合：
   ```bash
   venv\Scripts\activate
   ```
   - macOSおよびLinuxの場合：
   ```bash
   source venv/bin/activate
   ```
   
4. requirements.txtから必要なパッケージをインストールします：
   ```bash
   pip install -r requirements.txt
   ```
これでプロジェクトの必要なパッケージが設定されます。

## テスト

Flaskアプリケーションをテストするには、ディレクトリ内で次のコマンドを実行してください：
   ```bash
   flask run
   ```
   これにより、Flaskアプリケーションを提供するウェブサーバーが起動します。その後、ウェブブラウザを開いてhttp://localhost:5000
   にアクセスすることで、アプリケーションにアクセスできます。
   
この株式シミュレーターをお楽しみください！