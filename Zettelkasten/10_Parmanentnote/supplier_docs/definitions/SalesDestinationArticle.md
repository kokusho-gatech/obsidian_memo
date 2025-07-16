# SalesDestinationArticle

## 役割
卸先事業と物件の中間テーブル。

## 主なリレーション
- belongs_to: [[SalesDestination]]
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| sales_destination_id | integer | 卸先事業ID（sales_destinationへの外部キー） |
| article_id | integer | 物件ID（articleへの外部キー） |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_destination_articles テーブル定義
- モデル: app/models/sales_destination_article.rb 