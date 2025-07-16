# PriorValuation

## 役割
事前評価を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[User]]
- has_many: [[PriorValuationResult]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| evaluated_at | datetime | 評価日時 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: prior_valuations テーブル定義
- モデル: app/models/prior_valuation.rb 