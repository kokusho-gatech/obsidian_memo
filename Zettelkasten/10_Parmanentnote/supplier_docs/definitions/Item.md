# Item

## 役割
書類種別マスタを管理するモデル。

## 主なリレーション
- has_many: [[ArticleItem]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | 書類名 |
| description | text | 書類説明 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: items テーブル定義
- モデル: app/models/item.rb 