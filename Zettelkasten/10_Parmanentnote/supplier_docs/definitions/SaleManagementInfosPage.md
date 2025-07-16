# 発表管理一覧ページ（/sale_management_infos）

> [[SaleManagementInfosController]] `index`アクション & `app/views/sale_management_infos/index.html.erb` による描画

---

## 画面概要

- 発表（販売）管理対象となる物件の一覧を表示する画面。
- 物件名・販売状況・担当者・進捗などを一覧表示。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/sale_management_infos_controller.rb`
    - `@sale_management_infos` : 一覧表示用の[[SaleManagementInfo]]コレクション

- **主なロジック:**
    - 検索・絞り込み・ページネーション（詳細はコントローラ実装参照）

---

## 2. UIとデータの対応

- **一覧テーブル:**
    - 物件名・販売状況・担当者・進捗など（カラム詳細はビュー参照）
- **ページネーション:**
    - `paginate @sale_management_infos`

---

## 関連リンク
- [[SaleManagementInfosController]]
- [[SaleManagementInfo]]

---

## 参考ファイル
- コントローラ: `app/controllers/sale_management_infos_controller.rb`
- モデル: `app/models/sale_management_info.rb`
- ビュー: `app/views/sale_management_infos/index.html.erb` 