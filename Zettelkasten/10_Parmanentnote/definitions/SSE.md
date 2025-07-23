# SSE (Server-Sent Events)

> **関連タグ:** #通信プロトコル #HTTP #リアルタイム通信 #WebAPI

## 概要

SSE（Server-Sent Events）は、Web標準の技術で、サーバーからクライアントへの一方向リアルタイム通信を実現するプロトコルです。HTTPプロトコルを基盤としており、WebSocketよりも軽量で実装が簡単です。

## 特徴

### 基本仕様
- **通信方向**: サーバーからクライアントへの一方向通信
- **プロトコル**: HTTP/HTTPS
- **データ形式**: テキストベース（UTF-8）
- **接続**: 長時間接続（Keep-Alive）

### WebSocketとの比較
| 項目 | SSE | WebSocket |
|------|-----|-----------|
| 通信方向 | 一方向（サーバー→クライアント） | 双方向 |
| プロトコル | HTTP | WebSocket |
| 実装の複雑さ | 簡単 | やや複雑 |
| ブラウザ対応 | 良好 | 良好 |

## 技術的詳細

### データ形式
```
data: メッセージ内容

data: 複数行の
data: メッセージ

event: カスタムイベント
data: イベントデータ

id: 12345
data: メッセージID付きデータ
```

### 主要なフィールド
- `data`: 実際のメッセージ内容
- `event`: イベントタイプ（カスタム定義可能）
- `id`: メッセージID（再接続時の復旧に使用）
- `retry`: 再接続間隔（ミリ秒）

## 実装例

### サーバーサイド（Node.js）
```javascript
app.get('/events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
  });

  const sendEvent = (data) => {
    res.write(`data: ${JSON.stringify(data)}\n\n`);
  };

  // 定期的にデータを送信
  const interval = setInterval(() => {
    sendEvent({ message: 'Hello from server', timestamp: Date.now() });
  }, 1000);

  req.on('close', () => {
    clearInterval(interval);
  });
});
```

### クライアントサイド（JavaScript）
```javascript
const eventSource = new EventSource('/events');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('受信:', data);
};

eventSource.onerror = (error) => {
  console.error('SSE接続エラー:', error);
  eventSource.close();
};
```

## MCPでの活用

MCP（Model Context Protocol）サーバーでは、以下の通信方式の一つとして使用されています：

1. **ローカルMCPサーバー**: 標準入出力
2. **リモートMCPサーバー**: HTTP、SSE、Streamable HTTP

### SSEの利点
- 実装が比較的簡単
- HTTPベースのため、既存のインフラで利用可能
- 自動再接続機能
- ブラウザネイティブサポート

## 使用場面

### 適している用途
- リアルタイム通知
- ライブチャット
- データ更新通知
- プログレス表示
- ログストリーミング

### 適していない用途
- 双方向通信が必要な場合
- 大量のデータ送信
- 低レイテンシーが重要な場合

## 関連技術

- [[Streamable HTTP]]
- WebSocket
- HTTP/2 Server Push
- MCP (Model Context Protocol)
- EventSource API

## 参考資料

- [[やさしいMCP入門]]
- [[MCPサーバー自作入門]]
- [[For Server Developers]]

## メモ

- 2025-07-23: 査定自動化プロジェクトでMCPサーバーの通信方式として学習が必要
- 一方向通信に特化した軽量なリアルタイム通信技術
- HTTPベースのため、既存のWebインフラとの親和性が高い 