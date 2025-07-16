# HomeController

## 役割
このコントローラはアプリケーションのホーム画面（トップページ）を表示します。

## 処理フロー
```mermaid
graph TD
  "A"["リクエスト受信"] --> "B"{"アクション分岐"}
  "B" -->|"index"| "C"["ホーム画面表示→[[home/index.html.erb]]"]
```

## アクション一覧
- `index`: ホーム画面を表示。

## コールバック
- 特になし（ApplicationControllerの認証等は継承）。

## Strong Parameters
- なし 