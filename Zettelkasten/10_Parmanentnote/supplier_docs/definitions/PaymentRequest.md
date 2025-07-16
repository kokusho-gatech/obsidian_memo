# PaymentRequestモデル定義詳細

- **定義場所**: `app/models/payment_request.rb:2`
- **主な役割**: 支払い依頼管理

## 主要な関連（定義元行番号付き）
- `belongs_to :article` (`payment_request.rb:36`)
- `belongs_to :user` (`payment_request.rb:37`)
- `has_many :payment_request_comments` (`payment_request.rb:38`)

## payment_requestsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:1968 |
| article_id | integer | 物件ID | db/schema.rb:? |
| user_id | integer | ユーザーID | db/schema.rb:? |
| ... | ... | ... | ... | 