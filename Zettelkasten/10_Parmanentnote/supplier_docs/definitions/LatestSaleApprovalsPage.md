# 販売稟議一覧ページ（/articles/latest_sale_approvals）

> [[Articles__LatestSaleApprovalsController]] `index`アクション & `app/views/articles/latest_sale_approvals/index.html.erb` による描画

---

## 画面概要

- 販売稟議（SaleApproval）を一覧表示する画面。
- 物件名・販売月・稟議ステータス・申請者・申請コメント・申請日時などを表示。
- 検索フォームで絞り込みが可能。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/latest_sale_approvals_controller.rb:5-13`
    - `@index_form` : [[Article__LatestSaleApproval__IndexForm]]（検索条件を保持）
    - `@latest_sale_approvals` : 検索・絞り込み済みの[[SaleApproval]]一覧（ページネーション付き）

- **主なロジック:**
    - 検索条件を受け取り、callで絞り込み
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `form_with model: @index_form, ...` (`index.html.erb:5`)
- **一覧テーブル:**
    - `<%= render Article::LatestSaleApproval::ListRowComponent.new(sale_approval:) %>` (`index.html.erb:90`)
        - 各カラムはListRowComponentで描画
- **ページネーション:**
    - `paginate @latest_sale_approvals` (`index.html.erb:38`)

---

## 関連リンク
- [[Articles__LatestSaleApprovalsController]]
- [[SaleApproval]]
- [[Article__LatestSaleApproval__IndexForm]]
- [[Article__LatestSaleApproval__ListRowComponent]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/latest_sale_approvals_controller.rb`
- モデル: `app/models/sale_approval.rb`, `app/models/article/latest_sale_approval/index_form.rb`
- ビュー: `app/views/articles/latest_sale_approvals/index.html.erb`
- コンポーネント: `app/components/article/latest_sale_approval/list_row_component.rb` など 