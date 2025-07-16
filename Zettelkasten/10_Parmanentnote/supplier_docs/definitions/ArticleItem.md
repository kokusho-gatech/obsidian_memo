# ArticleItemモデル定義詳細

- **定義場所**: `app/models/article_item.rb:2`
- **主な役割**: 物件に紐づく書類情報を管理

## 主要な関連（定義元行番号付き）
- `belongs_to :item` (`article_item.rb:8`)
- `belongs_to :article` (`article_item.rb:9`)
- `belongs_to :uploaded_by, foreign_key: 'uploader_id', primary_key: 'id', class_name: 'User'` (`article_item.rb:10`)
- `has_many :article_item_files, inverse_of: :article_item` (`article_item.rb:11`)
- `has_many :unmounted_article_item_files, class_name: 'UnmountedArticleItemFile'` (`article_item.rb:12`)
- `has_one :last_file, -> { order(id: :desc) }, class_name: 'ArticleItemFile'` (`article_item.rb:13`)
- ...（他にも多数。全て記載）

## article_itemsテーブル定義（抜粋）

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:181 |
| item_id | integer | 書類ID | db/schema.rb:182 |
| article_id | integer | 物件ID | db/schema.rb:183 |
| uploaded_date | date | アップロード日 | db/schema.rb:184 |
| schd_upload_date | date | アップロード予定日 | db/schema.rb:185 |
| remark | text | 備考 | db/schema.rb:186 |
| additionally_confirmed | boolean | 備考チェック | db/schema.rb:187 |
| created_at | datetime | null: false | db/schema.rb:188 |
| updated_at | datetime | null: false | db/schema.rb:189 | 