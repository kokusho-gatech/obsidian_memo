# PaymentRequestComment

## 役割
支払い依頼のコメントを管理するモデル。

## 主なリレーション
- belongs_to: [[PaymentRequest]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| payment_request_id | integer | 支払い依頼ID（payment_requestへの外部キー） |
| comment | text | コメント内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: payment_request_comments テーブル定義
- モデル: app/models/payment_request_comment.rb 