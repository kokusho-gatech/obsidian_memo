# DocusignFile

## 役割
DocuSignファイルを管理するモデル。

## 主なリレーション
- belongs_to: [[SalesContractFile]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| sales_contract_file_id | integer | 契約書ファイルID（sales_contract_fileへの外部キー） |
| file_name | string | ファイル名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: docusign_files テーブル定義
- モデル: app/models/docusign_file.rb 