# IntermediaryStaffsController

> 本来のクラス名は IntermediaryStaffsController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/intermediary_staffs_controller.rb:5)

* **機能概要:**
  仲介担当者の一覧表示。
* **処理フロー:**
    1. 会社IDで絞り込み、preload・orderで取得（:6-10）
* **返すもの:**
    - 一覧画面のHTML

---

### `new` (出典: app/controllers/intermediary_staffs_controller.rb:12)

* **機能概要:**
  新規仲介担当者作成画面の表示。
* **処理フロー:**
    1. 仲介会社をIDで取得（:13）
    2. 新規担当者インスタンス作成（:14）
* **返すもの:**
    - 新規作成画面のHTML

---

### `edit` (出典: app/controllers/intermediary_staffs_controller.rb:17)

* **機能概要:**
  仲介担当者編集画面の表示。
* **処理フロー:**
    1. 仲介会社・担当者をIDで取得（:18-19）
* **返すもの:**
    - 編集画面のHTML

---

### `create` (出典: app/controllers/intermediary_staffs_controller.rb:22)

* **機能概要:**
  新規仲介担当者の作成。
* **処理フロー:**
    1. 仲介会社をIDで取得（:23）
    2. 新規担当者インスタンス作成（:24）
    3. updateで保存（:26-31）
    4. 成功時は会社編集画面へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `update` (出典: app/controllers/intermediary_staffs_controller.rb:33)

* **機能概要:**
  仲介担当者の更新。
* **処理フロー:**
    1. 仲介会社・担当者をIDで取得（:34-35）
    2. updateで保存（:37-42）
    3. 成功時は会社編集画面へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `destroy` (出典: app/controllers/intermediary_staffs_controller.rb:45)

* **機能概要:**
  仲介担当者の削除。
* **処理フロー:**
    1. 仲介会社・担当者をIDで取得（:46-47）
    2. destroyで削除（:49）
    3. 成功/失敗時は会社編集画面へリダイレクト（:51-54）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
- [[IntermediaryStaff]]
- [[IntermediaryCompany]] 