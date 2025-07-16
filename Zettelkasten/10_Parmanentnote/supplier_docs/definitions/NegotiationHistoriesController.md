# NegotiationHistoriesController（Articles::NegotiationHistoriesController）

## 概要
- 交渉履歴の新規作成・保存。
- `/articles/:id/negotiation_histories` で利用。

## アクション一覧

### new（6-9行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、フォームを初期化。
- **返すもの**: @article, @form

### create（11-39行目）
- **受け取るもの**: params[:id], negotiation_history_params
- **処理内容**: Articleを取得し、フォームで保存。Turbo Frameかどうかで分岐し、リダイレクトや描画を制御。
- **返すもの**: フラッシュメッセージ、リダイレクトまたはビュー描画

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 