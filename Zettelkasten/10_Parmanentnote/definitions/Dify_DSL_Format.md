---
tags:
  - dify
  - dsl
  - yaml
  - workflow-definition
  - architecture
  - definitions
creation-date: 2025-02-01
---

# Dify DSL Format

## 概要

DifyのDSL（Domain Specific Language）は、AIワークフローアプリケーションを定義するためのYAML形式の設定ファイルです。ワークフローの実行フロー、ノード間の関係、各処理の詳細設定を宣言的に記述します。

## DSLファイル全体構造

```yaml
app:                    # アプリケーション基本情報
dependencies:           # 外部依存関係
kind:                   # リソース種別
version:                # スキーマバージョン
workflow:               # ワークフロー定義（メイン部分）
```

## 詳細構造

### 1. アプリケーション定義 (`app`)

```yaml
app:
  description: string           # アプリケーションの説明
  icon: string                 # アイコン（絵文字）
  icon_background: string      # アイコン背景色
  mode: string                 # 実行モード（workflow, chat, completion等）
  name: string                 # アプリケーション名
  use_icon_as_answer_icon: boolean
```

### 2. 依存関係 (`dependencies`)

```yaml
dependencies:
  - current_identifier: string    # 現在の識別子
    type: string                 # 依存タイプ（marketplace等）
    value:
      marketplace_plugin_unique_identifier: string  # マーケットプレイスプラグインID
```

### 3. ワークフロー定義 (`workflow`)

#### 3.1 環境変数

```yaml
workflow:
  environment_variables:
    - description: string        # 変数の説明
      id: string                # 一意識別子
      name: string              # 変数名
      selector: [env, variable_name]  # セレクタ
      value: string             # デフォルト値
      value_type: string        # 値の型
```

#### 3.2 機能設定

```yaml
  features:
    file_upload:                # ファイルアップロード設定
      enabled: boolean
      allowed_file_extensions: [string]
      allowed_file_types: [string]
    retriever_resource:         # 検索リソース設定
      enabled: boolean
    # その他の機能設定...
```

#### 3.3 グラフ構造

ワークフローの核心部分で、ノード間の接続関係と各ノードの処理内容を定義します。

##### エッジ（接続関係）

```yaml
  graph:
    edges:
      - data:                   # エッジデータ
          isInLoop: boolean     # ループ内か
          sourceType: string    # 接続元ノードタイプ
          targetType: string    # 接続先ノードタイプ
        id: string              # エッジID
        source: string          # 接続元ノードID
        sourceHandle: string    # 接続元ハンドル
        target: string          # 接続先ノードID
        targetHandle: string    # 接続先ハンドル
        type: string            # エッジタイプ
```

##### ノード（処理単位）

```yaml
    nodes:
      - data:                   # ノード固有データ
          # ノードタイプによって異なる構造
        height: number          # UI上の高さ
        id: string              # 一意識別子
        position:               # UI上の位置
          x: number
          y: number
        type: string            # ノードタイプ
        width: number           # UI上の幅
```

## 主要ノードタイプ

### 1. 開始ノード (`start`)

```yaml
data:
  desc: string                  # 説明
  title: string                 # タイトル
  type: start
  variables:                    # 入力変数定義
    - label: string             # ラベル
      max_length: number        # 最大長
      required: boolean         # 必須フラグ
      type: string              # 変数型
      variable: string          # 変数名
```

### 2. LLMノード (`llm`)

```yaml
data:
  model:                        # 使用モデル
    completion_params:          # 完了パラメータ
      temperature: number
    mode: string                # モード（chat, completion等）
    name: string                # モデル名
    provider: string            # プロバイダー
  prompt_template:              # プロンプトテンプレート
    - id: string
      role: string              # system, user, assistant
      text: string              # プロンプト本文
  title: string
  type: llm
```

### 3. コードノード (`code`)

```yaml
data:
  code: string                  # 実行コード
  code_language: string        # 言語（python3, javascript等）
  desc: string                  # 説明
  outputs:                      # 出力定義
    result:
      children: null
      type: string              # 出力型
  title: string
  type: code
  variables:                    # 入力変数
    - value_selector: [string]  # 値セレクタ
      variable: string          # 変数名
```

### 4. ナレッジ検索ノード (`knowledge-retrieval`)

```yaml
data:
  dataset_ids: [string]         # データセットID
  multiple_retrieval_config:    # 検索設定
    reranking_enable: boolean
    reranking_model:
      model: string
      provider: string
    score_threshold: number     # スコア閾値
    top_k: number               # 取得件数
    weights:                    # 重み設定
      keyword_setting:
        keyword_weight: number
      vector_setting:
        embedding_model_name: string
        vector_weight: number
  query_variable_selector: [string]  # クエリ変数
  retrieval_mode: string        # 検索モード
  title: string
  type: knowledge-retrieval
```

### 5. パラメータ抽出ノード (`parameter-extractor`)

```yaml
data:
  model:                        # 使用モデル設定
  parameters:                   # 抽出パラメータ定義
    - description: string       # パラメータ説明
      name: string              # パラメータ名
      required: boolean         # 必須フラグ
      type: string              # データ型
  query: [string]               # 入力クエリ
  title: string
  type: parameter-extractor
```

### 6. 条件分岐ノード (`if-else`)

```yaml
data:
  cases:                        # 条件ケース
    - case_id: string           # ケースID
      conditions:               # 条件定義
        - comparison_operator: string  # 比較演算子
          id: string
          value: string         # 比較値
          varType: string       # 変数型
          variable_selector: [string]  # 変数セレクタ
      logical_operator: string  # 論理演算子
  title: string
  type: if-else
```

### 7. 終了ノード (`end`)

```yaml
data:
  outputs: []                   # 出力定義
  title: string
  type: end
```

## 変数参照システム

DSL内では、ノード間での値の受け渡しに統一された参照システムを使用：

```yaml
value_selector:
  - "ノードID"                  # 参照元ノードID
  - "出力フィールド名"          # 出力フィールド名
```

例：
```yaml
variables:
  - value_selector:
    - '1744282688828'           # 文章構造化ノードID
    - text                      # textフィールド
    variable: input_text        # ローカル変数名
```

## 座標系とレイアウト

UI上での配置情報も含まれ、ワークフローの視覚的な構造を保持：

```yaml
position:
  x: number                     # X座標
  y: number                     # Y座標
positionAbsolute:              # 絶対座標
  x: number
  y: number
height: number                  # ノードの高さ
width: number                   # ノードの幅
```

## データフロー特徴

1. **宣言的定義**: 実行順序はエッジで定義される依存関係で決定
2. **型安全性**: 各変数と出力に明確な型定義
3. **モジュラー構造**: 各ノードが独立した処理単位
4. **設定の外部化**: 環境変数による設定値の管理
5. **視覚的編集対応**: UI座標情報の保持

## 実行時の動作

```
開始ノード → パラメータ抽出 → 条件分岐 → 並列処理 → 結果統合 → 終了ノード
    ↓           ↓            ↓         ↓          ↓         ↓
  入力受付   → 構造化解析  → ルート選択 → 各種判定  → 文章生成  → 出力
```

DSLファイルは、この複雑な処理フローを宣言的かつ再現可能な形で記述するためのフォーマットです。

## 関連概念

- [[Dify]]
- [[YAML]]
- [[ワークフロー設計]]
- [[AIアプリケーション開発]]

```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}

for (let outgo of dv.pages('outgoing([[' + dv.current().file.name + ']])')) {
    dv.header(4, outgo.file.name);
    dv.list(outgo.file.inlinks.sort());
}

// バックリンクがあるノートも出力
let backlinks = dv.pages().where(p => p.file.inlinks && p.file.inlinks.map(l=>l.path).includes(dv.current().file.path));
if (backlinks.length > 0) {
    dv.header(3, "このノートへのバックリンク");
    dv.list(backlinks.file.link);
}

``` 