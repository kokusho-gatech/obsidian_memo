# SaleManagementInfo

## 役割
発表管理を行うモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[Bank]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| bank_id | integer | 銀行ID（bankへの外部キー） |
| info | text | 管理情報 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sale_management_infos テーブル定義
- モデル: app/models/sale_management_info.rb 