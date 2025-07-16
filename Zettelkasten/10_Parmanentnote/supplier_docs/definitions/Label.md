# Label

## 役割
ラベルを管理するモデル。

## 主なリレーション
（特になし）

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| name | string | ラベル名 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: labels テーブル定義
- モデル: app/models/label.rb 