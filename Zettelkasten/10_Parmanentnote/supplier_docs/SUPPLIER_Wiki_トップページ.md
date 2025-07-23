---
tags:
  - spec
  - supplier
  - wiki
  - navigation
  - parmanentnote
---
# SUPPLIER by RENOSY システム仕様Wiki

> **SUPPLIER by RENOSY**は、不動産の仕入れ業務を効率化・高度化するための業務システムです。このWikiでは、システムの技術仕様、アーキテクチャ、機能詳細を体系的に整理しています。

---

## 📚 システム概要・アーキテクチャ

### 基本情報
- **[[00_SUPPLIER_全体概要]]** - プロジェクト概要、技術スタック、規模感
- **[[01_SUPPLIER_設定_セキュリティ_インフラ]]** - セキュリティ・インフラ設定の詳細分析
- **[[02_SUPPLIER_バックグラウンドジョブ]]** - 非同期処理・ジョブ管理の仕組み

### 技術ガイド
- **[[Ruby on Rails 探検ガイド]]** - Railsアプリケーションの探検方法

---

## 🏗️ システム構成

### フロントエンド・ページ構成
- **[[03_SUPPLIER_主要ページ一覧]]** - 主要画面・機能ページのURLパス一覧

### バックエンド・コントローラー構成
- **[[04_SUPPLIER_コントローラー一覧]]** - 主要コントローラーの一覧と詳細解説

### データベース・インフラ
- **[[05_SUPPLIER_DB構造]]** - データベース設計・テーブル構造
- **[[06_SUPPLIER_Rakeタスク]]** - 管理用タスク・バッチ処理
- **[[07_SUPPLIER_テスト構成]]** - テスト戦略・構成

---

## 🔍 プロダクトドキュメントの歩き方

- **[[プロダクトドキュメントの歩き方]]** - このWikiの使い方・ナビゲーション方法

---

## 📖 用語集・定義

### 技術用語
- **[[ActiveJob]]** - Railsのバックグラウンドジョブフレームワーク
- **[[API]]** - アプリケーションプログラミングインターフェース
- **[[APIエンドポイント]]** - APIの接続点
- **[[AWS S3]]** - Amazon Simple Storage Service
- **[[AWS Secrets Manager]]** - AWSの機密情報管理サービス
- **[[CloudFront]]** - AWSのCDNサービス
- **[[Datadog]]** - 監視・分析プラットフォーム
- **[[devise]]** - Rails認証フレームワーク
- **[[DocuSign]]** - 電子署名サービス
- **[[HSTS]]** - HTTP Strict Transport Security
- **[[kaminari]]** - ページネーションgem
- **[[lograge]]** - 構造化ログgem
- **[[OCR]]** - 光学文字認識
- **[[omniauth-google-oauth2]]** - Google OAuth2認証
- **[[paper_trail]]** - データ変更履歴管理
- **[[PostgreSQL]]** - リレーショナルデータベース
- **[[Puma]]** - Ruby Webサーバー
- **[[PumaWorkerKiller]]** - Pumaのメモリ管理
- **[[ransack]]** - 検索・絞り込みgem
- **[[Redis]]** - インメモリデータストア
- **[[Rollbar]]** - エラー監視サービス
- **[[Ruby on Rails]]** - Webアプリケーションフレームワーク
- **[[sidekiq]]** - バックグラウンドジョブキュー
- **[[Slack]]** - チームコミュニケーションツール
- **[[SSL]]** - Secure Sockets Layer
- **[[view_component]]** - UIコンポーネントgem

### ビジネス用語
- **[[Approval]]** - 承認
- **[[ApprovalDetail]]** - 承認詳細
- **[[ApprovalStatusHistory]]** - 承認ステータス履歴
- **[[ApprovalStatusHistoryComment]]** - 承認ステータス履歴コメント
- **[[Article]]** - 物件
- **[[ArticleDetailPage]]** - 物件詳細ページ
- **[[ArticleInputsPage]]** - 物件入力ページ
- **[[ArticleItem]]** - 物件資料項目
- **[[ArticleItemsPage]]** - 物件資料ページ
- **[[ArticlesPage]]** - 物件一覧ページ
- **[[AssessmentEditPage]]** - 査定編集ページ
- **[[AssessmentNgPage]]** - 査定NGページ
- **[[AssessmentPage]]** - 査定ページ
- **[[Attachment]]** - 添付ファイル
- **[[Building]]** - 建物
- **[[BuildingConfirmation]]** - 建物確認
- **[[BuildingConfirmationsPage]]** - 建物確認ページ
- **[[BuildingInformationEditPage]]** - 建物情報編集ページ
- **[[BusinessPartner]]** - ビジネスパートナー
- **[[CatalogEditPage]]** - カタログ編集ページ
- **[[CertifiedCopyEditPage]]** - 謄本編集ページ
- **[[Comment]]** - コメント
- **[[CompensationPaymentAgreementEditPage]]** - 補償金支払い契約編集ページ
- **[[ConsultingOutsourcingAgreementEditPage]]** - コンサルティング委託契約編集ページ
- **[[ConsumptionTaxVersion]]** - 消費税バージョン
- **[[ConsumptionTaxVersionsNewPage]]** - 消費税計算新規作成ページ
- **[[ContractController]]** - 契約コントローラー
- **[[DeletedArticlesPage]]** - 削除済み物件ページ
- **[[DocusignFile]]** - DocuSignファイル
- **[[ForSaleMaisokuEditPage]]** - 販売用マイソク編集ページ
- **[[ForSimulationEditPage]]** - シミュレーション編集ページ
- **[[IntermediaryCompany]]** - 仲介会社
- **[[IntermediaryCompaniesPage]]** - 仲介会社ページ
- **[[IntermediaryDomain]]** - 仲介ドメイン
- **[[IntermediaryStaff]]** - 仲介スタッフ
- **[[IntermediaryStaffUser]]** - 仲介スタッフユーザー
- **[[Item]]** - 項目
- **[[Janitor]]** - 管理人
- **[[Jikoshintaku]]** - 自己新宅
- **[[JikoshintakuArticle]]** - 自己新宅物件
- **[[Label]]** - ラベル
- **[[LatestApprovalEditPage]]** - 最新承認編集ページ
- **[[LatestApprovalsPage]]** - 最新承認ページ
- **[[LatestSaleApprovalEditPage]]** - 最新販売承認編集ページ
- **[[LatestSaleApprovalsPage]]** - 最新販売承認ページ
- **[[ManagementForApprovalEditPage]]** - 承認用管理編集ページ
- **[[ManagementForPaymentRequestEditPage]]** - 支払い請求用管理編集ページ
- **[[ManagementPage]]** - 管理ページ
- **[[NegotiationHistory]]** - 交渉履歴
- **[[OwnrInfo]]** - 所有者情報
- **[[PamphletEditPage]]** - パンフレット編集ページ
- **[[PaymentRequest]]** - 支払い請求
- **[[PaymentRequestComment]]** - 支払い請求コメント
- **[[Prefecture]]** - 都道府県
- **[[PricePrediction]]** - 価格予測
- **[[PriorValuation]]** - 事前評価
- **[[PriorValuationEditPage]]** - 事前評価編集ページ
- **[[PriorValuationResult]]** - 事前評価結果
- **[[PriorValuationsPage]]** - 事前評価ページ
- **[[PurchaseContractsPage]]** - 仕入契約ページ
- **[[ReplaceMaisokuForSbjJob]]** - SBJ用マイソク生成ジョブ
- **[[ReportOfImportantInfoSurveyEditPage]]** - 重要情報調査報告編集ページ
- **[[ReuploadDocusignFilesJob]]** - DocuSignファイル再アップロードジョブ
- **[[SaleApproval]]** - 販売承認
- **[[SaleApproval::Detail]]** - 販売承認詳細
- **[[SaleApproval::StatusHistory]]** - 販売承認ステータス履歴
- **[[SaleApproval::StatusHistory::Comment]]** - 販売承認ステータス履歴コメント
- **[[SaleManagementInfo]]** - 販売管理情報
- **[[SaleManagementInfosPage]]** - 販売管理情報ページ
- **[[SalesAgreementAbEditPage]]** - 販売契約AB編集ページ
- **[[SalesAgreementOnPurchaseEditPage]]** - 購入時販売契約編集ページ
- **[[SalesAgreementSetPage]]** - 販売契約セットページ
- **[[SalesContractField]]** - 販売契約フィールド
- **[[SalesContractFile]]** - 販売契約ファイル
- **[[SalesContractTemplate]]** - 販売契約テンプレート
- **[[SalesContractTemplatesPage]]** - 販売契約テンプレートページ
- **[[SalesDestination]]** - 販売先
- **[[SalesDestinationArticle]]** - 販売先物件
- **[[SalesInfo]]** - 販売情報
- **[[SalesPropertiesSheetField]]** - 販売物件シートフィールド
- **[[SoldDocumentsPage]]** - 販売済み書類ページ
- **[[SupplierMail]]** - サプライヤーメール
- **[[TenantLeaseAgreementEditPage]]** - 賃貸借契約編集ページ
- **[[UnassociatedPage]]** - 未関連ページ
- **[[UpdateArticleWithMaisokuReaderJob]]** - マイソク読み取りジョブ
- **[[UpdateModelsWithCertifiedCopyReaderJob]]** - 謄本読み取りジョブ
- **[[User]]** - ユーザー
- **[[UsersPage]]** - ユーザーページ
- **[[UsersPages]]** - ユーザーページ群
- **[[Valuation]]** - 評価
- **[[ValuationCertificateEditPage]]** - 評価証明書編集ページ
- **[[ValuationHistory]]** - 評価履歴
- **[[ValuationHistoriesEditPage]]** - 評価履歴編集ページ

### 日本語用語
- **[[交渉]]** - 物件の交渉プロセス
- **[[交渉詳細（コントラクト用）]]** - コントラクト用交渉詳細
- **[[交渉詳細（バイヤー用）]]** - バイヤー用交渉詳細
- **[[仕入契約一覧]]** - 仕入契約の一覧表示
- **[[仲介会社]]** - 不動産仲介会社
- **[[仲介会社一覧]]** - 仲介会社の一覧表示
- **[[仲介会社管理]]** - 仲介会社の管理機能
- **[[契約]]** - 不動産取引契約
- **[[契約管理]]** - 契約の管理機能
- **[[履歴管理]]** - データ変更履歴の管理
- **[[書類]]** - 不動産取引関連書類
- **[[書類管理]]** - 書類の管理機能
- **[[査定]]** - 物件の査定プロセス
- **[[査定編集]]** - 査定情報の編集
- **[[物件]]** - 不動産物件
- **[[物件管理]]** - 物件の管理機能
- **[[発表詳細]]** - 物件発表の詳細情報
- **[[認可]]** - システム利用の認可
- **[[認証]]** - ユーザー認証
- **[[通知]]** - システム通知機能
- **[[進捗]]** - 業務進捗の管理

---

## 🚀 クイックスタート

### 新規参入者向け
1. **[[00_SUPPLIER_全体概要]]** でシステムの全体像を把握
2. **[[プロダクトドキュメントの歩き方]]** でWikiの使い方を学習
3. **[[03_SUPPLIER_主要ページ一覧]]** で主要機能を確認

### 開発者向け
1. **[[01_SUPPLIER_設定_セキュリティ_インフラ]]** でインフラ構成を理解
2. **[[04_SUPPLIER_コントローラー一覧]]** でバックエンド構造を把握
3. **[[05_SUPPLIER_DB構造]]** でデータベース設計を確認

### 運用者向け
1. **[[02_SUPPLIER_バックグラウンドジョブ]]** で非同期処理を理解
2. **[[06_SUPPLIER_Rakeタスク]]** で管理タスクを確認
3. **[[07_SUPPLIER_テスト構成]]** でテスト戦略を把握

---

## 📝 最近の更新

```dataviewjs
dv.header(3, "最近更新されたドキュメント");
dv.list(dv.pages("#spec AND #supplier").sort(f => f.file.mtime.ts, "desc").limit(10).file.link);
```

---

## 🔗 関連リンク

- **[[SUPPLIER by RENOSY]]** - プロダクト概要
- **[[Ruby on Rails 探検ガイド]]** - Railsアプリケーションの探検方法

---

*このWikiは継続的に更新されています。新しい情報や改善提案があれば、お気軽にお知らせください。* 