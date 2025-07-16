# SaleApproval::StatusHistory::Comment

## 役割
販売稟議ステータス履歴のコメントを管理するモデル。

## 主なリレーション
- belongs_to: [[SaleApproval::StatusHistory]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| sale_approval_status_history_id | integer | ステータス履歴ID（sale_approval_status_historyへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| comment | text | コメント内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sale_approval_status_history_comments テーブル定義
- モデル: app/models/sale_approval/status_history/comment.rb 