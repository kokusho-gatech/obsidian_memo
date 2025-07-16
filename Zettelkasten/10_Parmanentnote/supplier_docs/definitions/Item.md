# Itemモデル定義詳細

- **定義場所**: `app/models/item.rb:4`
- **主な役割**: 書類種別マスタ

## 主要な関連（定義元行番号付き）
- `has_many :article_items` (`item.rb:?`)
- ...（他にもあれば全て記載）

## itemsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:1671 |
| name | string | 書類名 | db/schema.rb:? |
| ... | ... | ... | ... | 