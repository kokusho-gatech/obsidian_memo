---
tags:
  - 定義
  - http
  - 技術
  - web開発
  - 通信プロトコル
---

# Streamable HTTP

> **関連タグ:** #通信プロトコル #HTTP #MCP #リアルタイム通信

## 概要

Streamable HTTPは、HTTPプロトコルを拡張した通信方式で、リアルタイムなデータストリーミングを可能にする技術です。従来のHTTPのリクエスト-レスポンスモデルを超えて、継続的なデータ送信を実現します。

## 特徴

### 従来のHTTPとの違い
- **従来のHTTP**: リクエスト-レスポンスの1回限りの通信
- **Streamable HTTP**: 継続的なデータストリーミングが可能

### 主な用途
- リアルタイムデータ配信
- チャットアプリケーション
- ライブストリーミング
- MCP（Model Context Protocol）でのリモート通信

## MCPでの活用

MCPサーバーでは、以下の通信方式が使用されています：

1. **ローカルMCPサーバー**: 標準入出力
2. **リモートMCPサーバー**: HTTP、SSE、Streamable HTTP

### Streamable HTTPの利点
- クラウド上での運用が可能
- Webアプリやスマートフォンなど、様々な環境からアクセス可能
- リアルタイムなレスポンス配信

## 技術的詳細

### 実装方式
- HTTP/1.1のチャンク転送エンコーディングを活用
- 長時間接続（Keep-Alive）を維持
- ストリーミングデータの効率的な配信

### 対応プラットフォーム
- Cloudflare
- AWS Lambda
- その他のクラウドサービス

## 関連技術

- [[SSE]] (Server-Sent Events)
- WebSocket
- HTTP/2 Server Push
- MCP (Model Context Protocol)

## 参考資料

- [[やさしいMCP入門]]
- [[MCPサーバー自作入門]]
- [[For Server Developers]]

## メモ

- 2025-07-23: 査定自動化プロジェクトでMCPサーバーの通信方式として学習が必要
- リアルタイム通信の実装方法として注目されている技術 