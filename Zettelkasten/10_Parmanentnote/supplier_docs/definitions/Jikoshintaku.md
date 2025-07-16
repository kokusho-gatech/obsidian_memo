# Jikoshintaku

## 役割
自己信託マスタを管理するモデル。

## 主なリレーション
- has_many: [[JikoshintakuArticle]]
- has_many: [[Article]]（through: :jikoshintaku_articles）

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | 自己信託名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: jikoshintakus テーブル定義
- モデル: app/models/jikoshintaku.rb 