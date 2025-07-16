# InventoriesController（Articles::InventoriesController）

## 概要
- 在庫管理（編集・販売可否・販売先・自己信託）
- `/articles/:id/inventories` で利用。

## アクション一覧

### edit（6-9行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleと販売先を取得。
- **返すもの**: @article, @sales_destination

### update_sale_available_status（11-22行目）
- **受け取るもの**: params[:id], params[:article][:sale_available_status]
- **処理内容**: Articleを取得し、販売可否を更新。
- **返すもの**: 編集画面へリダイレクト、メッセージ

### update_sales_destination（24-39行目）
- **受け取るもの**: params[:id], params[:sales_destination_id]
- **処理内容**: Articleと販売先を取得し、関連付けを更新。
- **返すもの**: 編集画面へリダイレクト、メッセージ

### update_jikoshintaku（41-56行目）
- **受け取るもの**: params[:id], params[:jikoshintaku_id]
- **処理内容**: Articleと自己信託を取得し、関連付けを更新。
- **返すもの**: 編集画面へリダイレクト、メッセージ

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 