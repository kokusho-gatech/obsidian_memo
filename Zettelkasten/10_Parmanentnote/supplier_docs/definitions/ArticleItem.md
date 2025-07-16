# ArticleItem

## 役割
物件に紐づく書類情報を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[Item]]
- has_many: [[ArticleItemFile]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | integer | 主キー |
| item_id | integer | 書類ID（itemへの外部キー） |
| article_id | integer | 物件ID（articleへの外部キー） |
| uploaded_date | date | アップロード日 |
| schd_upload_date | date | アップロード予定日 |
| remark | text | 備考 |
| additionally_confirmed | boolean | 備考チェック |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: article_items テーブル定義
- モデル: app/models/article_item.rb 