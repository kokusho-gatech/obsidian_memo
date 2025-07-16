# LabelsController

## 役割
このコントローラは[[Label]]モデルのラベル管理（一覧表示、新規作成、編集、削除）を担当します。主にドキュメント進捗管理用のラベルを操作します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["ラベル一覧取得→[[labels/index.html.erb]]表示"]
  "C" -->|"new"| "D2"["新規作成フォーム→[[labels/new.html.erb]]表示"]
  "C" -->|"edit"| "D3"["編集フォーム→[[labels/edit.html.erb]]表示"]
  "C" -->|"create"| "D4"["新規作成→保存→リダイレクトor再表示"]
  "C" -->|"update"| "D5"["編集→保存→リダイレクトor再表示"]
```

## アクション一覧
- `index`: ラベル一覧を取得し、[[labels/index.html.erb]]を表示。
- `new`: 新規作成フォームを表示。
- `edit`: 編集フォームを表示。
- `create`: 新規ラベルを作成。成功時は一覧へリダイレクト、失敗時は再表示。
- `update`: ラベル情報を更新。成功時は一覧へリダイレクト、失敗時は再表示。

## コールバック
- 各アクションで`current_user.document_admin?`による権限チェック。

## Strong Parameters
- `label_params`:
  - 許可: `:target_type`, `:name`, `:short_name`, `:description`, `:color`, `:active`, `:position` 