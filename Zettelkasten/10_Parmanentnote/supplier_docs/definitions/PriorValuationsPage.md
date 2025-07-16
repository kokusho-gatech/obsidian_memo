# 仕入評価一覧ページ（/articles/prior_valuations）

> [[Articles__PriorValuationsController]] `index`アクション & `app/views/articles/prior_valuations/index.html.erb` による描画

---

## 画面概要

- 物件ごとの仕入評価（PriorValuation）を一覧表示する画面。
- 物件名・回答ステータス・仕入担当・依頼日・希望日・エリア・各銀行回答・備考などを表示。
- 検索フォームで絞り込みが可能。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/prior_valuations_controller.rb:4-10`
    - `@index_form` : [[PriorValuation__IndexForm]]（検索条件を保持）
    - `@prior_valuations` : 検索・絞り込み済みの[[PriorValuation]]一覧（ページネーション付き）

- **主なロジック:**
    - 検索条件を受け取り、callで絞り込み
    - ページネーション（kaminari）

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `render 'index_form', model: @index_form` (`index.html.erb:5`)
- **一覧テーブル:**
    - `<%= render PriorValuation::ListRowComponent.new(prior_valuation:) %>` (`index.html.erb:74`)
        - 各カラムはListRowComponentで描画
- **ページネーション:**
    - `paginate @prior_valuations` (`index.html.erb:22`)

---

## 関連リンク
- [[Articles__PriorValuationsController]]
- [[PriorValuation]]
- [[PriorValuation__IndexForm]]
- [[PriorValuation__ListRowComponent]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/prior_valuations_controller.rb`
- モデル: `app/models/prior_valuation.rb`, `app/models/prior_valuation/index_form.rb`
- ビュー: `app/views/articles/prior_valuations/index.html.erb`
- コンポーネント: `app/components/prior_valuation/list_row_component.rb` など 