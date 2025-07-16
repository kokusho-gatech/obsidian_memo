# PaymentRequest

## 役割
支払い依頼を管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[User]]
- has_many: [[PaymentRequestComment]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| amount | integer | 支払い金額 |
| status | integer | 支払いステータス |
| requested_at | datetime | 依頼日時 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: payment_requests テーブル定義
- モデル: app/models/payment_request.rb 