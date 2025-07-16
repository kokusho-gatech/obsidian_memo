# 交渉詳細(バイヤー用)ページ（/articles/:id/management/for_approval/edit）

> [[Articles__Management__ForApprovalsController]] `edit`アクション & `app/views/articles/management/for_approvals/edit.html.erb` による描画

---

## 画面概要

- 交渉中物件の詳細情報をバイヤー担当者が編集・管理する画面。
- 物件情報、交渉履歴、ファイルタブ、建物情報、仲介/バイヤー情報などを表示・編集。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/management/for_approvals_controller.rb:5-64`
    - `@article` : 編集対象の[[Article]]
    - `@form` : 編集フォーム
    - `@negotiation_history_form`, `@negotiation_histories`, `@prior_valuation_form`, `@same_building_prior_valuations`, `@article_items_for_file_tab`, `@file_tabs_html`, `@negotiated_same_building_and_floor_in`, `@sold_with_same_room`, `@past_articles_count` など

- **主なロジック:**
    - 編集対象Articleの取得・権限チェック
    - 各種フォーム・表示用インスタンス変数のセット
    - ページ遷移やリダイレクト制御

---

## 2. UIとデータの対応

- **物件名:** `@article.article_name` (`edit.html.erb:8`)
- **交渉履歴:** `@negotiation_histories` (`edit.html.erb:---`)
- **ファイルタブ:** `@file_tabs_html` (`edit.html.erb:---`)
- **仲介会社・担当・バイヤー担当:** 各フォームフィールド (`edit.html.erb:---`)
- **建物情報:** BLDGリンク、過去取扱物件リンク (`edit.html.erb:---`)
- **仕入評価:** `@prior_valuation_form` など
- **ページネーションや各種リンク**

---

## 関連リンク
- [[Articles__Management__ForApprovalsController]]
- [[Article]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/management/for_approvals_controller.rb`
- モデル: `app/models/article.rb`
- ビュー: `app/views/articles/management/for_approvals/edit.html.erb` 