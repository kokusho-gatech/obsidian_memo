# SaleStatesController（Articles::SaleStatesController）

## 概要
- 物件の販売状態を更新するコントローラー。
- `/articles/:id/sale_states` で利用。

## アクション一覧

### update（6-16行目）
- **受け取るもの**: params[:id], params[:article][:sale_state]
- **処理内容**: Articleを取得し、Handlerで販売状態を更新。
- **返すもの**: フラッシュメッセージ、リダイレクト

---

[コントローラー一覧に戻る](../supplier_controllers_index.md)
 