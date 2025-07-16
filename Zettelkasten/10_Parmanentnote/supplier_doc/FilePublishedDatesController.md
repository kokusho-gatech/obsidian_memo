# FilePublishedDatesController

## 役割
このコントローラは[[FilePublishedDate]]モデルのファイル公開日管理（新規作成・編集・削除など）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["公開日一覧取得→[[file_published_dates/index.html.erb]]表示"]
  "C" -->|"new"| "D2"["新規作成フォーム→[[file_published_dates/new.html.erb]]表示"]
  "C" -->|"edit"| "D3"["編集フォーム→[[file_published_dates/edit.html.erb]]表示"]
  "C" -->|"create"| "D4"["新規作成→保存→リダイレクトor再表示"]
  "C" -->|"update"| "D5"["編集→保存→リダイレクトor再表示"]
  "C" -->|"destroy"| "D6"["削除→リダイレクト"]
```

## アクション一覧
- `index`: 公開日一覧を取得し、[[file_published_dates/index.html.erb]]を表示。
- `new`: 新規作成フォームを表示。
- `edit`: 編集フォームを表示。
- `create`: 新規公開日を作成。成功時は一覧へリダイレクト、失敗時は再表示。
- `update`: 公開日情報を更新。成功時は一覧へリダイレクト、失敗時は再表示。
- `destroy`: 公開日を削除し、一覧へリダイレクト。

## コールバック
- 各アクションで認証・権限チェック（ApplicationController由来）。

## Strong Parameters
- `file_published_date_params`:
  - 許可: `:published_at`, `:file_id`, `:description` 