---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# Articles__CatalogsController

> 本来のクラス名は Articles::CatalogsController です

---

## アクション一覧と詳細

### `edit` (出典: app/controllers/articles/catalogs_controller.rb:6)

* **機能概要:**
  物件ID・document_typeで分岐し、マイソク編集・シミュレーション編集・エラー遷移。
* **処理フロー:**
    1. 物件IDでArticleを取得（:7）
    2. document_typeが空または'maisoku'ならマイソク編集へリダイレクト（:9）
    3. document_typeが'simulation'ならシミュレーション編集へリダイレクト（:10-11）
    4. それ以外はrouting_error（:12）
* **返すもの:**
    - 編集画面へのリダイレクトまたはエラー

---

## 関連リンク
- [[Article]]
- [[マイソク]]
- [[シミュレーション]] 