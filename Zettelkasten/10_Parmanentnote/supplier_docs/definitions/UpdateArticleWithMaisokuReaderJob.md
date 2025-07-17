# UpdateArticleWithMaisokuReaderJob

## 概要
マイソク（図面）ファイルがアップロードされた際に、OCR技術を使ってマイソクの内容を自動で読み取り、Article情報を更新するバックグラウンドジョブ。

## 主な用途・処理内容
- 物件のマイソク読み取り準備が完了した時に非同期で実行
- Articleモデルを取得し、DocumentReader::Maisokuで内容を読み取り
- 読み取り結果をログ出力
- DocumentReader::Maisoku::ArticleUpdaterでArticle情報を更新
- 更新失敗時はログ出力

## トリガー
- Articleモデルのpost_maisoku_readerメソッド内

## 扱うデータ
- Article（物件情報）
- DocumentReader::Maisoku（マイソク読み取りサービス） 