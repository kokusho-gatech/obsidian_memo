# ReuploadDocusignFilesJob

## 概要
DocuSignで作成された契約書ファイルを再アップロードし、TechConsulシステムに通知を送信するバックグラウンドジョブ。

## 主な用途・処理内容
- API経由でDocuSignファイルの再アップロードリクエスト時に非同期で実行
- SalesContractFieldのステータスをready_contractに更新
- Connectors::TechConsulで外部システムに通知
- 成功・失敗に関わらず通知を送信
- エラー発生時はRollbarでエラーログを記録

## トリガー
- API経由でreupload_docusign_filesアクション実行時

## 扱うデータ
- SalesContractField（売買契約フィールド）
- Connectors::TechConsul（外部システム連携） 