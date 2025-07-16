# IntermediaryStaffsController

## 役割
このコントローラは[[IntermediaryStaff]]モデルの仲介担当者管理（一覧表示、新規作成、編集、削除）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["仲介担当者一覧取得→[[intermediary_staffs/index.html.erb]]表示"]
  "C" -->|"new"| "D2"["新規作成フォーム→[[intermediary_staffs/new.html.erb]]表示"]
  "C" -->|"edit"| "D3"["編集フォーム→[[intermediary_staffs/edit.html.erb]]表示"]
  "C" -->|"create"| "D4"["新規作成→保存→リダイレクトor再表示"]
  "C" -->|"update"| "D5"["編集→保存→リダイレクトor再表示"]
  "C" -->|"destroy"| "D6"["削除→リダイレクト"]
```

## アクション一覧
- `index`: 仲介担当者一覧を取得し、[[intermediary_staffs/index.html.erb]]を表示。
- `new`: 新規作成フォームを表示。
- `edit`: 編集フォームを表示。
- `create`: 新規仲介担当者を作成。成功時は親会社編集画面へリダイレクト、失敗時は再表示。
- `update`: 仲介担当者情報を更新。成功時は親会社編集画面へリダイレクト、失敗時は再表示。
- `destroy`: 仲介担当者を削除し、親会社編集画面へリダイレクト。

## コールバック
- 各アクションで親会社（[[IntermediaryCompany]]）の取得。

## Strong Parameters
- `intermediary_staff_params`:
  - 許可: `:email`, `:name`, `:phone_number`, `user_ids: []` 