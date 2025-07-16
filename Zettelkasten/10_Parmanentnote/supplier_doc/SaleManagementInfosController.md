# SaleManagementInfosController

## 役割
このコントローラは[[Article]]モデルの発表管理（一覧表示、CSVダウンロード）を担当します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] -->|"before_action"| "B"["認証・権限チェック"]
  "B" --> "C"{"アクション分岐"}
  "C" -->|"index"| "D1"["発表管理一覧取得→[[sale_management_infos/index.html.erb]]表示"]
  "C" -->|"download"| "D2"["CSV生成→ダウンロード"]
```

## アクション一覧
- `index`: 発表管理一覧を取得し、[[sale_management_infos/index.html.erb]]を表示。
- `download`: 検索条件に合致する発表管理一覧をCSVでダウンロード。

## コールバック
- 検索条件の変換やman_yen_to_yen変換などをprivateメソッドで実施。

## Strong Parameters
- 直接的なStrong Parametersはなし（ransackを利用）。 