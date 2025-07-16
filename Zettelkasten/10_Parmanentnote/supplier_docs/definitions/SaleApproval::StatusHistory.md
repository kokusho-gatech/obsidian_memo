# SaleApproval::StatusHistory

## 役割
販売稟議のステータス履歴を管理するモデル。

## 主なリレーション
- belongs_to: [[SaleApproval]]
- belongs_to: [[User]]（actor）
- has_one: [[SaleApproval::StatusHistory::Comment]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| sale_approval_id | integer | 販売稟議ID（sale_approvalへの外部キー） |
| actor_id | integer | 操作ユーザーID（userへの外部キー） |
| status | integer | ステータス |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sale_approval_status_histories テーブル定義
- モデル: app/models/sale_approval/status_history.rb 