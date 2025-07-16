# UsersController

## 役割
このコントローラは[[User]]モデルの管理（一覧表示、詳細表示、新規作成、編集、削除、Gmail認証など）を担当します。主に管理者がユーザー情報を操作するための機能を提供します。

## 処理フロー
```mermaid
graph TD
  A[リクエスト受信] -->|before_action| B[認証・権限チェック]
  B --> C{アクション分岐}
  C -->|index| D1[ユーザー一覧取得→[[users/index.html.erb]]表示]
  C -->|show| D2[ユーザー詳細取得→[[users/show.html.erb]]表示]
  C -->|new| D3[新規ユーザー作成フォーム→[[users/new.html.erb]]表示]
  C -->|edit| D4[ユーザー編集フォーム→[[users/edit.html.erb]]表示]
  C -->|create| D5[ユーザー新規作成→保存→リダイレクトor[[users/new.html.erb]]再表示]
  C -->|update| D6[ユーザー情報更新→保存→リダイレクトor[[users/edit.html.erb]]再表示]
  C -->|login| D7[ログイン状態判定→リダイレクト]
  C -->|authorize_gmail| D8[Gmail認証処理→リダイレクト]
  C -->|clear_gmail_authorization| D9[Gmail認証解除→リダイレクト]
```

## アクション一覧
- `index`: ユーザー一覧を取得し、[[users/index.html.erb]]を表示。
- `show`: 指定ユーザーの詳細を取得し、[[users/show.html.erb]]を表示。
- `new`: 管理者のみ新規ユーザー作成フォーム（[[users/new.html.erb]]）を表示。
- `edit`: 管理者のみユーザー編集フォーム（[[users/edit.html.erb]]）を表示。
- `create`: 管理者のみ新規ユーザーを作成。成功時は一覧へリダイレクト、失敗時は[[users/new.html.erb]]再表示。
- `update`: 管理者のみユーザー情報を更新。成功時は一覧へリダイレクト、失敗時は[[users/edit.html.erb]]再表示。
- `login`: ログイン状態に応じてユーザー詳細またはGoogle認証ページへリダイレクト。
- `authorize_gmail`: Gmail認証コードを受け取り、認証処理後ユーザー詳細へリダイレクト。
- `clear_gmail_authorization`: Gmail認証情報を削除し、ユーザー詳細へリダイレクト。

## コールバック
- `before_action :authenticate_user!`（except: :login）: ログイン済みユーザーのみ許可。
- `skip_before_action :verify_authenticity_token`（only: :create）: create時にCSRFチェックをスキップ。
- `skip_before_action :reject_unauthorized_user`（only: :create）: create時に権限チェックをスキップ。

## Strong Parameters
- `create_params`:
  - 許可: `:name`, `:email`, `:mobile_phone`, `:leave`, `:type`, `authority: []`
- `update_params`:
  - 許可: `:name`, `:mobile_phone`, `:leave`, `:type`, `authority: []`
- `search_params`:
  - 許可: `:name`, `:email`, `:leave`, `:type`, `:authority` 