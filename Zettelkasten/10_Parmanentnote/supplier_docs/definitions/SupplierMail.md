# SupplierMailモデル定義詳細

- **定義場所**: `app/models/supplier_mail.rb:2`
- **主な役割**: 査定メール管理

## 主要な関連（定義元行番号付き）
- `belongs_to :contact_person, class_name: 'User'` (`supplier_mail.rb:5`)
- `belongs_to :intermediary_company` (`supplier_mail.rb:6`)
- `belongs_to :intermediary_staff` (`supplier_mail.rb:7`)
- `belongs_to :intermediary_domain` (`supplier_mail.rb:8`)
- `has_many :attachments` (`supplier_mail.rb:9`)
- `has_many :articles` (`supplier_mail.rb:10`)

## supplier_mailsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:? |
| contact_person_id | integer | 査定担当者ID | db/schema.rb:? |
| intermediary_company_id | integer | 仲介会社ID | db/schema.rb:? |
| ... | ... | ... | ... | 