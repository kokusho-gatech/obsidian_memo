---
tags:
  - spec
  - supplier
  - overview
  - guideline
  - rails
  - real-estate
  - architecture
---
# SUPPLIER by RENOSY プロジェクト概要

## 1. プロジェクト概要

このアプリケーションは、不動産の仕入れ業務を効率化・高度化するための業務システムです。  
主に「[[物件]]の[[査定]]」「[[交渉]]」「[[契約]]」「[[書類管理]]」「[[仲介会社]]・スタッフ管理」など、不動産仕入れに関わる一連の業務をWeb上で一元管理できるように設計されています。  
これにより、煩雑な書類作業や情報の分散、進捗の見える化といった課題を解決し、業務の効率化・品質向上を実現します。

---

## 2. 主要な技術スタック（Gem）

Gemfileから、特に重要と思われるGemをピックアップし、役割を平易に解説します。

| Gem名                       | 役割・説明                                    |
| -------------------------- | ---------------------------------------- |
| [[devise]]                 | ログイン・[[ユーザー認証]]の専門家。安全なログイン機能を提供します。     |
| [[sidekiq]]                | 時間のかかる処理（例：メール送信やバッチ処理）を裏側で自動実行してくれる働き者。 |
| [[kaminari]]               | 一覧画面のページ送り（ページネーション）を簡単に実装できる便利屋。        |
| [[paper_trail]]            | データの変更履歴を自動で記録してくれる監査役。                  |
| [[aws-sdk-s3]]             | ファイルの保存や配信を[[Amazon S3]]で行うための橋渡し役。      |
| [[cloudinary]]             | 画像やPDFなどのファイルをクラウドで管理・配信するためのサービス連携。     |
| [[ransack]]                | 検索・絞り込み機能を簡単に作れる検索エンジン。                  |
| [[omniauth-google-oauth2]] | [[Googleアカウント]]でのログインを実現する連携担当。          |
| [[lograge]]                | アクセスログを見やすく整理してくれる記録係。                   |
| [[view_component]]         | UI部品を部品化して再利用しやすくする設計サポーター。              |

---

## 3. プロジェクトの規模感

- **[[モデル]]（app/models）**  
  50以上のファイル＋多数のサブディレクトリ（例：user、article、contract、sales、payment等）。  
  → [[物件]]、[[契約]]、[[ユーザー]]、[[書類]]、[[進捗]]、[[仲介会社]]など多岐にわたる業務データを管理。

- **[[コントローラー]]（app/controllers）**  
  30以上のファイル＋サブディレクトリ（articles、intermediary_companies、users、api等）。  
  → [[物件管理]]、[[契約管理]]、[[ユーザー管理]]、[[仲介会社管理]]、[[API]]など多機能。

- **[[サービスクラス]]（app/services）**  
  ※`app/services`ディレクトリは存在しませんでした。  
  代わりに[[モデル]]や[[コントローラー]]の肥大化を避けるため、`app/models`配下のサブディレクトリや`lib/`などにロジックを分散している可能性があります。

---

## 4. 主要なルーティング（URLと担当コントローラー/アクション）

routes.rbから、主な機能と担当コントローラーを抜粋して表にまとめます。

| URL例                                              | 機能概要                                    | コントローラー#アクション                                |
| ------------------------------------------------- | --------------------------------------- | -------------------------------------------- |
| /articles/assessment                              | [[AssessmentPage]]                      | articles/assessment#index                    |
| /articles/assessment_ng                           | [[AssessmentNgPage]]                    | articles/assessment_ng#index                 |
| /articles/unassociated                            | [[UnassociatedPage]]                    | articles/unassociated#index                  |
| /articles/:id/edit                                | [[AssessmentPage]]                      | articles/assessment#edit                     |
| /articles/management                              | [[ManagementPage]]                      | articles/management#index                    |
| /articles/:id/management/for_approval/edit        | [[ManagementForApprovalEditPage]]       | articles/management/for_approval#edit        |
| /articles/:id/management/for_payment_request/edit | [[ManagementForPaymentRequestEditPage]] | articles/management/for_payment_request#edit |
| /sale_management_infos                            | [[SaleManagementInfosPage]]             | sale_management_infos#index                  |
| /articles/:id                                     | [[SaleManagementInfosPage]]             | articles#show                                |
| /intermediary_companies                           | [[IntermediaryCompaniesPage]]           | intermediary_companies#index                 |
| /users                                            | [[UsersPage]]                           | users#index                                  |
| /purchase_contracts                               | [[PurchaseContractsPage]]               | purchase_contracts#index                     |
| /sidekiq                                          | [[sidekiq]]                             | Sidekiq::Web（管理画面）                           |
|                                                   |                                         |                                              |

※他にも多数のルートがありますが、主要な業務機能に関わるものを抜粋しています。

---

## 備考

- [[モデル]]・[[コントローラー]]ともにサブディレクトリが多く、業務ドメインごとに細かく分割されています。
- [[APIエンドポイント]]も多数用意されており、外部連携やフロントエンドとの通信も重視されています。
- [[認証]]・[[認可]]、[[ファイル管理]]、[[通知]]、[[履歴管理]]など、業務システムとして必要な機能が一通り揃っています。 

```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}
```