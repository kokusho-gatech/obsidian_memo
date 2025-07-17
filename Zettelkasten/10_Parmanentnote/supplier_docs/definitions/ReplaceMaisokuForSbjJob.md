# ReplaceMaisokuForSbjJob

## 概要
マイソク（図面）ファイルがアップロードされた際に、SBJ（不動産投資信託）用のマイソクを自動生成するバックグラウンドジョブ。

## 主な用途・処理内容
- マイソクファイルのアップロード完了時に非同期で実行
- Articleとユーザーを取得し、article.replace_maisoku_for_sale!を呼び出してSBJ用マイソクを生成
- エラー発生時はログ出力とNotifier.reportでエラー通知

## トリガー
- ArticleItemsPageでのマイソクファイル作成後のコールバック

## 扱うデータ
- Article（物件情報）
- User（マイソク作成者）
- ArticleItemFile（マイソクファイル） 