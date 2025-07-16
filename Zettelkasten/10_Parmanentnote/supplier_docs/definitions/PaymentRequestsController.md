# PaymentRequestsController（Articles::PaymentRequestsController）

## 概要
- 支払依頼の更新・送信管理。
- `/articles/:id/payment_requests` で利用。

## アクション一覧

### update（6-17行目）
- **受け取るもの**: params[:id], update_payment_request_params
- **処理内容**: Articleを取得し、フォームで保存。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

### send_to_flow（19-30行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、送信処理を実行。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 