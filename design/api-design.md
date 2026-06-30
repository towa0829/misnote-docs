# API設計

## 基本情報

| 項目 | 内容 |
|-----|-----|
| ベースURL | `https://api.misnote.com/v1` |
| 認証方式 | Amazon Cognito (JWTトークン) |
| データ形式 | JSON|

### 認証ヘッダー
```
Authorization: Bearer {CognitoのJWTトークン}
```

---

## エンドポイント一覧

### 科目（subjects）

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/subjects` | 科目一覧取得 |
| POST | `/subjects` | 科目作成 |
| PUT | `/subjects/{id}` | 科目更新 |
| DELETE | `/subjects/{id}` | 科目削除 |

### 単元（units）

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/subjects/{subject_id}/units` | 単元一覧取得 |
| POST | `/subjects/{subject_id}/units` | 単元作成 |
| PUT | `/units/{id}` | 単元更新 |
| DELETE | `/units/{id}` | 単元削除 |

### 問題（questions）

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/questions` | 問題一覧取得 |
| GET | `/questions/{id}` | 問題詳細取得 |
| POST | `/questions` | 問題作成 |
| PUT | `/questions/{id}` | 問題更新 |
| DELETE | `/questions/{id}` | 問題削除 |

### 回答（attempts）

| メソッド | パス | 説明 |
|---------|------|------|
| POST | `/questions/{id}/attempts` | 回答を記録 |

### 間違いノート（mistake_notes）

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/mistake-notes` | 苦手問題一覧取得 |
| GET | `/mistake-notes/today` | 今日の復習一覧取得 |
| GET | `/mistake-notes/mastered` | 克服済み一覧取得 |
| PUT | `/mistake-notes/{id}` | メモ・復習日を更新 |
| PUT | `/mistake-notes/{id}/mastered` | 克服済みに変更 |

---

## 詳細仕様

### 科目一覧取得
`GET /subjects`

**レスポンス**
```json
[
  { "id": "uuid", "name": "数学" },
  { "id": "uuid", "name": "英語" }
]
```

---

### 科目作成
`POST /subjects`

**リクエスト**
```json
{ "name": "数学" }
```

**レスポンス**
```json
{ "id": "uuid", "name": "数学" }
```

---

### 科目更新
`PUT /subjects/{id}`

**リクエスト**
```json
{ "name": "数学（改訂）" }
```

**レスポンス**
```json
{ "id": "uuid", "name": "数学（改訂）" }
```

---

### 科目削除
`DELETE /subjects/{id}`

**レスポンス**
- `204 No Content`（成功時）
- `409 Conflict`（紐づく単元または問題が存在する場合）

```json
// 409 の場合
{ "detail": "Subject has related units or questions" }
```

---

### 単元一覧取得
`GET /subjects/{subject_id}/units`

**レスポンス**
```json
[
  { "id": "uuid", "subject_id": "uuid", "name": "二次方程式" },
  { "id": "uuid", "subject_id": "uuid", "name": "因数分解" }
]
```

---

### 単元作成
`POST /subjects/{subject_id}/units`

**リクエスト**
```json
{ "name": "二次方程式" }
```

**レスポンス**
```json
{ "id": "uuid", "subject_id": "uuid", "name": "二次方程式" }
```

---

### 単元更新
`PUT /units/{id}`

**リクエスト**
```json
{ "name": "二次方程式（応用）" }
```

**レスポンス**
```json
{ "id": "uuid", "subject_id": "uuid", "name": "二次方程式（応用）" }
```

---

### 単元削除
`DELETE /units/{id}`

**レスポンス**
- `204 No Content`（成功時）
- `409 Conflict`（紐づく問題が存在する場合）

```json
// 409 の場合
{ "detail": "Unit has related questions" }
```

---

### 問題一覧取得
`GET /questions`

**クエリパラメータ**

| パラメータ | 型 | 必須 | 説明 |
|-----------|-----|------|------|
| subject_id | UUID | No | 科目で絞り込む |
| unit_id | UUID | No | 単元で絞り込む |

**レスポンス**
```json
[
  {
    "id": "uuid",
    "subject": { "id": "uuid", "name": "数学" },
    "unit": { "id": "uuid", "name": "二次方程式" },
    "question_text": "次の方程式を解け: 2x + 3 = 7",
    "correct_answer": "x = 2",
    "created_at": "2024-01-01T00:00:00"
  }
]
```

> `unit` は登録時に未指定の場合 `null` になる

---

### 問題詳細取得
`GET /questions/{id}`

**レスポンス**
```json
{
  "id": "uuid",
  "subject": { "id": "uuid", "name": "数学" },
  "unit": { "id": "uuid", "name": "二次方程式" },
  "question_text": "次の方程式を解け: 2x + 3 = 7",
  "correct_answer": "x = 2",
  "created_at": "2024-01-01T00:00:00"
}
```

---

### 問題作成
`POST /questions`

**リクエスト**
```json
{
  "subject_id": "uuid",
  "unit_id": "uuid",
  "question_text": "次の方程式を解け: 2x + 3 = 7",
  "correct_answer": "x = 2"
}
```

> `unit_id` は省略可（null 可）

**レスポンス**
```json
{
  "id": "uuid",
  "subject": { "id": "uuid", "name": "数学" },
  "unit": { "id": "uuid", "name": "二次方程式" },
  "question_text": "次の方程式を解け: 2x + 3 = 7",
  "correct_answer": "x = 2",
  "created_at": "2024-01-01T00:00:00"
}
```

---

### 問題更新
`PUT /questions/{id}`

**リクエスト**
```json
{
  "subject_id": "uuid",
  "unit_id": "uuid",
  "question_text": "次の方程式を解け: 3x + 6 = 12",
  "correct_answer": "x = 2"
}
```

**レスポンス** — `GET /questions/{id}` と同じ形

---

### 問題削除
`DELETE /questions/{id}`

**レスポンス**
- `204 No Content`

> 紐づく `attempts`・`mistake_notes` もカスケード削除される

---

### 回答を記録
`POST /questions/{id}/attempts`

**リクエスト**
```json
{
  "user_answer": "x = 3",
  "is_correct": false
}
```

**レスポンス**
```json
{
  "id": "uuid",
  "question_id": "uuid",
  "user_answer": "x = 3",
  "is_correct": false,
  "answered_at": "2024-01-01T00:00:00",
  "mistake_note_id": "uuid"
}
```

> 不正解の場合、`mistake_notes` に自動でレコードが追加される（`next_review_at` は `null` で作成され、ユーザーが後から設定する）。正解の場合 `mistake_note_id` は `null`

---

### 苦手問題一覧取得
`GET /mistake-notes`

status が `active` の一覧を返す。

**レスポンス**
```json
[
  {
    "id": "uuid",
    "question": {
      "id": "uuid",
      "question_text": "次の方程式を解け: 2x + 3 = 7",
      "correct_answer": "x = 2"
    },
    "memo": "符号のミスに注意",
    "status": "active",
    "wrong_count": 3,
    "next_review_at": "2024-01-08"
  }
]
```

---

### 今日の復習一覧取得
`GET /mistake-notes/today`

`next_review_at` が今日以前で `status` が `active` の一覧を返す。

**レスポンス**
```json
[
  {
    "id": "uuid",
    "question": {
      "id": "uuid",
      "question_text": "次の方程式を解け: 2x + 3 = 7",
      "correct_answer": "x = 2"
    },
    "memo": "符号のミスに注意",
    "wrong_count": 3,
    "next_review_at": "2024-01-01"
  }
]
```

---

### 克服済み一覧取得
`GET /mistake-notes/mastered`

status が `mastered` の一覧を返す。

**レスポンス**
```json
[
  {
    "id": "uuid",
    "question": {
      "id": "uuid",
      "question_text": "次の方程式を解け: 2x + 3 = 7",
      "correct_answer": "x = 2"
    },
    "memo": "符号のミスに注意",
    "status": "mastered",
    "wrong_count": 3,
    "next_review_at": null
  }
]
```

---

### メモ・復習日を更新
`PUT /mistake-notes/{id}`

**リクエスト**
```json
{
  "memo": "符号のミスに注意。移項するとき符号が変わる",
  "next_review_at": "2024-01-08"
}
```

**レスポンス**
```json
{
  "id": "uuid",
  "memo": "符号のミスに注意。移項するとき符号が変わる",
  "next_review_at": "2024-01-08",
  "status": "active"
}
```

---

### 克服済みに変更
`PUT /mistake-notes/{id}/mastered`

リクエストボディなし。

**レスポンス**
```json
{
  "id": "uuid",
  "status": "mastered",
  "question": {
    "id": "uuid",
    "question_text": "次の方程式を解け: 2x + 3 = 7",
    "correct_answer": "x = 2"
  },
  "memo": "符号のミスに注意",
  "wrong_count": 3,
  "next_review_at": null
}
```

---

## エラーレスポンス

| ステータスコード | 意味 |
|----------------|------|
| 400 | リクエストの形式が間違っている |
| 401 | 認証エラー（トークンが無効） |
| 403 | 権限エラー（他のユーザーのデータにアクセス） |
| 404 | データが見つからない |
| 409 | 競合エラー（紐づくデータが存在するため削除不可） |
| 500 | サーバーエラー |

**エラーレスポンスの形式**
```json
{
  "detail": "Question not found"
}
```

---

## OpenAPI Generator

### 概要

FastAPIは実装するだけで `openapi.yaml` を自動生成する。
そのyamlをopenapi-generatorに渡すことで、Next.js用のコードを自動生成できる。

### 生成されるもの

| 生成物 | 使う場所 | 説明 |
|--------|---------|------|
| TypeScript型定義 | Next.js | APIのリクエスト・レスポンスの型 |
| APIクライアント | Next.js | fetchを自分で書かなくていい |

### 手順

**① FastAPI起動後、yamlを取得**
```bash
curl http://localhost:8000/openapi.json -o openapi.yaml
```

**② openapi-generatorでNext.js用コードを生成**
```bash
openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-fetch \
  -o ./frontend/src/generated
```

**③ 生成されたコードを使う**
```typescript
// 自分でfetchを書く代わりにこれだけでOK
import { QuestionsApi } from '@/generated'

const api = new QuestionsApi()
const questions = await api.getQuestions()
```

### 生成されるフォルダ構成

```
frontend/src/generated/
├── apis/
│   ├── QuestionsApi.ts
│   ├── MistakeNotesApi.ts
│   └── SubjectsApi.ts
└── models/
    ├── Question.ts
    ├── MistakeNote.ts
    └── Attempt.ts
```

## 関連ドキュメント

- [アプリ概要](./overview.md)
- [DB設計](./db-design.md)
- [画面設計](./screen-design.md)
