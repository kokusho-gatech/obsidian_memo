# IntermediaryStaffUser

## 役割
仲介担当者とユーザーの中間テーブル。

## 主なリレーション
- belongs_to: [[IntermediaryStaff]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| intermediary_staff_id | integer | 仲介担当者ID（intermediary_staffへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: intermediary_staff_users テーブル定義
- モデル: app/models/intermediary_staff_user.rb 