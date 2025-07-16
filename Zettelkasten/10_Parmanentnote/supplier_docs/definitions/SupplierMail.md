# SupplierMail

## 役割
査定メール管理を行うモデル。

## 主なリレーション
- belongs_to: [[User]]（contact_person）
- belongs_to: [[IntermediaryCompany]]
- belongs_to: [[IntermediaryStaff]]
- belongs_to: [[IntermediaryDomain]]
- has_many: [[Attachment]]
- has_many: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| contact_person_id | integer | 査定担当者ID（userへの外部キー） |
| intermediary_company_id | integer | 仲介会社ID（intermediary_companyへの外部キー） |
| intermediary_staff_id | integer | 仲介担当者ID（intermediary_staffへの外部キー） |
| intermediary_domain_id | integer | 仲介ドメインID（intermediary_domainへの外部キー） |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: supplier_mails テーブル定義
- モデル: app/models/supplier_mail.rb 