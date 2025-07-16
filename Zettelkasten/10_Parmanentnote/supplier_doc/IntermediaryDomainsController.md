# IntermediaryDomainsController

## 役割
このコントローラは[[IntermediaryDomain]]モデルの仲介ドメイン管理（新規作成、編集、削除）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"new"| "D1"["新規作成フォーム→[[intermediary_domains/new.html.erb]]表示"]
  "C" -->|"edit"| "D2"["編集フォーム→[[intermediary_domains/edit.html.erb]]表示"]
  "C" -->|"create"| "D3"["新規作成→保存→リダイレクトor再表示"]
  "C" -->|"update"| "D4"["編集→保存→リダイレクトor再表示"]
  "C" -->|"destroy"| "D5"["削除→リダイレクト"]
```

## アクション一覧
- `new`: 新規作成フォームを表示。
- `edit`: 編集フォームを表示。
- `create`: 新規仲介ドメインを作成。成功時は親会社編集画面へリダイレクト、失敗時は再表示。
- `update`: 仲介ドメイン情報を更新。成功時は親会社編集画面へリダイレクト、失敗時は再表示。
- `destroy`: 仲介ドメインを削除し、親会社編集画面へリダイレクト。

## コールバック
- 各アクションで親会社（[[IntermediaryCompany]]）の取得。

## Strong Parameters
- `intermediary_domain_params`:
  - 許可: `:domain`, `:user_id` 