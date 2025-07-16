# SaleStatesController

> 本来のクラス名は Articles::SaleStatesController です

---

## アクション一覧と詳細

### `update` (出典: app/controllers/articles/sale_states_controller.rb:6)

* **機能概要:**
  物件の販売状態を更新。
* **処理フロー:**
    1. ArticleをIDで取得（:7）
    2. Handlerを生成しexecuteで更新（:8-13）
    3. 成功/失敗時はフラッシュ・リダイレクト（:14-16）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
 