---
tags:
  - spec
  - supplier
  - rails
  - glossary
  - parmanentnote
---
# Rails技術用語集

SUPPLIER by RENOSYで使用されているRails関連の技術用語集です。開発者が理解しておくべき技術用語を網羅的に解説しています。

---

## 🏗️ Railsフレームワーク

### 基本概念
- **[[Ruby on Rails]]** - Ruby on Railsフレームワーク
- **[[Rails]]** - Railsの基本概念
- **[[コントローラー]]** - Railsコントローラーの概念
- **[[モデル]]** - Railsモデルの概念
- **[[ビュー]]** - Railsビューの概念

### MVCアーキテクチャ
- **[[コントローラー]]** - コントローラーの役割と実装
- **[[モデル]]** - モデルの役割と実装
- **[[ビュー]]** - ビューの役割と実装

---

## 🔐 認証・認可

### 認証フレームワーク
- **[[devise]]** - Devise認証フレームワーク
- **[[omniauth-google-oauth2]]** - Google OAuth2認証
- **[[認証]]** - 認証システムの概要
- **[[認可]]** - 権限管理・アクセス制御

### セッション管理
- **[[devise]]** - Deviseセッション管理
- **[[認証]]** - 認証セッション管理

---

## 🗄️ データベース

### データベースエンジン
- **[[PostgreSQL]]** - PostgreSQLデータベースエンジン
- **[[DB]]** - データベースの基本概念

### ORM・クエリ
- **[[ActiveRecord]]** - ActiveRecord ORM
- **[[ransack]]** - Ransack検索gem
- **[[kaminari]]** - Kaminariページネーションgem

---

## ⚙️ バックグラウンド処理

### ジョブフレームワーク
- **[[ActiveJob]]** - Railsのバックグラウンドジョブフレームワーク
- **[[ApplicationJob]]** - 基底ジョブクラス
- **[[sidekiq]]** - Sidekiq非同期処理エンジン

### ジョブ管理
- **[[バックグラウンドジョブ管理]]** - バックグラウンドジョブ管理の全体像

---

## 🗄️ キャッシュ・セッション

### キャッシュシステム
- **[[Redis]]** - Redisキャッシュ・セッションストア
- **[[キャッシュ・セッション管理]]** - キャッシュ・セッション管理の全体像

### セッション管理
- **[[devise]]** - Deviseセッション管理
- **[[Redis]]** - Redisセッションストア

---

## 📊 監視・ログ

### ログ管理
- **[[lograge]]** - 構造化ログ管理
- **[[監視・ログシステム]]** - 監視・ログシステムの全体像

### エラー監視
- **[[Rollbar]]** - Rollbarエラー監視サービス

---

## 🔧 開発・運用ツール

### 開発ツール
- **[[view_component]]** - ViewComponent gem
- **[[paper_trail]]** - PaperTrail履歴管理gem

### 運用ツール
- **[[Janitor]]** - システム監視・メンテナンス
- **[[Puma]]** - Puma Webサーバー
- **[[PumaWorkerKiller]]** - Pumaワーカーキラー

---

## ☁️ クラウド・インフラ

### AWSサービス
- **[[AWS S3]]** - Amazon S3ファイルストレージ
- **[[aws-sdk-s3]]** - AWS S3 SDK
- **[[AWS Secrets Manager]]** - AWS Secrets Manager
- **[[CloudFront]]** - AWS CloudFront CDN

### 外部サービス
- **[[cloudinary]]** - Cloudinaryファイル管理サービス
- **[[Datadog]]** - Datadog監視サービス

---

## 📄 ファイル・ドキュメント

### ファイル管理
- **[[ファイル管理]]** - ファイル管理システムの全体像
- **[[Attachment]]** - 添付ファイル管理

### ドキュメント処理
- **[[OCR]]** - 光学文字認識技術
- **[[DocuSign]]** - 電子署名サービス
- **[[DocusignFile]]** - DocuSignファイル管理

---

## 🔗 API・通信

### API設計
- **[[API]]** - APIの基本概念と定義
- **[[APIエンドポイント]]** - APIエンドポイントの概要

### 通信プロトコル
- **[[SSE]]** - Server-Sent Events
- **[[Streamable HTTP]]** - ストリーミングHTTP

---

## 🛠️ 開発環境・ツール

### 開発環境
- **[[uv]]** - uv Pythonパッケージマネージャー

### テスト・品質
- **[[テスト]]** - テストの基本概念
- **[[品質管理]]** - 品質管理の基本概念

---

## 📋 ビジネスロジック

### 業務概念
- **[[サービスクラス]]** - サービスクラスの概念
- **[[バックグラウンドジョブ管理]]** - バックグラウンドジョブ管理

### データ管理
- **[[履歴管理]]** - 履歴管理システムの全体像
- **[[進捗]]** - 進捗管理の概念

---

## 🔐 セキュリティ

### セキュリティ技術
- **[[SSL]]** - SSL/TLS暗号化
- **[[HSTS]]** - HTTP Strict Transport Security

### セキュリティ管理
- **[[認証]]** - 認証システムの概要
- **[[認可]]** - 権限管理・アクセス制御

---

## 📊 パフォーマンス・最適化

### パフォーマンス技術
- **[[キャッシュ・セッション管理]]** - キャッシュ・セッション管理の全体像
- **[[Redis]]** - Redisキャッシュ・セッションストア

### 最適化技術
- **[[lograge]]** - 構造化ログ管理
- **[[PumaWorkerKiller]]** - Pumaワーカーキラー

---

## 🔄 外部連携

### 外部サービス
- **[[Slack]]** - Slack通知サービス
- **[[SupplierMail]]** - システムメール機能
- **[[SupplierMailsController]]** - システムメール管理

### 連携技術
- **[[API]]** - APIの基本概念と定義
- **[[APIエンドポイント]]** - APIエンドポイントの概要

---

*この技術用語集は、SUPPLIER by RENOSYの開発者が理解しておくべき技術用語を網羅的に解説しています。新しい技術や用語が追加された場合は、随時更新しています。*

```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}
``` 