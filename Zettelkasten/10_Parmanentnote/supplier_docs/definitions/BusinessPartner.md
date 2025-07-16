# BusinessPartner

## 役割
ビジネスパートナーを管理するモデル。

## 主なリレーション
- has_many: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | ビジネスパートナー名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: business_partners テーブル定義
- モデル: app/models/business_partner.rb 