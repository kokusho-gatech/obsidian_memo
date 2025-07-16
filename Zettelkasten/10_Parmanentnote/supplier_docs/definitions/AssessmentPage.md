# 査定一覧ページ（/articles/assessment）

> [[AssessmentController]] `index`アクション & `app/views/assessment/index.html.erb` による描画

---

## 画面概要

- 仕入査定対象となる物件（Article）の一覧を表示する画面。
- 検索条件に応じて物件を絞り込み、物件名・受信日時・メールタイトル・仲介会社・返信状況などを一覧表示。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/assessment_controller.rb:4-34`
    - `@articles` : 検索・絞り込み済みの[[Article]]一覧（ページネーション付き）
    - `@q` : ransackによる検索オブジェクト
    - `@intermediary_companies` : [[IntermediaryCompany]]一覧
    - `@params_user` : サプライヤーユーザーの場合のみ、ユーザー名を格納

- **主なロジック:**
    - サプライヤーユーザーの場合、デフォルトで自分宛てメールのみを絞り込み
    - Articleモデルに対し、left_outer_joinsやscopes（active, on_sale, assessment）で絞り込み
    - ransackで検索条件を適用
    - includesで仲介会社・メール添付情報を事前ロード
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `render 'layouts/search'` (`app/views/assessment/index.html.erb:1`)
        - 検索条件入力フォーム（詳細は`app/views/layouts/_search.html.erb`）

- **物件一覧テーブル:**
    - `<% @articles.each do |article| %> ... </tr> <% end %>` (`index.html.erb:38-74`)
        - [[Article]] 一覧を1行ずつ表示。
        - 各カラムの対応：
            - **物件名:** `display_article_name(article.building_name, article.room_number, article.floor)` (`index.html.erb:46`)
                - [[display_article_name]]: `app/helpers/articles_helper.rb:105` で定義。物件名＋号室/階を整形表示。
            - **受信日時:** `article&.attachment&.supplier_mail&.received_at&.strftime('%-m/%-d %-H:%M')` (`index.html.erb:50`)
            - **タイトル:** `article.subject_from_intermediary_email` (`index.html.erb:52`)
                - [[subject_from_intermediary_email]]: `app/models/article.rb:1104` で定義。メールタイトルを省略表示。
            - **仲介会社:** `article.intermediary_company&.name_with_branch` (`index.html.erb:55`)
            - **From:** `article&.attachment&.supplier_mail&.from` (`index.html.erb:56`)
            - **返信状況:** `article.unnecessary_to_reply?`/`article.email_replied_at` (`index.html.erb:59-64`)
                - 「査定対象外」「済（返信日）」などを表示。

- **ページネーション:**
    - `paginate @articles` (`index.html.erb:32`)

- **ゴミ箱一覧リンク:**
    - `link_to 'ゴミ箱一覧を見る', articles_deleted_index_path, ...` (`index.html.erb:29`)

---

## 関連リンク
- [[AssessmentController]]
- [[Article]]
- [[IntermediaryCompany]]
- [[display_article_name]]
- [[subject_from_intermediary_email]]

---

## 参考ファイル
- コントローラ: `app/controllers/assessment_controller.rb`
- モデル: `app/models/article.rb`
- ビュー: `app/views/assessment/index.html.erb`
- ヘルパー: `app/helpers/articles_helper.rb` 