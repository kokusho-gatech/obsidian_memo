# Janitor

## 役割
建物管理員を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| name | string | 管理員名 |
| phone | string | 電話番号 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: janitors テーブル定義
- モデル: app/models/janitor.rb 