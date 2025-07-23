---
tags:
  - spec
  - supplier
  - rake-task
  - parmanentnote
---
# SUPPLIER by RENOSY Rakeタスク分析

## 概要
このドキュメントは、[SUPPLIER by RENOSY]]プロジェクトの`lib/tasks`ディレクトリ配下に定義されているRakeタスクの分析結果です。

## 定期バッチ処理タスク

| タスク名 | 定義場所 | タスクの目的・説明 | 想定される実行タイミング | 主要な処理内容の概要 |
|---------|---------|------------------|----------------------|-------------------|
| `periodic_batch:eager_load` | `lib/tasks/periodic_batch.rake:6` | Railsアプリケーションのeager loading実行 | 他の定期バッチタスクの前処理として | `Rails.application.eager_load!`を実行 |
| `periodic_batch:flow_update_payment_requests` | `lib/tasks/periodic_batch.rake:10` | [仕入手付支払申請]]の[[FLOW]]との連携 | 毎日定期実行 | `PaymentRequest.bulk_synchronize_with_flow`で決済情報を同期 |
| `periodic_batch:bulk_import_room_plan` | `lib/tasks/periodic_batch.rake:14` | [[AI抽出]]の間取り図を[Supplier]]の[[S3]]に保存 | 毎日定期実行 | `ArticleItem.bulk_import_room_plan!`で間取り図を一括インポート |
| `periodic_batch:bulk_import_files_from_flow` | `lib/tasks/periodic_batch.rake:18` | [[FLOW]]からの決済明細書吸い上げ | 毎日定期実行 | `ArticleItem.bulk_import_from_flow!`で決済書類を一括インポート |
| `periodic_batch:rewrite_tech_building_id` | `lib/tasks/periodic_batch.rake:22` | 重複建物の[[TechBuildingId]]洗い替え | 手動でのデータ移行時 | `Tasks::RewriteTechBuildingId.new.execute`で建物IDを更新 |
| `periodic_batch:import_supplier_mails` | `lib/tasks/periodic_batch.rake:26` | 仲介メール取り込み | 毎日定期実行 | `Tasks::MailReciever.execute`でGmailからメールを取得・処理 |
| `periodic_batch:article_data_sync_to_Shinkyobyousan` | `lib/tasks/periodic_batch.rake:30` | [[神居秒算]]への物件データの連携 | 毎日定期実行 | `Tasks::ShinkyobyousanCsvUploader.execute`でCSVデータをアップロード |
| `periodic_batch:notify_bring_back_contract_files_unchecked_articles` | `lib/tasks/periodic_batch.rake:34` | [[OWNR]]アプリ連携すべき物件の[[Slack]]通知 | 毎日定期実行 | `Notifiers::OwnrBringBackContractFiles.execute`で通知送信 |
| `periodic_batch:notify_valuation_certificate_required_articles` | `lib/tasks/periodic_batch.rake:38` | [[評価証明書]]登録すべき物件の[[Slack]]通知 | 毎日定期実行 | `Notifiers::ValuationCertificateRequiredArticles.execute`で通知送信 |
| `periodic_batch:activate_reserved_articles_certified_copy_uploader` | `lib/tasks/periodic_batch.rake:42` | [[留保物件]]の[[謄本]]取得 | 毎日定期実行 | `Tasks::ReservedArticles::CertifiedCopyUploader.execute`で謄本取得処理 |

## API開発支援タスク

| タスク名 | 定義場所 | タスクの目的・説明 | 想定される実行タイミング | 主要な処理内容の概要 |
|---------|---------|------------------|----------------------|-------------------|
| `api:generate[name]` | `lib/tasks/api.rake:5` | [[API]]の雛形を作成 | 新規API開発時 | コントローラー、レスポンス属性、検索パラメータ、テストファイルを自動生成 |

## 個別処理タスク

| タスク名 | 定義場所 | タスクの目的・説明 | 想定される実行タイミング | 主要な処理内容の概要 |
|---------|---------|------------------|----------------------|-------------------|
| `Tasks::MailReciever.execute` | `lib/tasks/mail_reciever.rb:25` | Gmailからのメール取得・処理 | 定期バッチから呼び出し | Gmail APIを使用してメールを取得し、添付ファイルを[[S3]]にアップロード |
| `Tasks::RewriteTechBuildingId.new.execute` | `lib/tasks/rewrite_tech_building_id.rb:6` | 重複建物の[[TechBuildingId]]更新 | 手動実行 | マージされた建物のIDを最新のIDに更新 |
| `Tasks::ShinkyobyousanCsvUploader.execute` | `lib/tasks/shinkyobyousan_csv_uploader.rb:32` | [[神居秒算]]へのデータ連携 | 定期バッチから呼び出し | 物件データと画像URLをCSV形式で[[S3]]にアップロード |
| `Tasks::BulkInsertManagementArticles.execute` | `lib/tasks/bulk_insert_management_articles.rb:6` | 交渉物件のサンプルデータ一括挿入 | 開発・テスト環境でのみ実行 | 50万件のサンプル交渉物件データを一括作成 |
| `Tasks::ReservedArticles::CertifiedCopyUploader.execute` | `lib/tasks/reserved_articles/certified_copy_uploader.rb:6` | [[留保物件]]の謄本取得処理 | 定期バッチから呼び出し | [[FLOW]]から留保物件IDを取得し、謄本取得APIを実行 |

## 主要な処理フロー

### メール処理フロー
1. `periodic_batch:import_supplier_mails` → `Tasks::MailReciever.execute`
2. Gmailからメールを取得
3. 添付ファイルを[[S3]]にアップロード
4. 物件情報をデータベースに保存

### 外部システム連携フロー
1. `periodic_batch:article_data_sync_to_Shinkyobyousan` → `Tasks::ShinkyobyousanCsvUploader.execute`
2. 開中の物件データを抽出
3. CSV形式で[[S3]]にアップロード
4. [[神居秒算]]システムで利用

### 決済連携フロー
1. `periodic_batch:flow_update_payment_requests`
2. [[FLOW]]システムと決済情報を同期
3. 手付支払申請の状態を更新

## 関連リンク
- [[SUPPLIER by RENOSY]]
- [[FLOW]]
- [[S3]]
- [[Gmail API]]
- [[神居秒算]]
- [[OWNR]]
- [[Slack]]
- [[謄本]]
- [[評価証明書]]
- [[TechBuildingId]]
- [[留保物件]] 


```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}
```