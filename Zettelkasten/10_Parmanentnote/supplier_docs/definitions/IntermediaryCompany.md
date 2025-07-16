# IntermediaryCompany

## 役割
仲介会社マスタを管理するモデル。

## 主なリレーション
- has_many: [[IntermediaryStaff]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | 仲介会社名（null: false） |
| user_id | integer | GA担当者（userへの外部キー） |
| monthly_handing_number | integer | 1ヶ月の取り扱い件数 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: intermediary_companies テーブル定義
- モデル: app/models/intermediary_company.rb 