---
tags:
  - definition
  - python
  - package-manager
  - development-tool
---

# uv

> **関連タグ:** #Python #パッケージ管理 #開発ツール #MCP

## 概要

uvは、Pythonの高速なパッケージマネージャーとプロジェクト管理ツールです。Rustで書かれており、pipやpoetryよりも大幅に高速で、依存関係の解決や仮想環境の管理を効率的に行えます。

## 特徴

### 主な利点
- **高速性**: Rustで実装されており、pipの10-100倍高速
- **依存関係解決**: 効率的なアルゴリズムによる高速な依存関係解決
- **仮想環境管理**: 自動的な仮想環境の作成と管理
- **プロジェクト管理**: プロジェクトの初期化から依存関係管理まで統合

### 従来ツールとの比較
| 機能 | uv | pip | poetry |
|------|----|-----|--------|
| 速度 | 非常に高速 | 標準 | やや遅い |
| 依存関係解決 | 高速 | 標準 | 高速 |
| 仮想環境管理 | 自動 | 手動 | 自動 |
| プロジェクト管理 | 統合 | なし | 統合 |

## インストール

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 基本的な使用方法

### プロジェクトの初期化
```bash
# 新しいプロジェクトを作成
uv init my-project
cd my-project

# 仮想環境を作成
uv venv

# 依存関係を追加
uv add requests
uv add "fastapi[all]"
```

### 依存関係の管理
```bash
# パッケージの追加
uv add package-name

# 開発依存関係の追加
uv add --dev pytest

# パッケージの削除
uv remove package-name

# 依存関係の更新
uv lock --upgrade
```

### スクリプトの実行
```bash
# 仮想環境内でスクリプトを実行
uv run script.py

# 特定のディレクトリで実行
uv run --directory /path/to/project script.py
```

## MCPでの活用

MCP（Model Context Protocol）サーバーの開発でuvが使用されています：

### プロジェクトセットアップ例
```bash
# MCPプロジェクトの初期化
uv init weather-mcp
cd weather-mcp

# 仮想環境作成
uv venv

# MCP関連パッケージの追加
uv add "mcp[cli]" httpx
```

### サーバー実行
```bash
# MCPサーバーの実行
uv run weather.py
```

## 設定ファイル

### pyproject.toml
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My Python project"
dependencies = [
    "requests>=2.28.0",
    "fastapi[all]>=0.100.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## 高度な機能

### 依存関係の解決
```bash
# 依存関係ツリーの表示
uv tree

# 依存関係の競合解決
uv lock --upgrade
```

### パフォーマンス最適化
- 並列ダウンロード
- キャッシュの活用
- 効率的なアルゴリズム

### 開発ワークフロー
```bash
# 開発サーバーの起動
uv run --reload app.py

# テストの実行
uv run pytest

# コードフォーマット
uv run black .
```

## 参考資料

- [[For Server Developers]]
- [[MCPサーバー自作入門]]
- [[やさしいMCP入門]]

## メモ

- 2025-07-23: 査定自動化プロジェクトでMCPサーバー開発のためのPython環境管理ツールとして学習が必要
- Rustで実装された高速なPythonパッケージマネージャー
- MCPサーバー開発での標準的なツールとして採用されている
- 従来のpipやpoetryよりも大幅に高速で効率的 