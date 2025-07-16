# 仕入評価編集ページ（/articles/prior_valuations/:id/edit）

> [[Articles__PriorValuationsController]] `edit`アクション & `app/views/articles/prior_valuations/edit.html.erb` による描画

---

## 画面概要

- 物件ごとの仕入評価（PriorValuation）の詳細・編集画面。
- 物件情報、評価結果、他の仕入評価、過去の仕入評価、銀行ごとの回答フォームなどを表示・編集。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/prior_valuations_controller.rb:12-38`
    - `@prior_valuation` : 編集対象の[[PriorValuation]]
    - `@prior_valuation_results_form` : 銀行ごとの評価結果フォーム
    - `@other_prior_valuations` : 同物件の他の仕入評価
    - `@previous_prior_valuations` : 同建物の過去仕入評価
    - `@is_prior_valuation_editable` : 編集可否フラグ

- **主なロジック:**
    - PriorValuationの取得・権限チェック
    - 各種フォーム・表示用インスタンス変数のセット
    - ページ遷移やリダイレクト制御

---

## 2. UIとデータの対応

- **物件名:** `@prior_valuation.article.building_name`（リンク付き、`edit.html.erb:5`）
- **評価結果フォーム:** `@prior_valuation_results_form`（`edit.html.erb:15-70`）
- **他の仕入評価:** `@other_prior_valuations`（`edit.html.erb:10`）
- **過去の仕入評価:** `@previous_prior_valuations`（`edit.html.erb:11`）
- **保存・回答ボタン:** `form.submit`/`link_to '回答'`（`edit.html.erb:65-72`）

---

## 関連リンク
- [[Articles__PriorValuationsController]]
- [[PriorValuation]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/prior_valuations_controller.rb`
- モデル: `app/models/prior_valuation.rb`
 