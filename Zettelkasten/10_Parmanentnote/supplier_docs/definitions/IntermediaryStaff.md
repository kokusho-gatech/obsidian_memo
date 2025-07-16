# IntermediaryStaff

## 役割
仲介担当者を管理するモデル。

## 主なリレーション
- belongs_to: [[IntermediaryCompany]]
- has_many: [[IntermediaryStaffUser]]
- has_many: [[User]]（through: :intermediary_staff_users）

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| intermediary_company_id | integer | 仲介会社ID（intermediary_companyへの外部キー） |
| name | string | 担当者名 |
| email | string | メールアドレス |
| phone | string | 電話番号 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: intermediary_staffs テーブル定義
- モデル: app/models/intermediary_staff.rb 