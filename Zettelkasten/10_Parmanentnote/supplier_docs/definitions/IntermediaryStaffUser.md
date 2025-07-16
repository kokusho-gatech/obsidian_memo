# IntermediaryStaffUserモデル定義詳細

- **定義場所**: `app/models/intermediary_staff_user.rb:2`
- **主な役割**: 仲介担当者とユーザーの中間テーブル

## 主要な関連（定義元行番号付き）
- `belongs_to :intermediary_staff` (`intermediary_staff_user.rb:3`)
- `belongs_to :user` (`intermediary_staff_user.rb:4`)

## intermediary_staff_usersテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:1648 |
| intermediary_staff_id | integer | 仲介担当者ID | db/schema.rb:? |
| user_id | integer | ユーザーID | db/schema.rb:? |
| ... | ... | ... | ... | 