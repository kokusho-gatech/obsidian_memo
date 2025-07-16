# ArticleItemFilesController（Articles::ArticleItemFilesController）

## 概要
- ファイルアップロード履歴・削除・ダウンロード管理。
- `/articles/:id/article_item_files` で利用。

## アクション一覧

### index（10-15行目）
- **受け取るもの**: params[:id], params[:viewed_from]
- **処理内容**: ArticleとそのArticleItem一覧を取得。
- **返すもの**: ビュー（ファイルアップロード履歴）

### destroy（17-28行目）
- **受け取るもの**: params[:article_item_file_id]
- **処理内容**: ArticleItemFileを取得し削除。
- **返すもの**: JSON（成功/失敗）

### download（30-77行目）
- **受け取るもの**: params[:id], params[:item_ids]
- **処理内容**: Articleと関連ファイルを取得しZIP化、送信。
- **返すもの**: ZIPファイル（ダウンロード）

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 