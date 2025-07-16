# Approvalモデル定義詳細

- **定義場所**: `app/models/approval.rb:2`
- **主な役割**: 稟議申請管理

## 主要な関連（定義元行番号付き）
- `belongs_to :article` (`approval.rb:?`)
- `belongs_to :user` (`approval.rb:?`)
- `has_one :approval_detail` (`approval.rb:?`)
- `has_many :approval_status_histories` (`approval.rb:?`)
- ...（他にもあれば全て記載）

## approvalsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:119 |
| article_id | integer | article_id | db/schema.rb:120 |
| user_id | integer | user_id | db/schema.rb:121 |
| ... | ... | ... | ... | 