# 仲介担当なし一覧ページ（/articles/unassociated）

> [[Articles__UnassociatedController]] `index`アクション & `app/views/articles/unassociated/index.html.erb` による描画

---

## 画面概要

- 仲介会社・担当者が未連携の物件（Article）を一覧表示する画面。
- 物件名・受信日時・タイトル・本文・メール情報・仲介マスタ登録状況・返信状況を表示。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/unassociated_controller.rb:5-14`
    - `@articles` : `Article.unassociated` で取得、関連情報をpreload、ページネーション

- **主なロジック:**
    - `Article.unassociated` スコープで「仲介未連携」物件を抽出
    - 関連情報（intermediary_company, intermediary_domain, intermediary_staff, attachment.supplier_mail）をpreload
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **物件一覧テーブル:**
    - `<% @articles.each do |article| %> ... </tr> <% end %>` (`index.html.erb:22-87`)
        - [[Article]] 一覧を1行ずつ表示。
        - 各カラムの対応：
            - **物件名:** `display_article_name(article.building_name, article.room_number, article.floor)`（リンク付き、`edit_articles_assessment_path`へ）
            - **受信日時:** `article&.attachment&.supplier_mail&.received_at&.strftime('%-m/%-d %-H:%M')`
            - **タイトル:** `article.subject_from_intermediary_email`
            - **本文:** `truncate(article&.attachment&.supplier_mail&.body, length: 70)`
            - **メール情報:** From/To/Cc/Bcc
            - **仲介マスタ登録:** 各マスタへのリンク or 未連携表示
            - **返信状況:** `article.unnecessary_to_reply?`/`article.email_replied_at`
    - **ページネーション:**
        - `paginate @articles` (`index.html.erb:4`)

---

## 関連リンク
- [[Articles__UnassociatedController]]
- [[Article]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/unassociated_controller.rb`
- モデル: `app/models/article.rb`
- ビュー: `app/views/articles/unassociated/index.html.erb` 