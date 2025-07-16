# IntermediaryStaffs__MultipleSelectOptionsController

> 本来のクラス名は IntermediaryStaffs::MultipleSelectOptionsController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/intermediary_staffs/multiple_select_options_controller.rb:5)

* **機能概要:**
  仲介担当者の複数選択オプション一覧を取得。
* **処理フロー:**
    1. targetパラメータを取得（:6）
    2. intermediary_company_idsで担当者を絞り込み、preloadで取得（:7-9）
* **返すもの:**
    - オプション一覧のHTML

---

## 関連リンク
- [[IntermediaryStaff]]
- [[IntermediaryCompany]] 