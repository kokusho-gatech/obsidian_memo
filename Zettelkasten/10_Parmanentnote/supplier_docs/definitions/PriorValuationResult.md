# PriorValuationResult

## 役割
事前評価結果を管理するモデル。

## 主なリレーション
- belongs_to: [[PriorValuation]]
- belongs_to: [[Bank]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| prior_valuation_id | integer | 事前評価ID（prior_valuationへの外部キー） |
| bank_id | integer | 銀行ID（bankへの外部キー） |
| result | text | 評価結果 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: prior_valuation_results テーブル定義
- モデル: app/models/prior_valuation_result.rb 