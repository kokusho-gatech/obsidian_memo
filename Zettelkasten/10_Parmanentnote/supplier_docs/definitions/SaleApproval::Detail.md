# SaleApproval::Detail

## 役割
販売稟議の詳細情報を管理するモデル。

## 主なリレーション
- belongs_to: [[SaleApproval]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| sale_approval_id | integer | 販売稟議ID（sale_approvalへの外部キー） |
| detail | text | 詳細内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sale_approval_details テーブル定義
- モデル: app/models/sale_approval/detail.rb 