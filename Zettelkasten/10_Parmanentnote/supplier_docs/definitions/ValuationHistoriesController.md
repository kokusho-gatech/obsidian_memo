# ValuationHistoriesController（Articles::ValuationHistoriesController）

## 概要
- 銀行評価履歴の編集・更新。
- `/articles/:id/valuation_histories` で利用。

## アクション一覧

### edit（6-15行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、編集権限やフォームをセット。
- **返すもの**: @article, @is_valuation_histories_editable_user, @valuation_histories_form

### update（17-34行目）
- **受け取るもの**: params[:id], valuation_histories_params
- **処理内容**: Articleを取得し、フォームで更新。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 