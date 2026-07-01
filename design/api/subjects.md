# API：科目（subjects）

ベースURL: `https://api.misnote.com/v1` / 認証・エラー: [共通仕様](./conventions.md)

## エンドポイント一覧

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/subjects` | 科目一覧取得 |
| POST | `/subjects` | 科目作成 |
| PUT | `/subjects/{id}` | 科目更新 |
| DELETE | `/subjects/{id}` | 科目削除 |

---

## 科目一覧取得
`GET /subjects`

**レスポンス**
```json
[
  { "id": "uuid", "name": "数学" },
  { "id": "uuid", "name": "英語" }
]
```

---

## 科目作成
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

## 科目更新
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

## 科目削除
`DELETE /subjects/{id}`

**レスポンス**
- `204 No Content`（成功時）
- `409 Conflict`（紐づく単元または問題が存在する場合）

```json
// 409 の場合
{ "detail": "Subject has related units or questions" }
```

---

## 関連ドキュメント

- [共通仕様](./conventions.md)
- [単元API](./units.md)
- [DB: テーブル定義](../db/schema.md)
