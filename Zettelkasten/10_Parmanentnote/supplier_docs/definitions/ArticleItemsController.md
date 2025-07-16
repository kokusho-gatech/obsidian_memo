# ArticleItemsController（Articles::ArticleItemsController）

## 概要
- ファイルチェックページのコントローラー。
- `/articles/:id/article_items` で利用。

## アクション一覧

### index（15-22行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、所有者情報や履歴等をセット。
- **返すもの**: @ownr_info, @modification_histories, @article_wrapper_class, @is_file_check_page, @building_confirmations_count

### update（24-54行目）
- **受け取るもの**: params[:id], article_item_params, params[:item_name]
- **処理内容**: Articleを取得し、ファイルアップロード・認定謄本の更新ジョブ実行等。
- **返すもの**: JSONメッセージ（成功/失敗）

### files（56-63行目）
- **受け取るもの**: params[:id]
- **処理内容**: ArticleItemを取得し、画像セクションHTMLを返す。
- **返すもの**: JSON（image_section_html）

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 