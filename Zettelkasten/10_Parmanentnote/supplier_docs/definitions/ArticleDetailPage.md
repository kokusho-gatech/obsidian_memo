# 発表詳細ページ（/articles/:id）

> [[ArticlesController]] `show`アクション & `app/views/articles/show.html.erb` による描画

---

## 画面概要

- 物件（Article）の詳細情報を表示・編集する画面。
- 物件名、各種タブ（全体・FLOW・マイソク・発表・その他・決済・水道・取引台帳・発表後管理・評価）、物件情報、契約・担当・進捗などを表示。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles_controller.rb:17-60`
    - `@article` : 詳細表示対象の[[Article]]
    - `@sales_contract_field`, `@article_wrapper_class`, `@additionally_cfm_item_ids`, `@past_articles_count`, `@is_valuation_histories_editable_user`, `@ownr_info`, `@modification_histories`, `@article_items_for_file_tab`, `@file_tabs_html`, `@is_show_page`, `@equipment`, `@auth_url`, `@purchase_contract`, `@transaction_register`, `@janitor`, `@prior_valuation`, `@same_building_prior_valuations` など

- **主なロジック:**
    - Articleの状態に応じてリダイレクト（査定中→編集、交渉中→交渉詳細）
    - 関連情報・履歴・ファイルタブ・契約情報などをセット

---

## 2. UIとデータの対応

- **物件名:** `@article.article_name` (`show.html.erb:20`)
- **タブ:** 各種タブリンク（`show.html.erb:30-50`）
- **物件情報:** 各タブ内で`render`されるパーシャル
- **契約・担当・進捗:** 各フォームフィールド
- **ページネーションや各種リンク**

---

## 関連リンク
- [[ArticlesController]]
- [[Article]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles_controller.rb`
- モデル: `app/models/article.rb`
- ビュー: `app/views/articles/show.html.erb` 