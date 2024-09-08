
# Stripe API FastAPI Application

このプロジェクトは、Stripe APIを使用して顧客情報、サブスクリプション、請求書、支払い、商品情報を取得するFastAPIアプリケーションです。DockerとUbuntu 24.04を使用して簡単に実行できます。

## セットアップ手順 (Ubuntu 24.04)

### 1. Dockerのインストール

```bash
# システムパッケージを更新
sudo apt update
sudo apt upgrade -y

# 必要な依存関係をインストール
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Dockerの公式GPGキーを追加
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Dockerリポジトリを追加
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# パッケージリストを更新
sudo apt update

# Dockerをインストール
sudo apt install docker-ce docker-ce-cli containerd.io -y

# Dockerサービスを開始し、自動起動を有効化
sudo systemctl start docker
sudo systemctl enable docker

# 現在のユーザーをdockerグループに追加（再ログインが必要）
sudo usermod -aG docker $USER
```

### 2. Docker Composeのインストール

```shellscript
# Docker Composeをダウンロード
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 実行権限を付与
sudo chmod +x /usr/local/bin/docker-compose
```

### 3. プロジェクトのセットアップ

```shellscript
# リポジトリをクローン
git clone https://github.com/DaisukeHori/stripe_api-fastapi.git
cd stripe_api-fastapi
```


はい、.envファイルの作成と設定について、より詳細に説明いたします。

1. .envファイルの目的:
.envファイルは「環境変数」を保存するためのファイルです。環境変数とは、アプリケーションの設定や秘密の情報（APIキーなど）を安全に保存するための方法です。
2. .envファイルの作成:
プロジェクトのルートディレクトリ（stripe_api-fastapi フォルダ）内に、`.env`という名前のファイルを作成します。

ターミナルで以下のコマンドを実行して、.envファイルを作成できます：

```plaintext
touch .env
```


3. .envファイルの編集:
お好みのテキストエディタで.envファイルを開きます。例えば：

```plaintext
nano .env
```

または

```plaintext
vim .env
```


4. 環境変数の設定:
.envファイルに以下の内容を追加します：

```plaintext
STRIPE_API_KEY=your_stripe_api_key_here
AUTH_KEY=your_secret_auth_key_here
```

ここで：

1. `STRIPE_API_KEY`: StripeのAPIキーを設定します。これはStripe管理画面から取得できます。
2. `AUTH_KEY`: アプリケーションの認証に使用する秘密のキーです。これは自分で決めた任意の文字列を設定します。



5. 値の置き換え:
`your_stripe_api_key_here` と `your_secret_auth_key_here` を実際の値に置き換えてください。

例：

```plaintext
STRIPE_API_KEY=sk_test_51ABCDEFGhIjKlMnOpQrStUvW
AUTH_KEY=my_very_secret_auth_key_12345
```


6. ファイルの保存:
変更を保存してエディタを閉じます。
7. セキュリティ注意事項:

1. .envファイルには機密情報が含まれるため、Gitにコミットしないでください。
2. .gitignoreファイルに`.env`が含まれていることを確認してください。



8. 確認:
.envファイルが正しく作成されたか確認するには、以下のコマンドを使用します：

```plaintext
cat .env
```

このコマンドで.envファイルの内容が表示されます。




これらの手順に従うことで、アプリケーションに必要な環境変数を安全に設定できます。環境変数を使用することで、コード内に直接機密情報を書き込むことを避け、セキュリティを向上させることができます。

### 4. アプリケーションの実行

```shellscript
# Dockerイメージをビルドして実行
docker-compose up --build
```

アプリケーションが正常に起動すると、[http://localhost:8000](http://localhost:8000) でアクセスできます。

## API使用例

APIを使用するには、リクエストヘッダーに`X-Auth-Key`を含める必要があります。以下は各エンドポイントの使用例です。

### 顧客情報の取得

```shellscript
curl -H "X-Auth-Key: your_secret_auth_key_here" http://localhost:8000/api/customers/example@email.com
```

レスポンス例：

```json
{
  "customers": [
    {
      "id": "cus_1234567890",
      "object": "customer",
      "email": "example@email.com",
      "name": "John Doe",
      "created": 1634567890
    }
  ]
}
```

### サブスクリプション情報の取得

```shellscript
curl -H "X-Auth-Key: your_secret_auth_key_here" http://localhost:8000/api/subscriptions/example@email.com
```

レスポンス例：

```json
{
  "subscriptions": [
    {
      "id": "sub_1234567890",
      "object": "subscription",
      "customer": "cus_1234567890",
      "status": "active",
      "current_period_start": 1634567890,
      "current_period_end": 1637159890
    }
  ]
}
```

### 請求書情報の取得

```shellscript
curl -H "X-Auth-Key: your_secret_auth_key_here" http://localhost:8000/api/invoices/example@email.com
```

レスポンス例：

```json
{
  "invoices": [
    {
      "id": "in_1234567890",
      "object": "invoice",
      "customer": "cus_1234567890",
      "status": "paid",
      "total": 2000,
      "currency": "usd"
    }
  ]
}
```

### 支払い情報の取得

```shellscript
curl -H "X-Auth-Key: your_secret_auth_key_here" http://localhost:8000/api/payments/example@email.com
```

レスポンス例：

```json
{
  "payments": [
    {
      "id": "pi_1234567890",
      "object": "payment_intent",
      "amount": 2000,
      "currency": "usd",
      "status": "succeeded",
      "customer": "cus_1234567890"
    }
  ]
}
```

### 商品情報の取得

```shellscript
curl -H "X-Auth-Key: your_secret_auth_key_here" http://localhost:8000/api/products/example@email.com
```

レスポンス例：

```json
{
  "products": [
    {
      "id": "prod_1234567890",
      "object": "product",
      "name": "Premium Plan",
      "active": true,
      "description": "Access to all premium features"
    }
  ]
}
```

## 注意事項

- `.env`ファイルには機密情報が含まれるため、Gitにコミットしないよう注意してください。
- 本番環境で使用する場合は、適切なセキュリティ対策（HTTPS、認証など）を実装してください。
- Stripe APIキーは定期的に更新することをお勧めします。


ご質問や問題がある場合は、GitHubのIssuesセクションでお問い合わせください。
