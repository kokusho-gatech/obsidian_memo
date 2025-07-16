# Articleモデル定義詳細

- **定義場所**: `app/models/article.rb:8`
- **主な役割**: 物件情報を管理

## 主要な関連（定義元行番号付き）
- `belongs_to :building` (`article.rb:19`)
- `has_many :comments, dependent: :destroy` (`article.rb:20`)
- `has_many :approvals` (`article.rb:21`)
- `has_one :target_approval, ...` (`article.rb:22`)
- `has_one :payment_request` (`article.rb:23`)
- `has_one :attachment, dependent: :destroy` (`article.rb:24`)
- `has_one :supplier_mail, through: :attachment` (`article.rb:25`)
- `belongs_to :creator, class_name: 'User'` (`article.rb:26`)
- `belongs_to :user` (`article.rb:27`)
- `has_many :valuations, inverse_of: :article` (`article.rb:28`)
- ...（他にも多数。全て記載）

## articlesテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:288 |
| building_name | text | 建物名 | db/schema.rb:289 |
| zip | string | 郵便番号 | db/schema.rb:290 |
| prefecture | text | 住所１ | db/schema.rb:291 |
| ... | ... | ... | ... |
| created_at | datetime | null: false | db/schema.rb:312 |
| updated_at | datetime | null: false | db/schema.rb:313 |
| ... | ... | ... | ... | 