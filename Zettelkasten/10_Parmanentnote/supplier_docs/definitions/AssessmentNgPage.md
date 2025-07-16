# 査定NG一覧ページ（/articles/assessment_ng）

> [[Articles__AssessmentNgController]] `index`アクション & `app/views/articles/assessment_ng/index.html.erb` による描画

---

## 画面概要

- 査定NG（仕入対象外）となった物件（Article）の一覧を表示する画面。
- 物件名・受信日時・バイヤー担当・タイトル・仲介会社・返信日時・NG理由などを一覧表示。
- 検索フォームで物件名・仲介会社・バイヤー担当者による絞り込みが可能。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/assessment_ng_controller.rb:5-11`
    - `@index_form` : [[Article__AssessmentNg__IndexForm]]（検索条件を保持）
    - `@articles` : 検索・絞り込み済みの[[Article]]一覧（ページネーション付き）

- **主なロジック:**
    - `@index_form = Article::AssessmentNg::IndexForm.new(params: index_form_permitted_params)`
        - 検索条件（物件名・仲介会社・バイヤー担当）を受け取り、callで絞り込み
    - Articleモデルに対し、deleted: false, unnecessary_to_reply: true で絞り込み
    - 関連情報（user, intermediary_company, assessment_ng_reasons, attachment.supplier_mail）をpreload
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `render 'index_form', model: @index_form` (`app/views/articles/assessment_ng/index.html.erb:5`)
        - 検索条件入力フォーム（詳細は`app/views/articles/assessment_ng/_index_form.html.erb:1-32`）
        - 物件名・仲介会社・バイヤー担当で絞り込み

- **物件一覧テーブル:**
    - `<%= render Article::AssessmentNg::ListRowComponent.new(article:) %>` (`index.html.erb:61`)
        - 各行は[[Article__AssessmentNg__ListRowComponent]]で描画（`app/components/article/assessment_ng/list_row_component.rb:1-31`, `list_row_component.html.erb:1-26`）
        - 各カラムの対応：
            - **物件名:** `@article.building_name`（リンク付き）
            - **受信日時:** `supplier_mail_received_at`（attachment.supplier_mail.received_at）
            - **バイヤー担当:** `@article.user&.name`
            - **タイトル:** `@article.subject_from_intermediary_email`
            - **仲介会社:** `@article.intermediary_company&.name_with_branch` + `From: ...`
            - **返信日時:** `email_replied_at`（@article.email_replied_at）
            - **NG理由:** `assessment_ng_reasons`（@article.assessment_ng_reasons.map(&:reason_text).join(' / ')）

- **ページネーション:**
    - `paginate @articles` (`index.html.erb:20`)

---

## 関連リンク
- [[Articles__AssessmentNgController]]
- [[Article]]
- [[Article__AssessmentNg__IndexForm]]
- [[Article__AssessmentNg__ListRowComponent]]
- [[Article__AssessmentNgReason]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/assessment_ng_controller.rb`
- モデル: `app/models/article/assessment_ng/index_form.rb`, `app/models/article/assessment_ng_reason.rb`, `app/models/article.rb`
- ビュー: `app/views/articles/assessment_ng/index.html.erb`, `_index_form.html.erb`
- コンポーネント: `app/components/article/assessment_ng/list_row_component.rb`, `list_row_component.html.erb` 