# ContractController

## 役割
このコントローラは[[Article]]モデルの物件情報を外部システム（TechConsul）へ連携（release）する処理を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"release"| "D1"["物件情報更新・TechConsul連携→JSON/エラー返却"]
```

## アクション一覧
- `release`: 物件情報を更新し、TechConsulへ連携。成功時はJSON、失敗時はエラーメッセージを返却。

## コールバック
- 各アクションで認証・権限チェック（ApplicationController由来）。

## Strong Parameters
- `article_params`:
  - 許可: `base_attributes`（詳細は[[Article]]参照）
- `maisoku_params`:
  - 許可: `:maisoku` 