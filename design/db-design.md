# DB設計：間違いノートアプリ

## テーブル一覧

| テーブル | 役割 |
|---------|------|
| `users` | ユーザー情報 |
| `subjects` | 科目 |
| `units` | 単元（科目の下の階層） |
| `questions` | 問題 |
| `attempts` | 回答履歴 |
| `mistake_notes` | 間違いノート＋復習管理 |

---

## 各テーブル詳細

### `users`（ユーザー）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | UUID | 主キー |
| email | VARCHAR | メールアドレス |
| name | VARCHAR | 表示名 |
| created_at | TIMESTAMP | 作成日時 |

---

### `subjects`（科目）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | UUID | 主キー |
| user_id | UUID | → users |
| name | VARCHAR | 科目名（数学・英語など） |

---

### `units`（単元）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | UUID | 主キー |
| subject_id | UUID | → subjects |
| name | VARCHAR | 単元名（二次方程式など） |

---

### `questions`（問題）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | UUID | 主キー |
| user_id | UUID | → users |
| subject_id | UUID | → subjects |
| unit_id | UUID | → units（nullable） |
| question_text | TEXT | 問題文 |
| correct_answer | TEXT | 正解 |
| image_url | VARCHAR | 画像URL（S3） |
| created_at | TIMESTAMP | 作成日時 |

---

### `attempts`（回答履歴）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | UUID | 主キー |
| user_id | UUID | → users |
| question_id | UUID | → questions |
| user_answer | TEXT | 自分の答え |
| is_correct | BOOLEAN | 正解かどうか |
| answered_at | TIMESTAMP | 回答日時 |

---

### `mistake_notes`（間違いノート）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | UUID | 主キー |
| user_id | UUID | → users |
| question_id | UUID | → questions |
| memo | TEXT | 間違えた理由・ポイント |
| status | ENUM | active / mastered |
| wrong_count | INTEGER | 間違えた回数 |
| correct_streak | INTEGER | 連続正解数 |
| next_review_at | DATE | ユーザーが設定する次の復習日 |

---

## テーブル関係図

```
users
 ├──< subjects
 │      └──< units
 │
 ├──< questions >── subjects
 │                └── units（nullable）
 │
 ├──< attempts >── questions
 │
 └──< mistake_notes >── questions
```

---

## 設計のポイント

- `unit_id` はnullableにすることで、単元未分類の問題も登録できる
- `attempts` は同じ問題を何度解いても履歴として残る
- `mistake_notes` の `correct_streak` で連続正解数を管理し、`next_review_at` はユーザーが自分で次の復習日を設定する
- `status` が `mastered` になった問題は復習リストから外れる