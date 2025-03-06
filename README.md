# Python Meet Space

## プロジェクト概要

Python Meet Space は、会議室予約システムの API と テスト用のフロントエンドを提供するアプリケーションです。
FastAPI を使用したバックエンド API と、Streamlit を使用したテスト用インターフェースで構成されています。

## 機能

- ユーザー管理: ユーザー情報の登録と取得
- 会議室管理: 会議室情報の登録と取得
- 予約管理: 会議室の予約情報の登録と取得

## 技術スタック

- バックエンド: FastAPI
- フロントエンド: Streamlit
- データモデル: Pydantic

## 使用方法

### バックエンド API の起動

```bash
uvicorn main:app --reload
```

### フロントエンドの起動

```bash
streamlit run app.py
```

## API エンドポイント

- `GET /`: ヘルスチェック
- `POST /users`: ユーザー情報の登録
- `POST /rooms`: 会議室情報の登録
- `POST /bookings`: 予約情報の登録

## 開発環境のセットアップ

1. 必要なパッケージのインストール

```bash
pip install fastapi uvicorn streamlit pydantic
```

2. リポジトリのクローン

```bash
git clone <repository-url>
cd python-meet-space
```

## ライセンス

このプロジェクトはオープンソースとして提供されています。
