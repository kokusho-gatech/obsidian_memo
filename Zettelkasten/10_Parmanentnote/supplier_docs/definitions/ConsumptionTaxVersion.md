---
tags:
  - definition
  - model
  - supplier
  - parmanentnote
---

# ConsumptionTaxVersion

## 役割
消費税計算履歴を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| version | integer | バージョン番号 |
| tax_amount | integer | 消費税額 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: consumption_tax_versions テーブル定義
- モデル: app/models/consumption_tax_version.rb 