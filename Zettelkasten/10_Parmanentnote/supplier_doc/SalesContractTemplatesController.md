# SalesContractTemplatesController

## 役割
このコントローラは[[SalesContractTemplate]]モデルの売買契約テンプレート管理（一覧表示、編集）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["テンプレート一覧取得→[[sales_contract_templates/index.html.erb]]表示"]
  "C" -->|"edit"| "D2"["編集フォーム→[[sales_contract_templates/edit.html.erb]]表示"]
  "C" -->|"update"| "D3"["編集→保存→リダイレクトor再表示"]
```

## アクション一覧
- `index`: テンプレート一覧を取得し、[[sales_contract_templates/index.html.erb]]を表示。
- `edit`: 編集フォームを表示。
- `update`: テンプレート情報を更新。成功時は一覧へリダイレクト、失敗時は再表示。

## コールバック
- 各アクションで`current_user.has_auth?(:sales_contract_template_editor)`による権限チェック。

## Strong Parameters
- `sales_contract_template_params`:
  - 許可: `:sales_agreement_remarks_2`, `:sales_agreement_remarks_3`, `:sales_agreement_remarks_4`, `:sales_agreement_remarks_5`, `:presentation_of_important_info_remarks_15`, `:presentation_of_important_info_remarks_16`, `:seller_remarks`, `:fix_property_tax_liquidation_money_from`, `:has_cancellation_by_loan_usage_special_contract` 