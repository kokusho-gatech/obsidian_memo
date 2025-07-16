# IntermediaryDomain

## 役割
仲介会社ドメインを管理するモデル。

## 主なリレーション
- belongs_to: [[IntermediaryCompany]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| intermediary_company_id | integer | 仲介会社ID（intermediary_companyへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| domain | string | ドメイン名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: intermediary_domains テーブル定義
- モデル: app/models/intermediary_domain.rb 