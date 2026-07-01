# API：単元（units）

ベースURL: `https://api.misnote.com/v1` / 認証・エラー: [共通仕様](./conventions.md)

## エンドポイント一覧

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/subjects/{subject_id}/units` | 単元一覧取得 |
| POST | `/subjects/{subject_id}/units` | 単元作成 |
| PUT | `/units/{id}` | 単元更新 |
| DELETE | `/units/{id}` | 単元削除 |

---

## 単元一覧取得
`GET /subjects/{subject_id}/units`

**レスポンス**
```json
[
  { "id": "uuid", "subject_id": "uuid", "name": "二次方程式" },
  { "id": "uuid", "subject_id": "uuid", "name": "因数分解" }
]
```

---

## 単元作成
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

## 単元更新
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

## 単元削除
`DELETE /units/{id}`

**レスポンス**
- `204 No Content`（成功時）
- `409 Conflict`（紐づく問題が存在する場合）

```json
// 409 の場合
{ "detail": "Unit has related questions" }
```

---

## 関連ドキュメント

- [共通仕様](./conventions.md)
- [科目API](./subjects.md)
- [問題API](./questions.md)
- [DB: テーブル定義](../db/schema.md)
