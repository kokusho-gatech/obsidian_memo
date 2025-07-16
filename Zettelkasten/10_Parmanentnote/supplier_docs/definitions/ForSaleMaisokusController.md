# ForSaleMaisokusController（Articles::ForSaleMaisokusController）

## 概要
- マイソク作成・編集。
- `/articles/:id/for_sale_maisokus` で利用。

## アクション一覧

### edit（8-32行目）
- **受け取るもの**: params[:id]
- **処理内容**: Article・ArticleItem・ファイルタブ・マイソク情報等をセット。
- **返すもの**: 各種インスタンス変数（ビューで利用）

### update（34-56行目）
- **受け取るもの**: params[:id], article_params
- **処理内容**: Articleを更新し、リリース処理や通知を実行。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト or エラー時はメッセージ

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 