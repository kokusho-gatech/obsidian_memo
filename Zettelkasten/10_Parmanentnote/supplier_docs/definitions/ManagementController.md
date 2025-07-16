# ManagementController

> 本来のクラス名は ManagementController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/management_controller.rb:5)

* **機能概要:**
  交渉物件の一覧表示・検索。
* **処理フロー:**
    1. IndexFormで検索条件を構築（:6）
    2. 検索結果を降順・ページネーション（:7）
* **返すもの:**
    - 一覧画面のHTML

---

### `show` (出典: app/controllers/management_controller.rb:10)

* **機能概要:**
  交渉物件の詳細表示。権限により遷移先が異なる。
* **処理フロー:**
    1. 物件取得（:11）
    2. 権限によりfor_payment_requestまたはfor_approvalへリダイレクト（:12-15）
* **返すもの:**
    - 詳細画面のHTMLまたはリダイレクト

---

## 関連リンク
- [[Article]]
- [[交渉]] 