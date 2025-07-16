# PurchaseContractsController

> 本来のクラス名は PurchaseContractsController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/purchase_contracts_controller.rb:5)

* **機能概要:**
  仕入契約物件の一覧表示・検索。
* **処理フロー:**
    1. set_articleで物件一覧を取得（private:38-61）
    2. ページネーション（:7-8）
* **返すもの:**
    - 一覧画面のHTML

---

### `download` (出典: app/controllers/purchase_contracts_controller.rb:10)

* **機能概要:**
  仕入契約物件のCSVダウンロード。
* **処理フロー:**
    1. set_articleで物件一覧を取得（private:38-61）
    2. 一時ファイルにCSVを書き出し（:13-19）
    3. send_dataでダウンロードレスポンス（:21-22）
    4. 一時ファイル削除（:24）
* **返すもの:**
    - CSVファイルのダウンロードレスポンス

---

## 関連リンク
- [[Article]]
- [[仕入契約]]
- [[CSV出力]] 