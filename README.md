# Stripe API FastAPI Application

## 概要

このプロジェクトは、StripeのAPIを使用して顧客情報、サブスクリプション、請求書、支払い、および商品情報を取得するFastAPIアプリケーションです。メールアドレスを使用して、関連する情報をJSON形式で取得できます。

## 機能

- 顧客情報の取得
- サブスクリプション情報の取得
- 請求書情報の取得
- 支払い情報の取得
- 商品情報の取得

## 技術スタック

- Python 3.9+
- FastAPI
- Stripe Python Library
- Docker

## セットアップ

### 前提条件

- Python 3.9以上
- pip
- Docker (オプション)

### インストール

1. リポジトリをクローンします：

```

git clone [https://github.com/yourusername/stripe-api-fastapi.git](https://github.com/yourusername/stripe-api-fastapi.git)
cd stripe-api-fastapi

```

2. 仮想環境を作成し、アクティベートします：

```

python -m venv venv
source venv/bin/activate  # Linuxの場合

# venv\Scripts\activate  # Windowsの場合

```

3. 依存関係をインストールします：

```

pip install -r requirements.txt

```

4. `.env`ファイルを作成し、Stripe APIキーを設定します：

```

STRIPE_API_KEY=your_stripe_api_key_here

```

### Dockerを使用する場合

1. Dockerイメージをビルドします：

```

docker-compose build

```

2. Dockerコンテナを起動します：

```

docker-compose up

```

## 使用方法

### ローカルで実行

1. アプリケーションを起動します：

```

uvicorn app.main:app --reload

```

2. ブラウザで `http://localhost:8000/docs` にアクセスし、Swagger UIを使用してAPIをテストします。

### Dockerで実行

1. Dockerコンテナを起動します：

```

docker-compose up

```

2. ブラウザで `http://localhost:8000/docs` にアクセスし、Swagger UIを使用してAPIをテストします。

## APIエンドポイント

- `/api/customers/{email}`: 指定されたメールアドレスに関連する顧客情報を取得
- `/api/subscriptions/{email}`: 指定されたメールアドレスに関連するサブスクリプション情報を取得
- `/api/invoices/{email}`: 指定されたメールアドレスに関連する請求書情報を取得
- `/api/payments/{email}`: 指定されたメールアドレスに関連する支払い情報を取得
- `/api/products/{email}`: 指定されたメールアドレスに関連する商品情報を取得

## テスト

テストを実行するには、以下のコマンドを使用します：

```

pytest

```

## 注意事項

- 本番環境では、適切なセキュリティ対策（HTTPS、認証など）を実装してください。
- Stripe APIキーは安全に管理し、公開リポジトリにコミットしないよう注意してください。
- 大量のデータを扱う場合は、ページネーションの実装を検討してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 貢献

プルリクエストは歓迎します。大きな変更を加える場合は、まずissueを開いて変更内容を議論してください。

## 連絡先

質問や提案がある場合は、[issues](https://github.com/DaisukeHori/stripe-api-fastapi/issues)を開いてください。
