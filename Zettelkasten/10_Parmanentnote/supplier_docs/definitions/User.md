# Userモデル定義詳細

- **定義場所**: `app/models/user.rb:5`
- **主な役割**: ユーザー情報を管理

## 主要な関連（定義元行番号付き）
- `belongs_to :business_partner` (`user.rb:104`)
- `has_one :setting, class_name: 'Users::Setting'` (`user.rb:105`)
- `has_many :supplier_mails` (`user.rb:106`)
- `has_many :intermediaries` (`user.rb:107`)
- `has_many :intermediary_companies` (`user.rb:108`)
- `has_many :intermediary_domains` (`user.rb:109`)
- `has_many :intermediary_staffs` (`user.rb:110`)
- `has_many :articles` (`user.rb:111`)
- `has_many :incomplete_documents, through: :articles` (`user.rb:112`)
- `has_many :approvals` (`user.rb:113`)

## usersテーブル定義

| カラム名 | データ型 | 備考 | 定義場所 |
|---|---|---|---|
| id | bigint | 主キー | db/schema.rb:3195 |
| email | string | null: false, default: "", コメント: メールアドレス | db/schema.rb:3196 |
| encrypted_password | string | null: false, default: "", コメント: 暗号化パスワード | db/schema.rb:3197 |
| sign_in_count | integer | null: false, default: 0, コメント: サインイン回数 | db/schema.rb:3198 |
| current_sign_in_at | datetime | コメント: 現サインイン日時 | db/schema.rb:3199 |
| last_sign_in_at | datetime | コメント: 前回サインイン日時 | db/schema.rb:3200 |
| current_sign_in_ip | inet | コメント: 現サインインIP | db/schema.rb:3201 |
| last_sign_in_ip | inet | コメント: 前回サインインIP | db/schema.rb:3202 |
| name | string | コメント: 名前 | db/schema.rb:3203 |
| created_at | datetime | null: false | db/schema.rb:3204 |
| updated_at | datetime | null: false | db/schema.rb:3205 |
| type | string | null: false, default: "Salesperson", コメント: タイプ | db/schema.rb:3206 |
| chatwork_id | integer | コメント: チャットワークID | db/schema.rb:3207 |
| department_id | integer | コメント: 使用していない | db/schema.rb:3208 |
| mobile_phone | string | コメント: 携帯電話番号 | db/schema.rb:3209 |
| authority | text[] | null: false, default: [], コメント: 権限管理用カラム | db/schema.rb:3210 |
| business_partner_id | integer | コメント: ビジネスパートナーID | db/schema.rb:3211 |
| leave | boolean | null: false, default: false, コメント: 退職フラグ | db/schema.rb:3212 | 