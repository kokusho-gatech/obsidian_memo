# PurchaseContractsController

## 役割
このコントローラは[[PurchaseContract]]および[[Article]]モデルの仕入契約管理（一覧表示、CSVダウンロード）を担当します。

## 処理フロー
```mermaid
graph TD
  A[リクエスト受信] -->|before_action| B[set_articleで記事検索]
  B --> C{アクション分岐}
  C -->|index| D1[仕入契約一覧取得→[[purchase_contracts/index.html.erb]]表示]
  C -->|download| D2[CSV生成→ダウンロード]
```

## アクション一覧
- `index`: 仕入契約一覧を取得し、[[purchase_contracts/index.html.erb]]を表示。
- `download`: 検索条件に合致する仕入契約一覧をCSVでダウンロード。

## コールバック
- `set_article`: 検索条件に合致する[[Article]]一覧を取得。

## Strong Parameters
- 直接的なStrong Parametersはなし（set_article内でransackを利用）。 