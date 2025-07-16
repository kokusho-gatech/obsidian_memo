# UnprocessedMailsController

## 役割
このコントローラは[[UnprocessedMail]]モデルの未処理メール管理（一覧表示、新規作成、編集、削除など）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["未処理メール一覧取得→[[unprocessed_mails/index.html.erb]]表示"]
  "C" -->|"new"| "D2"["新規作成フォーム→[[unprocessed_mails/new.html.erb]]表示"]
  "C" -->|"edit"| "D3"["編集フォーム→[[unprocessed_mails/edit.html.erb]]表示"]
  "C" -->|"create"| "D4"["新規作成→保存→リダイレクトor再表示"]
  "C" -->|"update"| "D5"["編集→保存→リダイレクトor再表示"]
  "C" -->|"destroy"| "D6"["削除→リダイレクト"]
```

## アクション一覧
- `index`: 未処理メール一覧を取得し、[[unprocessed_mails/index.html.erb]]を表示。
- `new`: 新規作成フォームを表示。
- `edit`: 編集フォームを表示。
- `create`: 新規未処理メールを作成。成功時は一覧へリダイレクト、失敗時は再表示。
- `update`: 未処理メール情報を更新。成功時は一覧へリダイレクト、失敗時は再表示。
- `destroy`: 未処理メールを削除し、一覧へリダイレクト。

## コールバック
- 各アクションで認証・権限チェック（ApplicationController由来）。

## Strong Parameters
- `unprocessed_mail_params`:
  - 許可: `:subject`, `:body`, `:from`, `:to`, `:received_at`, `:status`, `:user_id` 