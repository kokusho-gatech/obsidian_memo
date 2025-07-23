---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# FilePublishedDatesController

> 本来のクラス名は FilePublishedDatesController です

---

## アクション一覧と詳細

### `create` (出典: app/controllers/file_published_dates_controller.rb:5)

* **機能概要:**
  ファイル公開日の新規登録。
* **処理フロー:**
    1. ArticleItemFileをIDで取得（:6）
    2. build_file_published_dateで新規作成（:7-9）
    3. バリデーション・保存（:11-13）
    4. 成功時はJSON、失敗時はエラーJSON（:14-16）
    5. 例外時はRollbar通知・エラーJSON（:18-20）
* **返すもの:**
    - 成功/失敗メッセージのJSON

---

### `update` (出典: app/controllers/file_published_dates_controller.rb:22)

* **機能概要:**
  ファイル公開日の更新。
* **処理フロー:**
    1. FilePublishedDateをIDで取得（:24）
    2. 日付を更新し保存（:25-27）
    3. 成功時はJSON、失敗時はエラーJSON（:28-30）
    4. 例外時はRollbar通知・エラーJSON（:31-33）
* **返すもの:**
    - 成功/失敗メッセージのJSON

---

## 関連リンク
- [[ArticleItemFile]]
- [[ファイル管理]] 