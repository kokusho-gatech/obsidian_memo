# 交渉一覧ページ（/articles/management）

> [[ManagementController]] `index`アクション & `app/views/management/index.html.erb` による描画

---

## 画面概要

- 交渉中の物件（Article）を一覧表示する画面。
- 物件名・号室・仲介会社・担当・交渉登録・交渉感触・交渉回数・査定返信日・金額・最終交渉・コメント・現況など多数カラムを表示。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/management_controller.rb:4-11`
    - `@index_form` : 検索条件フォーム
    - `@articles` : `Article::Management::IndexForm`で絞り込み、ページネーション

- **主なロジック:**
    - 検索条件をフォームで受け取り、callで絞り込み
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `render 'index_form', model: @index_form` (`index.html.erb:5`)
- **一覧テーブル:**
    - `<%= render Article::Management::ListRowComponent.new(article:) %>` (`index.html.erb:74`)
        - 各カラムはListRowComponentで描画
- **ページネーション:**
    - `paginate @articles` (`index.html.erb:28`)

---

## 関連リンク
- [[ManagementController]]
- [[Article]]
- [[Article__Management__IndexForm]]
- [[Article__Management__ListRowComponent]]

---

## 参考ファイル
- コントローラ: `app/controllers/management_controller.rb`
- モデル: `app/models/article.rb`, `app/models/article/management/index_form.rb`
- ビュー: `app/views/management/index.html.erb`
- コンポーネント: `app/components/article/management/list_row_component.rb` など 