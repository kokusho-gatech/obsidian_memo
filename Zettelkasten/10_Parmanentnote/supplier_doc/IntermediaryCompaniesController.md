# IntermediaryCompaniesController

## 役割
このコントローラは[[IntermediaryCompany]]モデルの仲介会社管理（一覧表示、新規作成、編集、削除）を担当します。

## 処理フロー
```mermaid
graph TD
  A[リクエスト受信] -->|before_action| B[認証・権限チェック]
  B --> C{アクション分岐}
  C -->|index| D1[仲介会社一覧取得→[[intermediary_companies/index.html.erb]]表示]
  C -->|new| D2[新規作成フォーム→[[intermediary_companies/new.html.erb]]表示]
  C -->|edit| D3[編集フォーム→[[intermediary_companies/edit.html.erb]]表示]
  C -->|create| D4[新規作成→保存→リダイレクトor再表示]
  C -->|update| D5[編集→保存→リダイレクトor再表示]
  C -->|destroy| D6[削除→リダイレクト]
```

## アクション一覧
- `index`: 仲介会社一覧を取得し、[[intermediary_companies/index.html.erb]]を表示。
- `new`: 新規作成フォームを表示。
- `edit`: 編集フォームを表示。
- `create`: 新規仲介会社を作成。成功時は一覧へリダイレクト、失敗時は再表示。
- `update`: 仲介会社情報を更新。成功時は編集画面へリダイレクト、失敗時は再表示。
- `destroy`: 仲介会社を削除し、一覧へリダイレクト。

## コールバック
- 権限チェック（contract_manager?）などを各アクションで実施。

## Strong Parameters
- `intermediary_company_params`:
  - 許可: `user_id`, `lead_source`, `name`, `branch_name`, `representative_name`, `zip`, `prefecture_id`, `state`, `city`, `street`, `tel`, `foundation_date`, `website`（編集可能時） 