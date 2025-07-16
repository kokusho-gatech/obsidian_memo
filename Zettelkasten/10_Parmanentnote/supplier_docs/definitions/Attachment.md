# Attachmentモデル定義詳細

- **定義場所**: `app/models/attachment.rb:2`
- **主な役割**: メール添付ファイル管理

## 主要な関連（定義元行番号付き）
- `belongs_to :supplier_mail` (`attachment.rb:?`)
- `belongs_to :article` (`attachment.rb:?`)

## attachmentsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:698 |
| supplier_mail_id | integer | 査定メールID | db/schema.rb:? |
| article_id | integer | 物件ID | db/schema.rb:? |
| ... | ... | ... | ... | 