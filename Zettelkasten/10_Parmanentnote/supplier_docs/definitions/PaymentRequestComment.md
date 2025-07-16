# PaymentRequestCommentモデル定義詳細

- **定義場所**: `app/models/payment_request_comment.rb:2`
- **主な役割**: 支払い依頼のコメント管理

## 主要な関連（定義元行番号付き）
- `belongs_to :payment_request` (`payment_request_comment.rb:3`)

## payment_request_commentsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:1957 |
| payment_request_id | integer | 支払い依頼ID | db/schema.rb:? |
| ... | ... | ... | ... | 