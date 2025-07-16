# ManagementController

## 役割
このコントローラは[[Article]]モデルの交渉管理（交渉一覧・詳細画面へのリダイレクト）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["交渉一覧取得→[[management/index.html.erb]]表示"]
  "C" -->|"show"| "D2"["権限に応じて詳細編集画面へリダイレクト"]
```

## アクション一覧
- `index`: 交渉一覧を取得し、[[management/index.html.erb]]を表示。
- `show`: 権限に応じてfor_approvalまたはfor_payment_requestの編集画面へリダイレクト。

## コールバック
- 権限チェック（current_user.has_auth?(:contract_manager)）をshowアクションで実施。

## Strong Parameters
- `index_form_permitted_params`:
  - 許可: `Article::Management::IndexForm.permit_arguments`（詳細は[[Article]]参照） 