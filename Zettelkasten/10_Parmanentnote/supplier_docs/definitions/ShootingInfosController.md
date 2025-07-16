# ShootingInfosController（Articles::ShootingInfosController）

## 概要
- 撮影依頼・解除の管理。
- `/articles/:id/shooting_infos` で利用。

## アクション一覧

### new（6-8行目）
- **受け取るもの**: params[:id]
- **処理内容**: ArticleをIDで取得。
- **返すもの**: @article（ビューで利用）

### create（10-15行目）
- **受け取るもの**: params[:id], params[:shooting_request_reason]
- **処理内容**: Articleを取得し、`shooting_request`を実行。
- **返すもの**: turbo_stream_reload（通知付き）

### destroy（17-22行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、`shooting_request_clear`を実行。
- **返すもの**: 編集画面へリダイレクト（通知付き）

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 