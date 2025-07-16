# SalesContractFile

## 役割
契約書ファイルを管理するモデル。

## 主なリレーション
- belongs_to: [[SalesContractField]]
- has_many: [[DocusignFile]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| sales_contract_field_id | integer | 契約書関連項目ID（sales_contract_fieldへの外部キー） |
| file_name | string | ファイル名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_contract_files テーブル定義
- モデル: app/models/sales_contract_file.rb 