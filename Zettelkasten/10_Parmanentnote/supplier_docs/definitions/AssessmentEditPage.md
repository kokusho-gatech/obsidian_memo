# 査定編集ページ（/articles/assessment/:id/edit）

> [[Articles__AssessmentController]] `edit`アクション & `app/views/articles/assessment/edit.html.erb` による描画

---

## 画面概要

- 物件（Article）の査定情報を編集する画面。
- 物件情報、AI家賃予測、過去取扱物件、ファイルタブ、各種フォームを表示。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/assessment_controller.rb:4-83`
    - `@article` : 編集対象の[[Article]]
    - `@form` : 編集フォーム
    - `@article_items_for_file_tab`, `@file_tabs_html`, `@price_prediction`, `@prior_valuation_form`, `@latest_prior_valuation`, `@same_building_prior_valuations`, `@negotiated_same_building_and_floor_in`, `@past_articles_count` など

- **主なロジック:**
    - 編集対象Articleの取得・権限チェック
    - 各種フォーム・表示用インスタンス変数のセット
    - ページ遷移やリダイレクト制御

---

## 2. UIとデータの対応

- **物件名:** `@article.article_name` (`edit.html.erb:13`)
- **AI家賃予測:** `@price_prediction.rental_price` (`edit.html.erb:22`)
- **ファイルタブ:** `@file_tabs_html` (`edit.html.erb:41`)
- **過去取扱物件:** `@past_articles_count`、リンク (`edit.html.erb:61`)
- **住所・階数・間取り・家賃等:** 各フォームフィールド (`edit.html.erb:80-250` 付近)
- **交渉履歴・査定履歴:** `@same_building_prior_valuations` など
- **ページネーションや各種リンク**

---

## 関連リンク
- [[Articles__AssessmentController]]
- [[Article]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/assessment_controller.rb`
- モデル: `app/models/article.rb`
- ビュー: `app/views/articles/assessment/edit.html.erb` 