# UsersController

## 役割

`UsersController`は、ユーザーの一覧表示、詳細表示、新規作成、編集、更新、Gmail認証など、ユーザー管理に関する全ての処理を担当します。主に管理者がユーザー情報を管理するためのコントローラです。

---

## 処理フロー（Mermaid記法）

```mermaid
graph TD
  A[リクエスト受信] -->|index| B[ユーザー一覧取得→[[users/index.html.erb]]表示]
  A -->|show| C[ユーザー詳細取得→[[users/show.html.erb]]表示]
  A -->|new| D[管理者判定→新規ユーザー作成画面[[users/new.html.erb]]]
  A -->|edit| E[管理者判定→ユーザー編集画面[[users/edit.html.erb]]]
  A -->|create| F[管理者判定→ユーザー新規作成→成功:一覧へ/失敗:フォーム再表示]
  A -->|update| G[管理者判定→ユーザー更新→成功:一覧へ/失敗:フォーム再表示]
  A -->|login| H[ログイン状態判定→ユーザー詳細orGoogle認証へリダイレクト]
  A -->|authorize_gmail| I[Gmail認証処理→ユーザー詳細へリダイレクト]
  A -->|clear_gmail_authorization| J[Gmail認証解除→ユーザー詳細へリダイレクト]
```

---

## アクション一覧

| アクション名 | 概要 | レンダリング/リダイレクト先 |
|---|---|---|
| index | ユーザー一覧を表示。[[User]]の検索・一覧取得 | [[users/index.html.erb]] |
| show | ユーザー詳細を表示。Gmail認証URLも表示 | [[users/show.html.erb]] |
| new | 新規ユーザー作成フォームを表示（管理者のみ） | [[users/new.html.erb]] |
| edit | ユーザー編集フォームを表示（管理者のみ） | [[users/edit.html.erb]] |
| create | ユーザー新規作成（管理者のみ）。成功時は一覧へ、失敗時はフォーム再表示 | [[users/new.html.erb]] |
| update | ユーザー情報更新（管理者のみ）。成功時は一覧へ、失敗時はフォーム再表示 | [[users/edit.html.erb]] |
| login | ログイン状態に応じてユーザー詳細またはGoogle認証へリダイレクト | なし（リダイレクト） |
| authorize_gmail | Gmail認証処理。成功/失敗でユーザー詳細へリダイレクト | なし（リダイレクト） |
| clear_gmail_authorization | Gmail認証解除。ユーザー詳細へリダイレクト | なし（リダイレクト） |

---

## コールバック

- `before_action :authenticate_user!`（except: :login）
  - ログインしていない場合は認証を要求
- `skip_before_action :verify_authenticity_token`（only: :create）
  - createアクションでCSRFトークン検証をスキップ
- `skip_before_action :reject_unauthorized_user`（only: :create）
  - createアクションで権限チェックをスキップ

---

## Strong Parameters

- `create_params`
  - 許可: `:name`, `:email`, `:mobile_phone`, `:leave`, `:type`, `authority: []`
- `update_params`
  - 許可: `:name`, `:mobile_phone`, `:leave`, `:type`, `authority: []`
- `search_params`
  - 許可: `:name`, `:email`, `:leave`, `:type`, `:authority`

---

## 関連モデル・ビュー

- モデル: [[User]]
- ビュー: [[users/index.html.erb]], [[users/show.html.erb]], [[users/new.html.erb]], [[users/edit.html.erb]], [[users/_form.html.erb]] 