# Articles__InputsController

> 本来のクラス名は Articles::InputsController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/articles/inputs_controller.rb:6)

* **機能概要:**
  書類入力項目の一覧表示。
* **処理フロー:**
    1. ArticleをIDで取得（:7）
    2. article_itemsをpreloadし、入力対象のみソート・build（:8-12）
    3. purchase_contract・sales_infoを取得（:13-14）
* **返すもの:**
    - 入力項目一覧画面のHTML

---

## 関連リンク
- [[Article]]
- [[書類入力]] 