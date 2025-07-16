# SalesContractTemplate

## 役割
契約書テンプレートを管理するモデル。

## 主なリレーション
- has_many: [[SalesContractField]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | テンプレート名 |
| description | text | テンプレート説明 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_contract_templates テーブル定義
- モデル: app/models/sales_contract_template.rb 