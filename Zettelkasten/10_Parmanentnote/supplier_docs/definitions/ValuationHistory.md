# ValuationHistory

## 役割
銀行評価履歴を管理するモデル。

## 主なリレーション
- belongs_to: [[Valuation]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| valuation_id | integer | 銀行評価ID（valuationへの外部キー） |
| history | text | 評価履歴内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: valuation_histories テーブル定義
- モデル: app/models/valuation_history.rb 