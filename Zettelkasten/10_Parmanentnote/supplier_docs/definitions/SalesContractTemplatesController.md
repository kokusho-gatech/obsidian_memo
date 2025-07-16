# SalesContractTemplatesController

> 本来のクラス名は SalesContractTemplatesController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/sales_contract_templates_controller.rb:5)

* **機能概要:**
  売買契約テンプレートの一覧を表示。
* **処理フロー:**
    1. テンプレートをID順で全件取得（:6）
* **返すもの:**
    - 一覧画面のHTML

---

### `edit` (出典: app/controllers/sales_contract_templates_controller.rb:9)

* **機能概要:**
  テンプレート編集画面の表示。権限チェックあり。
* **処理フロー:**
    1. 権限チェック（:11-13）
    2. テンプレート取得（:15）
    3. 権限がなければリダイレクト
* **返すもの:**
    - 編集画面のHTMLまたはリダイレクト

---

### `update` (出典: app/controllers/sales_contract_templates_controller.rb:18)

* **機能概要:**
  テンプレート内容の更新。権限チェックあり。
* **処理フロー:**
    1. テンプレート取得（:19）
    2. 権限チェック（:21-23）
    3. 更新処理（:25-32）
    4. 成功時は一覧へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

## 関連リンク
- [[SalesContractTemplate]]
- [[権限管理]] 