# misnote

間違えた問題・苦手な問題を記録し、ユーザーが設定した日程で反復復習できる「デジタル間違いノート」アプリ。小中高生をメインターゲットとしています。

## 主要機能

- **問題登録** — 問題文・正解・メモ（間違えた理由やポイント）を登録
- **復習日設定** — 次に復習する日をユーザー自身が設定
- **今日の復習** — 復習日が来た問題を自動でリストアップ
- **克服済み管理** — 3回連続正解すると「克服済みにしますか？」と提案。ユーザーが確認して初めて mastered に移行
- **科目・単元管理** — 科目・単元ごとに問題を整理

## 技術スタック

| 領域 | 技術 |
|------|------|
| フロントエンド | Next.js / TypeScript / Tailwind CSS |
| バックエンド | FastAPI (Python) / SQLAlchemy / Alembic / Pydantic |
| DB | PostgreSQL |
| API連携 | FastAPI が自動生成する OpenAPI を openapi-generator で TypeScript クライアント化し、フロントエンドはそれを利用（fetch を直書きしない） |

将来的には Amazon Cognito（認証）/ API Gateway / ECS+Fargate / RDS へ移行予定（詳細は `docs/ROADMAP.md`）。現時点では認証は未実装で、全リクエストをシードユーザーとして扱う。

## ディレクトリ構成

```
misnote/
├── backend/   # FastAPI（実装済み）
├── frontend/  # Next.js（雛形のみ、未実装）
├── docs/      # 設計ドキュメント（DB / API / 画面設計）
└── docker-compose.yml
```

## セットアップ

### Docker を使う場合（推奨）

```bash
cp backend/.env.example backend/.env
docker compose up -d db
docker compose run --rm api alembic upgrade head   # 初回のみ：テーブル作成
docker compose up
```

### ローカルで直接起動する場合

**バックエンド**

```bash
cd backend
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json

**フロントエンド**

```bash
cd frontend
npm install
npm run dev
```

- http://localhost:3000

## ドキュメント

詳しい仕様は `docs/` 以下を参照してください。

- [アプリ概要](docs/design/overview.md)
- [DB設計](docs/design/db/design.md) / [テーブル定義](docs/design/db/schema.md)
- [API共通仕様](docs/design/api/conventions.md)
- [画面設計](docs/design/screens/)
- [実装ロードマップ](docs/ROADMAP.md)
