# SaleApproval

## 役割
販売稟議を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- has_many: [[SaleApproval::StatusHistory]]
- has_one: [[SaleApproval::Detail]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| status | integer | 稟議ステータス |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sale_approvals テーブル定義
- モデル: app/models/sale_approval.rb 