# SupplierMailsController

## 役割
このコントローラは[[SupplierMail]]モデルの仕入メール管理（新規作成）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["authenticate_userで認証"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"new"| "D1"["新規作成フォーム→[[supplier_mails/new.html.erb]]表示"]
  "C" -->|"create"| "D2"["新規作成→保存→リダイレクトor再表示"]
```

## アクション一覧
- `new`: 新規作成フォームを表示。
- `create`: 新規仕入メールを作成。成功時は未処理メール画面へリダイレクト、失敗時は再表示。

## コールバック
- `before_action :authenticate_user`（管理者のみ許可）。

## Strong Parameters
- `supplier_mail_params`:
  - 許可: `:gmail_message_id`, `:from`, `:to`, `:cc`, `:subject`, `:received_at`, `:body`, `:intermediary_company_id`, `:intermediary_domain_id` 