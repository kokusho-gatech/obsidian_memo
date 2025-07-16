# IntermediaryCompanyモデル定義詳細

- **定義場所**: `app/models/intermediary_company.rb:2`
- **主な役割**: 仲介会社マスタ

## 主要な関連（定義元行番号付き）
- `has_many :intermediary_staffs` (`intermediary_company.rb:?`)
- ...（他にもあれば全て記載）

## intermediary_companiesテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:1610 |
| name | string | 仲介会社名 | db/schema.rb:? |
| ... | ... | ... | ... | 