# PurchaseContracts__CancellationsController

> 本来のクラス名は PurchaseContracts::CancellationsController です

---

## アクション一覧と詳細

### `create` (出典: app/controllers/purchase_contracts/cancellations_controller.rb:5)

* **機能概要:**
  仕入契約のキャンセル登録。
* **処理フロー:**
    1. PurchaseContractをIDで取得（:6）
    2. CreateFormを生成し保存（:7-9, private:18-20）
    3. 成功時はフラッシュ・リダイレクト、失敗時はエラー表示（:10-15）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
- [[PurchaseContract]]
- [[キャンセル処理]] 