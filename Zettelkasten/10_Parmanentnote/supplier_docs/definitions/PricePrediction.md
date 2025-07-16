# PricePrediction

## 役割
価格推定結果を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| predicted_price | integer | 推定価格 |
| predicted_at | datetime | 推定日時 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: price_predictions テーブル定義
- モデル: app/models/price_prediction.rb 