# Building

## 役割
建物マスタを管理するモデル。

## 主なリレーション
- has_many: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | 建物名 |
| address | string | 住所 |
| built_year | integer | 築年 |
| structure | string | 構造 |
| total_rooms | integer | 総戸数 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: buildings テーブル定義
- モデル: app/models/building.rb 