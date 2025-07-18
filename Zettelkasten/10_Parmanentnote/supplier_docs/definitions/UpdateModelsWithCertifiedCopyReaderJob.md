# UpdateModelsWithCertifiedCopyReaderJob

## 概要
謄本ファイルがアップロードされた際に、OCR技術を使って謄本の内容を自動で読み取り、Article情報や売買契約フィールド、入力謄本モデルを更新するバックグラウンドジョブ。

## 主な用途・処理内容
- 謄本ファイルのアップロード時に非同期で実行
- PDF形式のファイルを対象
- Article、SalesContractField、InputCertifiedCopyなど関連モデルを取得
- CertifiedCopy::ApiClient.readで謄本内容を読み取り
- 専用アップデーターで各モデルを更新
- Slack通知で物件URLと更新結果を送信

## トリガー
- API経由やArticleItemsPageでの謄本ファイルアップロード時

## 扱うデータ
- [[Article]]（物件情報）
- [[SalesContractField]]（売買契約フィールド）
- [[InputCertifiedCopy]]（入力謄本データ）
- [[ArticleItem]]（物件資料項目）
- [[ArticleItemFile]]（物件資料ファイル） 