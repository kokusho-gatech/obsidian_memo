---
tags:
  - spec
  - supplier
  - background-job
  - rails
  - automation
  - architecture
---
# SUPPLIER by RENOSY バックグラウンドジョブ分析

このドキュメントは、SUPPLIER by RENOSYプロジェクトの `app/jobs` ディレクトリに存在するバックグラウンド処理の一覧と詳細分析です。

## 概要

SUPPLIER by RENOSYは不動産仕入れのためのプロダクトで、以下の5つのバックグラウンドジョブが実装されています：

1. [[UpdateModelsWithCertifiedCopyReaderJob]] - 謄本の自動読み取り処理
2. [[ReplaceMaisokuForSbjJob]] - SBJ用マイソク生成処理
3. [[ReuploadDocusignFilesJob]] - DocuSignファイル再アップロード処理
4. [[UpdateArticleWithMaisokuReaderJob]] - マイソク自動読み取り処理
5. [[ApplicationJob]] - 基底ジョブクラス

これらのジョブは主に[[ArticleItemsPage]]でのファイルアップロードや、[[AssessmentPage]]・[[ManagementPage]]での物件情報更新時に実行されます。

---

## ジョブ詳細分析

- [[UpdateModelsWithCertifiedCopyReaderJob]]
- [[ReplaceMaisokuForSbjJob]]
- [[ReuploadDocusignFilesJob]]
- [[UpdateArticleWithMaisokuReaderJob]]
- [[ApplicationJob]]

---

## 技術的特徴

### キューの使用
- `ReplaceMaisokuForSbjJob` は専用キュー `sbj_maisoku_generator` を使用
- その他のジョブはデフォルトキューを使用

### エラーハンドリング
- すべてのジョブで例外処理が実装されている
- [[Rollbar]]を使用したエラー監視
- [[Slack]]通知による処理結果の可視化

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

### プロダクト・技術
- [[SUPPLIER by RENOSY]] - プロダクト概要
- [[ActiveJob]] - Railsのバックグラウンドジョブフレームワーク
- [[OCR]] - 光学文字認識技術
- [[DocuSign]] - 電子署名サービス
- [[TechConsul]] - 外部連携システム
- [[Slack]] - 通知システム
- [[Rollbar]] - エラー監視サービス
- [[SBJ]] - 不動産投資信託

### 関連ページ
- [[AssessmentPage]] - 査定一覧ページ
- [[ManagementPage]] - 交渉一覧ページ
- [[ArticleItemsPage]] - ファイルチェックページ

### 関連モデル
- [[Article]] - 物件情報モデル
- [[ArticleItem]] - 物件資料項目モデル
- [[Item]] - 書類種別マスタ 