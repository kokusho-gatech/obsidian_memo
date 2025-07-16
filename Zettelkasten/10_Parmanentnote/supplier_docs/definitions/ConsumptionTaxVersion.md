# ConsumptionTaxVersionモデル定義詳細

- **定義場所**: `app/models/consumption_tax_version.rb:2`
- **主な役割**: 消費税計算履歴

## 主要な関連（定義元行番号付き）
- `belongs_to :article` (`consumption_tax_version.rb:9`)
- `belongs_to :user` (`consumption_tax_version.rb:10`)

## consumption_tax_versionsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:920 |
| article_id | integer | 物件ID | db/schema.rb:? |
| user_id | integer | ユーザーID | db/schema.rb:? |
| ... | ... | ... | ... | 