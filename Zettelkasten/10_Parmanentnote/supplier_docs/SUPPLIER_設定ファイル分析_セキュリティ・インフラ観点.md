# SUPPLIER by RENOSY 設定ファイル分析 - セキュリティ・インフラ観点

## 概要

このドキュメントは、SUPPLIER by RENOSYプロジェクトの設定ファイルを[[SRE]]（Site Reliability Engineer）の観点から分析し、セキュリティとインフラに関する重要な設定を整理したものです。

## アプリケーション基本設定

### config/application.rb:1-36*設定項目・内容の概要**
- [[Rails]] 70.1のデフォルト設定を読み込み
- タイムゾーンを東京に設定
- デフォルトロケールを日本語に設定
- ActiveJobのキューアダプターを[[Sidekiq]]に設定
- 外部キー制約の検証を無効化（テスト用）

**目的と影響範囲**
- アプリケーション全体の基本動作を定義
- 非同期処理の基盤となる[[Sidekiq]]の設定
- データベースの整合性チェックに影響

## 本番環境設定

### config/environments/production.rb:1-70*設定項目・内容の概要**
- [[SSL]]強制有効化（`config.force_ssl = true`）
- [[CloudFront]]アセット配信設定
- [[Redis]]キャッシュストア設定
- [[Lograge]]による構造化ログ設定
- ヘルスチェックエンドポイントのSSL除外設定

**目的と影響範囲**
- セキュリティ強化（HTTPS強制）
- CDN経由での静的ファイル配信
- パフォーマンス向上（キャッシュ）
- ログ監視・分析の基盤
- ヘルスチェックの可用性確保

### config/environments/production.rb:1516**設定項目・内容の概要**
```ruby
config.force_ssl = true
config.ssl_options = { redirect: { exclude: -> request[object Object] request.path =~ /health_check/ } } }
```

**目的と影響範囲**
- [[HSTS]]（HTTP Strict Transport Security）の実装
- ヘルスチェックエンドポイントのSSL除外
- セキュリティヘッダーの自動付与

### config/environments/production.rb:1920**設定項目・内容の概要**
```ruby
config.log_level = ENV.fetch(RAILS_LOG_LEVEL', info)
config.log_tags = %i[request_id]
```

**目的と影響範囲**
- ログレベルの環境変数制御
- リクエスト追跡のためのタグ付与
- 監視・デバッグの基盤

### config/environments/production.rb:22**設定項目・内容の概要**
```ruby
config.cache_store = :redis_cache_store, { url: ENV['REDIS_URL'] }
```

**目的と影響範囲**
- [[Redis]]による分散キャッシュ
- セッション管理・フラグメントキャッシュ
- スケーラビリティの向上

## 認証・セキュリティ設定

### config/initializers/devise.rb:175*設定項目・内容の概要**
- [[Devise]]認証フレームワークの設定
- パスワードハッシュ化（bcrypt、stretches:11）
- セッション管理設定
- CSRFトークン保護
- パスワードリセット機能

**目的と影響範囲**
- ユーザー認証システム全体
- セキュリティ（パスワード保護、CSRF対策）
- セッション管理の安全性

### config/initializers/devise.rb:1001**設定項目・内容の概要**
```ruby
config.stretches = Rails.env.test? ? 1 : 11nfig.reconfirmable = true
```

**目的と影響範囲**
- パスワードハッシュ化の強度設定
- メールアドレス変更時の再確認要求
- セキュリティ強化

### config/initializers/omniauth.rb:1-25*設定項目・内容の概要**
- [[Google OAuth2]]認証設定
- 環境変数からAPI認証情報を読み込み
- 開発環境でのモック認証設定

**目的と影響範囲**
- サードパーティ認証（Google）
- シングルサインオン（SSO）機能
- 開発効率の向上

### config/initializers/filter_parameter_logging.rb:1-4**設定項目・内容の概要**
```ruby
Rails.application.config.filter_parameters += [
  :passw, :secret, :token, :_key, :crypt, :salt, :certificate, :otp, :ssn
]
```

**目的と影響範囲**
- 機密情報のログ出力防止
- セキュリティ監査対応
- コンプライアンス要件の満足

## インフラ・パフォーマンス設定

### config/puma.rb:1-56*設定項目・内容の概要**
- [[Puma]]Webサーバーの設定
- ワーカー数・スレッド数の環境変数制御
- [[PumaWorkerKiller]]によるメモリ管理
- プリロード設定

**目的と影響範囲**
- Webサーバーのパフォーマンス
- メモリリーク対策
- スケーラビリティ

### config/puma.rb:8-9**設定項目・内容の概要**
```ruby
max_threads_count = ENV.fetch(RAILS_MAX_THREADS") { 5 }
min_threads_count = ENV.fetch(RAILS_MIN_THREADS") { max_threads_count }
```

**目的と影響範囲**
- 同時接続数の制御
- リソース使用量の最適化
- パフォーマンスチューニング

### config/puma.rb:4248**設定項目・内容の概要**
```ruby
before_fork do
  PumaWorkerKiller.config do |config|
    config.ram           = ENV.fetch(SERVICE_RAM') { 3750  config.frequency     = 10
    config.percent_usage = 00.7
  end
end
```

**目的と影響範囲**
- メモリ使用量の監視・制御
- ワーカープロセスの自動再起動
- システム安定性の向上

### config/initializers/sidekiq.rb:1-10*設定項目・内容の概要**
- [[Sidekiq]]の[[Redis]]接続設定
- リトライ回数の制限（最大1回）

**目的と影響範囲**
- 非同期処理の基盤
- ジョブキューの管理
- システムの信頼性

## 外部サービス連携

### config/initializers/carrierwave.rb:1-16*設定項目・内容の概要**
- [[AWS S3]]ファイルストレージ設定
- 環境変数から認証情報を読み込み
- ファイルアップロード機能

**目的と影響範囲**
- ファイルストレージ（画像・ドキュメント）
- スケーラブルなストレージ
- セキュリティ（認証情報管理）

### config/initializers/rollbar.rb:1-74*設定項目・内容の概要**
- [[Rollbar]]エラー監視設定
- 環境変数からアクセストークンを読み込み
- 機密情報のスクラビング設定

**目的と影響範囲**
- エラー監視・通知
- アプリケーションの安定性監視
- セキュリティ（機密情報保護）

### config/initializers/datadog.rb:1-22*設定項目・内容の概要**
- [[Datadog]]監視設定
- APM（Application Performance Monitoring）
- セキュリティ監視（AppSec）

**目的と影響範囲**
- パフォーマンス監視
- セキュリティ監視
- 運用監視の基盤

### config/initializers/slack.rb:1-4*設定項目・内容の概要**
- [[Slack]]通知設定
- 環境変数からAPIトークンを読み込み

**目的と影響範囲**
- アラート通知
- チーム連携
- 運用効率の向上

## データベース設定

### config/database.yml:1-22*設定項目・内容の概要**
- [[PostgreSQL]]（PostGIS拡張）設定
- 環境別の接続設定
- コネクションプール設定

**目的と影響範囲**
- 地理空間データの処理
- データベースパフォーマンス
- スケーラビリティ

### config/database.yml:4-5**設定項目・内容の概要**
```yaml
pool: <%= ENV.fetch(RAILS_MAX_THREADS") { 5 } %>
postgis_schema: supplier
```

**目的と影響範囲**
- データベース接続プールの最適化
- スキーマ分離による管理性向上
- パフォーマンスチューニング

## セッション管理

### config/initializers/session_store.rb:1-4**設定項目・内容の概要**
```ruby
Rails.application.config.session_store :cookie_store, key: _supplier_session'
```

**目的と影響範囲**
- セッション管理方式の定義
- セキュリティ（セッションキー）
- ユーザー状態管理

## 設定管理

### config/initializers/config.rb:1-50*設定項目・内容の概要**
- [[Settings]] gemによる設定管理
- 環境変数からの設定読み込み
- 設定値の検証機能

**目的と影響範囲**
- 設定の一元管理
- 環境別設定の制御
- 設定値の型安全性

### config/settings.yml:1-42
**設定項目・内容の概要**
- 会社情報・資格情報の設定
- 管理会社情報の設定
- プロダクト情報の設定

**目的と影響範囲**
- ビジネスロジックの設定
- 法的要件への対応
- システムの信頼性

## セキュリティリスクと対策

### 高リスク項目1. **認証情報の管理**
   - 環境変数による適切な管理
   - ログ出力時のフィルタリング
2. **SSL/TLS設定**
   - 強制SSL有効化
   - HSTSヘッダーの実装
3. **セッション管理**
   - セキュアなセッション設定
   - CSRF保護の実装

### 推奨対策
1 **環境変数の暗号化**
   - [[AWS Secrets Manager]]の活用
   - 認証情報のローテーション
2 **監視の強化**
   - [[Datadog]]による包括的監視
   - [[Rollbar]]によるエラー監視

3**セキュリティヘッダーの追加**
   - CSP（Content Security Policy）
   - X-Frame-Options
   - X-Content-Type-Options

## まとめ

SUPPLIER by RENOSYプロジェクトは、セキュリティとインフラの観点から適切な設定が行われています。特に以下の点が評価できます：

- 環境変数による機密情報管理
- SSL強制とセキュリティヘッダーの実装
- 包括的な監視体制の構築
- スケーラブルなアーキテクチャの採用

継続的な改善として、セキュリティヘッダーの追加や認証情報の暗号化強化を検討することを推奨します。 