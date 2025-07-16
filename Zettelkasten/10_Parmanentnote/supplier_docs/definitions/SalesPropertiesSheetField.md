# SalesPropertiesSheetField

## 役割
販売物件管理スプレッドシート項目を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| field_name | string | 項目名 |
| value | text | 項目値 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_properties_sheet_fields テーブル定義
- モデル: app/models/sales_properties_sheet_field.rb 