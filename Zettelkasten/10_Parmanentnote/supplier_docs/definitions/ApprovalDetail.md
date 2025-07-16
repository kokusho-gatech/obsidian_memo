# ApprovalDetail

## 役割
稟議の詳細情報を管理するモデル。

## 主なリレーション
- belongs_to: [[Approval]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | integer | 主キー |
| approval_id | integer | 稟議ID（approvalへの外部キー） |
| detail | text | 詳細内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: approvals_detail テーブル定義
- モデル: app/models/approval_detail.rb 