# Prefecture

## 役割
都道府県マスタを管理するモデル。

## 主なリレーション
- has_many: [[IntermediaryCompany]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | 都道府県名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: prefectures テーブル定義
- モデル: app/models/prefecture.rb 