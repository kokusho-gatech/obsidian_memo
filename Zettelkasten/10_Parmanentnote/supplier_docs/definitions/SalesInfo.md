# SalesInfo

## 役割
発表詳細を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| info | text | 詳細情報 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: sales_infos テーブル定義
- モデル: app/models/sales_info.rb 