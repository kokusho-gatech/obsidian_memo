# SalesContractField

## 役割
契約書関連項目を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[SalesContractTemplate]]
- has_many: [[SalesContractFile]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| sales_contract_template_id | integer | 契約書テンプレートID（sales_contract_templateへの外部キー） |
| has_accessory_building | boolean | 付属建物の有無（default: false） |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_contract_fields テーブル定義
- モデル: app/models/sales_contract_field.rb 