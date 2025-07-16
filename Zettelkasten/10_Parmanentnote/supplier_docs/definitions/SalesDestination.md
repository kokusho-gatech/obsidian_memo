# SalesDestination

## 役割
卸先事業マスタを管理するモデル。

## 主なリレーション
- has_many: [[SalesDestinationArticle]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | 卸先事業名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_destinations テーブル定義
- モデル: app/models/sales_destination.rb 