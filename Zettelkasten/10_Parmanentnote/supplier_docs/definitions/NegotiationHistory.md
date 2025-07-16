# NegotiationHistory

## 役割
交渉履歴を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| content | text | 交渉内容 |
| status | integer | 交渉ステータス |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: negotiation_histories テーブル定義
- モデル: app/models/negotiation_history.rb 