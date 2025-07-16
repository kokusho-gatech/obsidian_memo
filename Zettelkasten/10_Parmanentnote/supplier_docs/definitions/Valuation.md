# Valuation

## 役割
銀行評価を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[Bank]]
- has_many: [[ValuationHistory]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| bank_id | integer | 銀行ID（bankへの外部キー） |
| evaluated_at | datetime | 評価日時 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: valuations テーブル定義
- モデル: app/models/valuation.rb 