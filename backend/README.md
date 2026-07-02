# misnote-backend

misnote の FastAPI バックエンド。

## 技術スタック

- Python 3.12+
- FastAPI
- SQLAlchemy 2.0 + Alembic
- PostgreSQL 16
- Pydantic v2

## 起動方法

### Docker を使う場合（推奨）

環境変数を設定してから、リポジトリルートの `docker-compose.yml` で起動します。venv は不要です。

```bash
cp .env.example .env
cd ..
docker compose up
```

### ローカルで直接起動する場合

PostgreSQL を別途起動した上で、venv を作成して起動します。

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## マイグレーション

```bash
# 初回：マイグレーションファイルを自動生成
alembic revision --autogenerate -m "init"

# DB に適用
alembic upgrade head

# ロールバック
alembic downgrade -1
```

## API ドキュメント

起動後に以下の URL で確認できます。

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

## ディレクトリ構成

```
misnote-backend/
├── app/
│   ├── main.py        # FastAPI アプリ・ルーター登録
│   ├── config.py      # 環境変数の読み込み
│   ├── database.py    # DB 接続・Base
│   ├── deps.py        # 共通 Depends（DB セッション等）
│   ├── models/        # SQLAlchemy モデル（6テーブル）
│   ├── schemas/       # Pydantic スキーマ
│   └── routers/       # エンドポイント
├── alembic/           # マイグレーション管理
├── alembic.ini
├── requirements.txt
└── Dockerfile
```

## 環境変数

| 変数名 | 説明 | デフォルト |
|--------|------|-----------|
| `DATABASE_URL` | PostgreSQL 接続文字列 | `postgresql://misnote:misnote@localhost:5432/misnote` |
| `SECRET_KEY` | JWT 署名キー（Phase 3 で使用） | `change-me-in-production` |
