# SupplierMailsController

> 本来のクラス名は SupplierMailsController です

---

## アクション一覧と詳細

### `new` (出典: app/controllers/supplier_mails_controller.rb:6)

* **機能概要:**
  仕入メールの新規登録画面の表示。
* **処理フロー:**
    1. 新規インスタンス作成（:7）
    2. 認証（before_action:4, private:38-41）
* **返すもの:**
    - 新規作成画面のHTML

---

### `create` (出典: app/controllers/supplier_mails_controller.rb:10)

* **機能概要:**
  仕入メールの新規登録。
* **処理フロー:**
    1. 新規インスタンス作成（:11）
    2. 保存処理（:13-17）
    3. 成功時は未処理メール登録画面へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

## 関連リンク
- [[SupplierMail]]
- [[Article]] 