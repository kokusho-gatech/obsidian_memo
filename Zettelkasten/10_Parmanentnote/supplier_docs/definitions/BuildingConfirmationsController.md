---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# BuildingConfirmationsController

> 本来のクラス名は BuildingConfirmationsController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/building_confirmations_controller.rb:5)

* **機能概要:**
  建物確認情報の一覧表示。
* **処理フロー:**
    1. set_articleで物件を取得（private:61-63）
    2. building_confirmationsをpreloadしID降順で取得（:7）
* **返すもの:**
    - 一覧画面のHTML

---

### `new` (出典: app/controllers/building_confirmations_controller.rb:10)

* **機能概要:**
  新規建物確認情報作成画面の表示。
* **処理フロー:**
    1. set_articleで物件を取得（:11）
    2. 新規インスタンス作成（:12）
* **返すもの:**
    - 新規作成画面のHTML

---

### `edit` (出典: app/controllers/building_confirmations_controller.rb:15)

* **機能概要:**
  建物確認情報編集画面の表示。
* **処理フロー:**
    1. set_articleで物件を取得（:16）
    2. インスタンス取得（:17）
* **返すもの:**
    - 編集画面のHTML

---

### `create` (出典: app/controllers/building_confirmations_controller.rb:20)

* **機能概要:**
  新規建物確認情報の作成。
* **処理フロー:**
    1. set_articleで物件を取得（:21）
    2. building_confirmations.buildで新規作成（:22）
    3. 保存処理（:24-29）
    4. 成功時は一覧へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `update` (出典: app/controllers/building_confirmations_controller.rb:32)

* **機能概要:**
  建物確認情報の更新。
* **処理フロー:**
    1. インスタンス取得（:33）
    2. 更新処理（:34-39）
    3. 成功時は一覧へリダイレクト、失敗時はエラー表示
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `destroy` (出典: app/controllers/building_confirmations_controller.rb:42)

* **機能概要:**
  建物確認情報の削除。
* **処理フロー:**
    1. set_articleで物件を取得（:43）
    2. インスタンス削除（:44）
    3. 一覧へリダイレクト（:46）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
- [[BuildingConfirmation]]
- [[Article]] 