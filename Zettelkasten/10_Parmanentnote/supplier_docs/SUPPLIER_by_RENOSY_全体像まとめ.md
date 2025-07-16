# SUPPLIER by RENOSY プロジェクト概要

## 1. プロジェクト概要

このアプリケーションは、不動産の仕入れ業務を効率化・高度化するための業務システムです。  
主に「物件の査定」「交渉」「契約」「書類管理」「仲介会社・スタッフ管理」など、不動産仕入れに関わる一連の業務をWeb上で一元管理できるように設計されています。  
これにより、煩雑な書類作業や情報の分散、進捗の見える化といった課題を解決し、業務の効率化・品質向上を実現します。

---

## 2. 主要な技術スタック（Gem）

Gemfileから、特に重要と思われるGemをピックアップし、役割を平易に解説します。

| Gem名 | 役割・説明 |
|-------|------------|
| devise | ログイン・ユーザー認証の専門家。安全なログイン機能を提供します。 |
| sidekiq | 時間のかかる処理（例：メール送信やバッチ処理）を裏側で自動実行してくれる働き者。 |
| kaminari | 一覧画面のページ送り（ページネーション）を簡単に実装できる便利屋。 |
| paper_trail | データの変更履歴を自動で記録してくれる監査役。 |
| aws-sdk-s3 | ファイルの保存や配信をAmazon S3で行うための橋渡し役。 |
| cloudinary | 画像やPDFなどのファイルをクラウドで管理・配信するためのサービス連携。 |
| ransack | 検索・絞り込み機能を簡単に作れる検索エンジン。 |
| omniauth-google-oauth2 | Googleアカウントでのログインを実現する連携担当。 |
| lograge | アクセスログを見やすく整理してくれる記録係。 |
| view_component | UI部品を部品化して再利用しやすくする設計サポーター。 |

---

## 3. プロジェクトの規模感

- **モデル（app/models）**  
  50以上のファイル＋多数のサブディレクトリ（例：user, article, contract, sales, payment等）。  
  → 物件、契約、ユーザー、書類、進捗、仲介会社など多岐にわたる業務データを管理。

- **コントローラー（app/controllers）**  
  30以上のファイル＋サブディレクトリ（articles, intermediary_companies, users, api等）。  
  → 物件管理、契約管理、ユーザー管理、仲介会社管理、APIなど多機能。

- **サービスクラス（app/services）**  
  ※`app/services`ディレクトリは存在しませんでした。  
  代わりにモデルやコントローラーの肥大化を避けるため、`app/models`配下のサブディレクトリや`lib/`などにロジックを分散している可能性があります。

---

## 4. 主要なルーティング（URLと担当コントローラー/アクション）

routes.rbから、主な機能と担当コントローラーを抜粋して表にまとめます。

| URL例 | 機能概要 | コントローラー#アクション |
|-------|----------|--------------------------|
| /articles/assessment | 査定一覧 | articles/assessment#index |
| /articles/assessment_ng | 査定NG一覧 | articles/assessment_ng#index |
| /articles/unassociated | 仲介担当なし一覧 | articles/unassociated#index |
| /articles/:id/edit | 査定編集 | articles/assessment#edit |
| /articles/management | 交渉一覧 | articles/management#index |
| /articles/:id/management/for_approval/edit | 交渉詳細（バイヤー用） | articles/management/for_approval#edit |
| /articles/:id/management/for_payment_request/edit | 交渉詳細（コントラクト用） | articles/management/for_payment_request#edit |
| /sale_management_infos | 発表管理一覧 | sale_management_infos#index |
| /articles/:id | 発表詳細 | articles#show |
| /intermediary_companies | 仲介会社一覧 | intermediary_companies#index |
| /users | ユーザー一覧 | users#index |
| /purchase_contracts | 仕入契約一覧 | purchase_contracts#index |
| /sidekiq | バックグラウンドジョブ管理 | Sidekiq::Web（管理画面） |

※他にも多数のルートがありますが、主要な業務機能に関わるものを抜粋しています。

---

## 備考

- モデル・コントローラーともにサブディレクトリが多く、業務ドメインごとに細かく分割されています。
- APIエンドポイントも多数用意されており、外部連携やフロントエンドとの通信も重視されています。
- 認証・認可、ファイル管理、通知、履歴管理など、業務システムとして必要な機能が一通り揃っています。 