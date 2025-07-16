# AssessmentController

## 役割
このコントローラは[[Article]]モデルの査定一覧管理（一覧表示、検索、CSV出力など）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["査定一覧取得→[[assessment/index.html.erb]]表示"]
  "C" -->|"download"| "D2"["CSV生成→ダウンロード"]
```

## アクション一覧
- `index`: 査定一覧 