# SalesContractFieldsController

> 本来のクラス名は Articles::SalesContractFieldsController です

---

## アクション一覧と詳細

### `copy` (出典: app/controllers/articles/sales_contract_fields_controller.rb:24)

* **機能概要:**
  他物件から契約情報をコピー。
* **処理フロー:**
    1. target_article_idでArticleを取得し、sales_contract_relation_field_copy!を実行（:27-30）
    2. 例外時はエラーレスポンス（:31-33）
* **返すもの:**
    - 成功/失敗メッセージのJSON

---

### `sales_agreement_set` (出典: app/controllers/articles/sales_contract_fields_controller.rb:36)

* **機能概要:**
  契約書類一式のPDF生成・ダウンロード。
* **処理フロー:**
    1. 必須属性チェック（:37-40）
    2. 各種PDFを生成しzip化（:42-49）
    3. send_fileでダウンロード（:50-51）
* **返すもの:**
    - zipファイルのダウンロード

---

### `edit` (出典: app/controllers/articles/sales_contract_fields_controller.rb:53)

* **機能概要:**
  契約書編集画面の表示。
* **処理フロー:**
    1. ファイルタブHTML生成（:54-60）
    2. ページ番号取得（:61）
* **返すもの:**
    - 編集画面のHTML

---

### `update` (出典: app/controllers/articles/sales_contract_fields_controller.rb:63)

* **機能概要:**
  契約書情報の更新・外部連携。
* **処理フロー:**
    1. ユーザー情報セット（:64）
    2. 顧客情報挿入可否チェック（:65-67）
    3. トランザクションで更新（:69-71）
    4. リリース済みなら外部連携（:73-75）
    5. 例外時はエラーレスポンス（:80-95）
* **外部連携:**
    - Connectors::TechConsul（:73）
* **返すもの:**
    - 成功/失敗メッセージ

---

## 関連リンク
- [[Article]]
- [[SalesContractField]]
- [[契約書管理]]
- [[外部API連携]] 