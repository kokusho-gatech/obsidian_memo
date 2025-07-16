# UnprocessedMailsController

> 本来のクラス名は UnprocessedMailsController です

---

## アクション一覧と詳細

### `new` (出典: app/controllers/unprocessed_mails_controller.rb:5)

* **機能概要:**
  未処理メールの新規登録画面の表示。
* **処理フロー:**
    1. 認証（before_action:2, private:45-48）
* **返すもの:**
    - 新規作成画面のHTML

---

### `create` (出典: app/controllers/unprocessed_mails_controller.rb:7)

* **機能概要:**
  未処理メールの登録・物件作成。
* **処理フロー:**
    1. パラメータバリデーション（:8-10）
    2. SupplierMailをGmail IDで検索（:12-14）
    3. 該当があれば物件・添付ファイルを作成しアップロード（:15-18）
    4. 該当がなければエラーレスポンス（:20-22）
    5. 例外時はRollbar通知・エラーレスポンス（:24-31）
* **返すもの:**
    - 成功時は物件IDのJSON、失敗時はエラーメッセージ

---

## 関連リンク
- [[SupplierMail]]
- [[Article]] 