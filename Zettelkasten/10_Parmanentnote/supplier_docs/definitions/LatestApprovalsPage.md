# 仕入稟議一覧ページ（/articles/latest_approvals）

> [[Articles__LatestApprovalsController]] `index`アクション & `app/views/articles/latest_approvals/index.html.erb` による描画

---

## 画面概要

- 仕入稟議（Approval）を一覧表示する画面。
- 物件名・稟議ステータス・バイヤー担当者・申請者・申請コメント・申請日時などを表示。
- 検索フォームで絞り込みが可能。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/latest_approvals_controller.rb:5-13`
    - `@index_form` : [[Article__LatestApproval__IndexForm]]（検索条件を保持）
    - `@latest_approvals` : 検索・絞り込み済みの[[Approval]]一覧（ページネーション付き）

- **主なロジック:**
    - 検索条件を受け取り、callで絞り込み
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `form_with model: @index_form, ...` (`index.html.erb:5`)
- **一覧テーブル:**
    - `<%= render Article::LatestApproval::ListRowComponent.new(approval:) %>` (`index.html.erb:90`)
        - 各カラムはListRowComponentで描画
- **ページネーション:**
    - `paginate @latest_approvals` (`index.html.erb:38`)

---

## 関連リンク
- [[Articles__LatestApprovalsController]]
- [[Approval]]
- [[Article__LatestApproval__IndexForm]]
- [[Article__LatestApproval__ListRowComponent]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/latest_approvals_controller.rb`
- モデル: `app/models/approval.rb`, `app/models/article/latest_approval/index_form.rb`
- ビュー: `app/views/articles/latest_approvals/index.html.erb`
- コンポーネント: `app/components/article/latest_approval/list_row_component.rb` など 