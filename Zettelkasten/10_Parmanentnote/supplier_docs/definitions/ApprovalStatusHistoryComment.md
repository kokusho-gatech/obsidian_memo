# ApprovalStatusHistoryComment

## 役割
稟議ステータス履歴のコメントを管理するモデル。

## 主なリレーション
- belongs_to: [[ApprovalStatusHistory]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | integer | 主キー |
| approval_status_history_id | integer | ステータス履歴ID（approval_status_historyへの外部キー） |
| user_id | integer | ユーザーID |
| comment | text | コメント内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: approval_status_history_comments テーブル定義
- モデル: app/models/approval_status_history_comment.rb 