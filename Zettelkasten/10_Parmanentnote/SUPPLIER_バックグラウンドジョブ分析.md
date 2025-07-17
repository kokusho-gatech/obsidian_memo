# SUPPLIER by RENOSY バックグラウンドジョブ分析

このドキュメントは、SUPPLIER by RENOSYプロジェクトの `app/jobs` ディレクトリに存在するバックグラウンド処理の一覧と詳細分析です。

## 概要

SUPPLIER by RENOSYは不動産仕入れのためのプロダクトで、以下の5つのバックグラウンドジョブが実装されています：1 [UpdateModelsWithCertifiedCopyReaderJob](#updatemodelswithcertifiedcopyreaderjob) - 謄本の自動読み取り処理
2ReplaceMaisokuForSbjJob](#replacemaisokuforsbjjob) - SBJ用マイソク生成処理3 [ReuploadDocusignFilesJob](#reuploaddocusignfilesjob) - DocuSignファイル再アップロード処理4[UpdateArticleWithMaisokuReaderJob](#updatearticlewithmaisokureaderjob) - マイソク自動読み取り処理
5[ApplicationJob](#applicationjob) - 基底ジョブクラス

---

## ジョブ詳細分析

### `UpdateModelsWithCertifiedCopyReaderJob` - (出典: `app/jobs/update_models_with_certified_copy_reader_job.rb:2`)

* **目的:** 謄本ファイルがアップロードされた際に、OCR技術を使用して自動的に謄本の内容を読み取り、物件情報や売買契約フィールド、入力謄本モデルを更新するための非同期処理

* **実行のトリガー:** 
  - 謄本ファイルのアップロード時に `perform_later` が呼び出される
  - トリガー箇所：
    - `app/controllers/concerns/api/article_item_file_actions.rb:18 - API経由での謄本アップロード時
    - `app/controllers/articles/article_items_controller.rb:35` - 管理画面での謄本更新時

* **主な処理内容:**
  1. アップロードされた謄本ファイルのURLを取得
2. ファイルがPDF形式であることを確認
  3 関連モデル（物件、売買契約フィールド、入力謄本）を取得
 4. 謄本読み取り可能な状態かチェック（売買契約フィールドが未作成かつ物件ステータスが契約・決済以外）
 5. `CertifiedCopy::ApiClient.read` を使用して謄本の内容を読み取り
  6各モデルに対して専用のアップデーターを使用してデータを更新
7. Slack通知を送信（物件URLと更新結果を含む）

* **扱うデータ:**
  - `Article` - 物件情報
  - `SalesContractField` - 売買契約フィールド
  - `InputCertifiedCopy` - 入力謄本データ
  - `ArticleItem` - 物件資料項目
  - `ArticleItemFile` - 物件資料ファイル

---

### `ReplaceMaisokuForSbjJob` - (出典: `app/jobs/replace_maisoku_for_sbj_job.rb:2`)

* **目的:** マイソク（図面）ファイルがアップロードされた際に、SBJ（不動産投資信託）用のマイソクを自動生成するための非同期処理

* **実行のトリガー:** 
  - マイソクファイルのアップロード完了時に `perform_later` が呼び出される
  - トリガー箇所：
    - `app/models/concerns/article_item_files/base.rb:46 - マイソクファイル作成後のコールバック

* **主な処理内容:**
 1 物件IDとユーザーIDを引数として受け取り
  2 物件とユーザーを取得
  3. `article.replace_maisoku_for_sale!` メソッドを呼び出してSBJ用マイソクを生成
  4ー発生時はログ出力とNotifier.reportでエラー通知

* **扱うデータ:**
  - `Article` - 物件情報
  - `User` - マイソク作成者
  - `ArticleItemFile` - マイソクファイル

---

### `ReuploadDocusignFilesJob` - (出典: `app/jobs/reupload_docusign_files_job.rb:4`)

* **目的:** DocuSignで作成された契約書ファイルを再アップロードし、TechConsulシステムに通知を送信するための非同期処理

* **実行のトリガー:** 
  - API経由でDocuSignファイルの再アップロードリクエストが送信された時に `perform_later` が呼び出される
  - トリガー箇所：
    - `app/controllers/api/articles_controller.rb:31` - `reupload_docusign_files` アクション実行時

* **主な処理内容:**
  1. 売買契約フィールドのステータスを `ready_contract` に更新
2 `Connectors::TechConsul` を使用してTechConsulシステムに通知を送信
  3. 成功・失敗に関わらず通知を送信
  4. エラー発生時はRollbarでエラーログを記録

* **扱うデータ:**
  - `SalesContractField` - 売買契約フィールド
  - `Connectors::TechConsul` - 外部システム連携

---

### `UpdateArticleWithMaisokuReaderJob` - (出典: `app/jobs/update_article_with_maisoku_reader_job.rb:2`)

* **目的:** マイソク（図面）ファイルがアップロードされた際に、OCR技術を使用して自動的にマイソクの内容を読み取り、物件情報を更新するための非同期処理

* **実行のトリガー:** 
  - 物件のマイソク読み取り準備が完了した時に `perform_later` が呼び出される
  - トリガー箇所：
    - `app/models/article.rb:1615` - `post_maisoku_reader` メソッド内

* **主な処理内容:**
 1. 物件モデルを取得
 2. マイソクのURLをログ出力
  3 `DocumentReader::Maisoku` を使用してマイソクの内容を読み取り
  4. 読み取り結果をログ出力
  5 `DocumentReader::Maisoku::ArticleUpdater` を使用して物件情報を更新
6. 更新失敗時はログ出力

* **扱うデータ:**
  - `Article` - 物件情報
  - `DocumentReader::Maisoku` - マイソク読み取りサービス

---

### `ApplicationJob` - (出典: `app/jobs/application_job.rb:3`)

* **目的:** すべてのバックグラウンドジョブの基底クラスとして、共通のログ機能とエラーハンドリングを提供する

* **実行のトリガー:** 直接実行されることはなく、他のジョブクラスが継承して使用

* **主な処理内容:**
  1. `around_perform` コールバックでログ機能を提供
  2. ジョブ開始時にログ出力
 3. ジョブ実行
  4. ジョブ完了時にログ出力
 5. エラー発生時はエラーログとバックトレースを出力

* **扱うデータ:** なし（基底クラス）

---

## 技術的特徴

### キューの使用
- `ReplaceMaisokuForSbjJob` は専用キュー `sbj_maisoku_generator` を使用
- その他のジョブはデフォルトキューを使用

### エラーハンドリング
- すべてのジョブで例外処理が実装されている
- Rollbarを使用したエラー監視
- Slack通知による処理結果の可視化

### 外部システム連携
- `CertifiedCopy::ApiClient` - 謄本読み取りAPI
- `DocumentReader::Maisoku` - マイソク読み取りサービス
- `Connectors::TechConsul` - TechConsulシステム連携
- `Slack::Bot` - Slack通知

### データ更新パターン
- 専用のアップデータークラスを使用した段階的なデータ更新
- トランザクション処理による整合性の保証

---

## 関連リンク

-SUPPLIER by RENOSY]] - プロダクト概要
- [[ActiveJob]] - Railsのバックグラウンドジョブフレームワーク
- OCR]] - 光学文字認識技術
-[DocuSign]] - 電子署名サービス
-TechConsul]] - 外部連携システム
- Slack]] - 通知システム
- [Rollbar]] - エラー監視サービス 