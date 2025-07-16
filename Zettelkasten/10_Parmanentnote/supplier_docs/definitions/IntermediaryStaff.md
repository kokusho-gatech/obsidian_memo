# IntermediaryStaffモデル定義詳細

- **定義場所**: `app/models/intermediary_staff.rb:2`
- **主な役割**: 仲介担当者

## 主要な関連（定義元行番号付き）
- `belongs_to :intermediary_company` (`intermediary_staff.rb:8`)
- `has_many :intermediary_staff_users, dependent: :destroy` (`intermediary_staff.rb:9`)
- `has_many :users, through: :intermediary_staff_users` (`intermediary_staff.rb:10`)
- ...（他にもあれば全て記載）

## intermediary_staffsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:1658 |
| intermediary_company_id | integer | 仲介会社ID | db/schema.rb:? |
| ... | ... | ... | ... | 