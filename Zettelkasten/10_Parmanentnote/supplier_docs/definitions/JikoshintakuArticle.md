# JikoshintakuArticle

## 役割
自己信託と物件の中間テーブル。

## 主なリレーション
- belongs_to: [[Jikoshintaku]]
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| jikoshintaku_id | integer | 自己信託ID（jikoshintakuへの外部キー） |
| article_id | integer | 物件ID（articleへの外部キー） |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: jikoshintaku_articles テーブル定義
- モデル: app/models/jikoshintaku_article.rb 