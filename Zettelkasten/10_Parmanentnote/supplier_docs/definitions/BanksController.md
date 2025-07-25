---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# BanksController

> 本来のクラス名は BanksController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/banks_controller.rb:5)

* **機能概要:**
  銀行の一覧表示。
* **処理フロー:**
    1. 関連ユーザーをpreloadしID順で取得（:6）
* **返すもの:**
    - 一覧画面のHTML

---

### `new` (出典: app/controllers/banks_controller.rb:10)

* **機能概要:**
  新規銀行作成画面の表示。
* **処理フロー:**
    1. 新規インスタンス作成（:11）
* **返すもの:**
    - 新規作成画面のHTML

---

### `edit` (出典: app/controllers/banks_controller.rb:14)

* **機能概要:**
  銀行編集画面の表示。
* **処理フロー:**
    1. インスタンス取得（:15）
* **返すもの:**
    - 編集画面のHTML

---

### `create` (出典: app/controllers/banks_controller.rb:18)

* **機能概要:**
  新規銀行の作成。
* **処理フロー:**
    1. 新規インスタンス作成（:19）
    2. ユーザー紐付け（:20）
    3. 保存処理（:22-27）
    4. 成功時は一覧へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `update` (出典: app/controllers/banks_controller.rb:30)

* **機能概要:**
  銀行内容の更新。
* **処理フロー:**
    1. インスタンス取得（:31）
    2. ユーザー紐付け（:32）
    3. 更新処理（:34-39）
    4. 成功時は一覧へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

## 関連リンク
- [[Bank]]
- [[権限管理]] 