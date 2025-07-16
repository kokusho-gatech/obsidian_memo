# IntermediaryDomainsController

> 本来のクラス名は IntermediaryDomainsController です

---

## アクション一覧と詳細

### `new` (出典: app/controllers/intermediary_domains_controller.rb:5)

* **機能概要:**
  仲介ドメインの新規作成画面の表示。
* **処理フロー:**
    1. 仲介会社をIDで取得（:6）
    2. 新規ドメインインスタンス作成（:7）
* **返すもの:**
    - 新規作成画面のHTML

---

### `edit` (出典: app/controllers/intermediary_domains_controller.rb:10)

* **機能概要:**
  仲介ドメイン編集画面の表示。
* **処理フロー:**
    1. 仲介会社・ドメインをIDで取得（:11-12）
* **返すもの:**
    - 編集画面のHTML

---

### `create` (出典: app/controllers/intermediary_domains_controller.rb:15)

* **機能概要:**
  仲介ドメインの新規作成。
* **処理フロー:**
    1. 仲介会社をIDで取得（:16）
    2. 新規ドメインインスタンス作成（:17-18）
    3. 保存処理（:20-25）
    4. 成功時は仲介会社編集画面へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `update` (出典: app/controllers/intermediary_domains_controller.rb:27)

* **機能概要:**
  仲介ドメインの更新。
* **処理フロー:**
    1. 仲介会社・ドメインをIDで取得（:28-29）
    2. 更新処理（:31-36）
    3. 成功時は仲介会社編集画面へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `destroy` (出典: app/controllers/intermediary_domains_controller.rb:38)

* **機能概要:**
  仲介ドメインの削除。
* **処理フロー:**
    1. 仲介会社・ドメインをIDで取得（:39-40）
    2. 削除処理（:42）
    3. 成功/失敗時は仲介会社編集画面へリダイレクト（:44-47）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
- [[IntermediaryDomain]]
- [[IntermediaryCompany]] 