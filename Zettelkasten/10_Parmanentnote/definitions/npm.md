---
tags:
  - definition
  - programming
  - javascript
  - package-manager
creation-date: 2025-07-18
---

# npm

## 定義

npm（Node Package Manager）とは、JavaScriptのパッケージマネージャーで、Node.jsと共に配布される標準的なパッケージ管理ツールです。JavaScriptライブラリやツールのインストール、管理、共有を効率的に行うことができます。

## 主要機能

### パッケージ管理
- JavaScriptライブラリのインストール・更新・削除
- 依存関係の自動解決
- バージョン管理とセマンティックバージョニング

### プロジェクト管理
- `package.json`ファイルによるプロジェクト設定
- スクリプトの実行（`npm run`）
- 開発環境と本番環境の依存関係分離

### パッケージ公開
- npmレジストリへのパッケージ公開
- プライベートレジストリの利用
- スコープ付きパッケージの管理

## 基本コマンド

### プロジェクト初期化
```bash
npm init          # 対話的にpackage.jsonを作成
npm init -y       # デフォルト値でpackage.jsonを作成
```

### パッケージインストール
```bash
npm install <package-name>     # パッケージをインストール
npm install -D <package-name>  # 開発依存としてインストール
npm install -g <package-name>  # グローバルにインストール
```

### スクリプト実行
```bash
npm run <script-name>          # package.jsonのscriptsを実行
npm start                      # npm run startの省略形
npm test                       # npm run testの省略形
```

## TypeScriptとの関係

### TypeScriptプロジェクトでの使用
- TypeScriptコンパイラのインストール
- 型定義ファイル（@types）の管理
- ビルドプロセスの自動化

### 開発環境の構築
```bash
npm install -D typescript @types/node
npm install -D ts-node nodemon
```

## MCPサーバー開発での活用

### プロジェクトセットアップ
```bash
npm init -y
npm install @modelcontextprotocol/sdk
npm install -D @types/node typescript
```

### ビルドと実行
```bash
npm run build    # TypeScriptをJavaScriptにコンパイル
npm start        # サーバーを起動
```

## 設定ファイル

### package.json
```json
{
  "name": "project-name",
  "version": "1.0.0",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "ts-node src/index.ts"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/node": "^20.0.0"
  }
}
```

### package-lock.json
- 依存関係の正確なバージョンを記録
- 再現可能なビルドを保証
- セキュリティ監査の対象

## ベストプラクティス

### セキュリティ
- 定期的なセキュリティ監査（`npm audit`）
- 依存関係の更新
- 脆弱性のあるパッケージの特定と修正

### パフォーマンス
- 不要な依存関係の削除
- パッケージサイズの最適化
- キャッシュの活用

### チーム開発
- バージョン管理の統一
- 開発環境の標準化
- CI/CDパイプラインの構築

## 関連ツール

### 代替パッケージマネージャー
- **yarn**: Facebookが開発した高速なパッケージマネージャー
- **pnpm**: 効率的なディスク使用量を実現するパッケージマネージャー
- **bun**: 高速なJavaScriptランタイムとパッケージマネージャー

### 開発ツール
- **npx**: パッケージを一時的に実行
- **nvm**: Node.jsのバージョン管理
- **npm-check**: 依存関係の更新確認

## 引用元

- npm公式ドキュメント[^1]
- Node.js公式サイト[^2]
- TypeScript公式ハンドブック[^3]
- Model Context Protocol公式ドキュメント[^4]

[^1]: https://docs.npmjs.com/
[^2]: https://nodejs.org/
[^3]: https://www.typescriptlang.org/docs/
[^4]: https://modelcontextprotocol.io/ 