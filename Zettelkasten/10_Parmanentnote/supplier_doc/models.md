# SUPPLIER by RENOSY モデルドキュメント

---

## [[User]]
### 役割
ユーザー情報・権限管理の中核モデル。各種認証・権限・担当物件・仲介会社など多様な関係を持つ。

### テーブル定義（例）
- name: string, null: false
- email: string, unique, null: false
- mobile_phone: string
- authority: array
- ...（他多数）

### バリデーション
- name: presence
- email: uniqueness, format
- mobile_phone: format
- authority: カスタムバリデーション

### アソシエーション
- belongs_to: [[BusinessPartner]]
- has_one: [[Users::Setting]]
- has_many: [[SupplierMail]], [[IntermediaryCompany]], [[IntermediaryDomain]], [[IntermediaryStaff]], [[Article]], [[Approval]] など

### 主要なメソッド
- `self.search(params)`: 検索条件でユーザーを絞り込む
- `has_auth?(auth_level)`: 指定権限を持つか判定
- `clear_gmail_authorization`: Gmail認証情報を削除
- ...（他多数）

---

## [[Article]]
### 役割
物件（記事）情報の中核モデル。多くの関連情報（査定、交渉、契約、ファイル等）を持つ。

### テーブル定義（例）
- building_id: integer, null: false
- user_id: integer, null: false
- ...（他多数）

### バリデーション
- Articles::OnUpdate::BaseValidator（更新時）

### アソシエーション
- belongs_to: [[Building]], [[User]], [[IntermediaryCompany]], [[IntermediaryStaff]], [[IntermediaryDomain]]
- has_many: [[Approval]], [[Valuation]], [[ArticleItem]], [[NegotiationHistory]], [[PriorValuation]], [[SaleApproval]], [[AssessmentNgReason]] など
- has_one: [[PaymentRequest]], [[OwnrInfo]], [[SaleManagementInfo]], [[ConsumptionTaxVersion]], [[SalesInfo]], [[Janitor]], [[DocumentProgress]], [[PurchaseContract]] など

### 主要なメソッド
- `address`: 住所文字列を返す
- `released?`: AGNT連携済みか判定
- `upload_article_item_files!`: ファイルアップロード処理
- ...（他多数）

---

## [[Approval]]
### 役割
仕入稟議の申請・承認フローを管理するモデル。

### テーブル定義（例）
- article_id: integer, null: false
- status: integer, enum
- ...

### バリデーション
- なし（主にenum・関連先の存在）

### アソシエーション
- belongs_to: [[Article]]
- has_one: [[ApprovalDetail]]
- has_many: [[ApprovalStatusHistory]]

### 主要なメソッド
- `change_approval?`: 変更稟議か判定
- `sendable?`: 送信可能な状態か判定
- `reviewing?`: レビュー中か判定
- ...

---

## [[Valuation]]
### 役割
銀行ごとの査定情報を管理。

### テーブル定義（例）
- article_id: integer, null: false
- bank_id: integer, null: false
- status: integer, enum
- price: integer
- ...

### バリデーション
- bank_id, status_changed_at: presence
- price: numericality
- bank_id+article_id: uniqueness

### アソシエーション
- belongs_to: [[Article]]
- belongs_to: [[Bank]]
- has_many: [[ValuationHistory]]
- has_one: [[ValuationHistory]]（last_valuation_history）

### 主要なメソッド
- `self.bulk_create!(article)`: 銀行ごとに査定レコードを一括生成

---

## [[PriorValuation]]
### 役割
仕入評価（銀行評価前の査定）を管理。

### テーブル定義（例）
- article_id: integer, null: false
- user_id: integer, null: false
- status: integer, enum
- ...

### バリデーション
- article_id, user_id, status, 住所・面積等: presence
- サブリース時はsublease_company等: presence

### アソシエーション
- belongs_to: [[Article]]
- belongs_to: [[User]]
- has_many: [[PriorValuation::Result]]
- has_one: [[PriorValuation::Result]]（jaccs_result, orix_result）

### 主要なメソッド
- `self.area_eq(area)`: 地域ごとに絞り込み
- `answerable?`: 回答可能か判定

---

## [[SalesContractField]]
### 役割
売買契約書の各種フィールド・契約情報を管理。

### テーブル定義（例）
- article_id: integer, null: false
- sales_contract_template_id: integer, null: false
- status: integer, enum
- ...

### バリデーション
- 各種数値項目: numericality
- ステータス: カスタムバリデーション

### アソシエーション
- belongs_to: [[Article]]
- belongs_to: [[SalesContractTemplate]]
- has_many: [[SalesContractFile]]
- has_many: [[DocusignInfo]]

### 主要なメソッド
- `zip`: 契約書類一式をzip化
- `copy!`: 他記事からフィールドをコピー

---

## [[SalesContractFile]]
### 役割
売買契約書・重要事項説明書などのPDFファイル生成・管理。

### テーブル定義（例）
- sales_contract_field_id: integer, null: false
- type: string, enum
- ...

### バリデーション
- なし

### アソシエーション
- belongs_to: [[SalesContractField]]
- has_many: [[DocusignFile]]

### 主要なメソッド
- `generate_pdf`: PDF生成
- `file_path`: ファイルパス取得

---

## [[IntermediaryCompany]]
### 役割
仲介会社情報の管理。

### テーブル定義（例）
- name: string, null: false
- branch_name: string
- zip: string
- tel: string
- ...

### バリデーション
- name: presence
- branch_name: uniqueness（nameスコープ）
- lead_source: presence（新規時）
- zip, tel: format

### アソシエーション
- has_many: [[Article]], [[SupplierMail]], [[IntermediaryStaff]], [[IntermediaryDomain]]
- belongs_to: [[User]], [[Prefecture]]

### 主要なメソッド
- `name_with_branch`: 支店名付き名称
- `user_id_modification_histories`: 担当者変更履歴

---

## [[IntermediaryStaff]]
### 役割
仲介会社の担当者情報。

### テーブル定義（例）
- intermediary_company_id: integer, null: false
- email: string, null: false, unique
- name: string, null: false
- phone_number: string
- ...

### バリデーション
- email: presence, uniqueness
- name, users: presence
- phone_number: format

### アソシエーション
- belongs_to: [[IntermediaryCompany]]
- has_many: [[IntermediaryStaffUser]], [[User]]（through）

### 主要なメソッド
- `strip_email`: メールアドレスの空白除去

---

## [[IntermediaryDomain]]
### 役割
仲介会社のメールドメイン管理。

### テーブル定義（例）
- intermediary_company_id: integer, null: false
- user_id: integer, null: false
- domain: string, null: false, unique

### バリデーション
- domain: presence, uniqueness

### アソシエーション
- belongs_to: [[IntermediaryCompany]], [[User]]

### 主要なメソッド
- `delete_at_mark`, `strip_domain`: ドメイン整形

---

## [[BusinessPartner]]
### 役割
外部取引先（GA technologies等）の情報管理。

### テーブル定義（例）
- name: string
- ...

### バリデーション
- なし

### アソシエーション
- has_many: [[User]]

### 主要なメソッド
- `self.ga_tech`: GA technologies取得
- `self.address_with_postal_code`: 住所取得

---

## [[ArticleItem]]
### 役割
物件ごとの書類（ファイル）管理。

### テーブル定義（例）
- item_id: integer, null: false
- article_id: integer, null: false
- uploaded_date: date
- ...

### バリデーション
- item, article: presence

### アソシエーション
- belongs_to: [[Item]], [[Article]], [[User]]（uploaded_by）
- has_many: [[ArticleItemFile]], [[UnmountedArticleItemFile]]

### 主要なメソッド
- `upload_files!`: ファイルアップロード
- `bulk_create!`: 一括生成

---

## [[NegotiationHistory]]
### 役割
交渉履歴の管理。

### テーブル定義（例）
- article_id: integer, null: false
- negotiation_status: integer, enum
- ga_offer_price: integer
- intermediary_offer_price: integer
- ...

### バリデーション
- any_offer_price: presence

### アソシエーション
- belongs_to: [[Article]]
- has_one: [[OtherCompanyNegotiation]]

### 主要なメソッド
- `elapsed_days`: 経過日数
- `subtracted_offer_price`: 差額計算

---

## [[SalesInfo]]
### 役割
発表管理情報。

### テーブル定義（例）
- article_id: integer, null: false, unique

### バリデーション
- article_id: uniqueness

### アソシエーション
- belongs_to: [[Article]]

---

## [[SaleManagementInfo]]
### 役割
販売管理情報。

### テーブル定義（例）
- article_id: integer, null: false
- bank_id: integer
- ...

### バリデーション
- なし

### アソシエーション
- belongs_to: [[Article]], [[Bank]]

### 主要なメソッド
- `self.select_banks`: 顧客申込銀行リスト取得

---

## [[ConsumptionTaxVersion]]
### 役割
消費税計算バージョン管理。

### テーブル定義（例）
- article_id: integer, null: false
- user_id: integer, null: false
- calculation_method: integer, enum
- ...

### バリデーション
- なし

### アソシエーション
- belongs_to: [[Article]], [[User]]

### 主要なメソッド
- `input_logical_values_on_new_page`: 計算値セット
- `update_articles_consumption_tax!`: 記事の消費税更新

---

## [[Building]]
### 役割
建物情報の管理。

### テーブル定義（例）
- building_name: string
- zip: string
- prefecture: string
- ...

### バリデーション
- なし

### アソシエーション
- has_many: [[BuildingImage]], [[Article]]

---

## [[Prefecture]]
### 役割
都道府県情報・エリア区分。

### テーブル定義（例）
- name: string

### バリデーション
- なし

---

## [[Manager]] / [[Salesperson]] / [[SettlementAgent]] / [[LoanAgent]]
### 役割
ユーザーのサブクラス。各担当者種別。

### テーブル定義
- Userと同じ

### バリデーション・アソシエーション
- Userと同じ

---

## [[Janitor]]
### 役割
物件の管理人情報。

### テーブル定義（例）
- article_id: integer, null: false
- work_style: integer, enum
- ...

### バリデーション
- article_id, work_style: presence

### アソシエーション
- belongs_to: [[Article]]

### 主要なメソッド
- `work_style_maisoku_text`: マイソク用文言

---

## [[OwnrInfo]]
### 役割
OWNR用顧客契約書類の管理。

### テーブル定義（例）
- article_id: integer, unique
- ...

### バリデーション
- article_id: uniqueness

### アソシエーション
- belongs_to: [[Article]]

### 主要なメソッド
- `modification_histories`: 変更履歴取得

---

## [[SalesDestination]]
### 役割
販売先情報。

### テーブル定義（例）
- name: string, unique, null: false
- active: boolean
- ...

### バリデーション
- name: presence, uniqueness
- active: inclusion

### アソシエーション
- has_many: [[SalesDestinationArticle]]

### 主要なメソッド
- `self.default_sales_destination`: デフォルト販売先取得

---

## [[SalesDestinationArticle]]
### 役割
物件と販売先の関連。

### テーブル定義（例）
- sales_destination_id: integer, null: false
- article_id: integer, null: false, unique
- is_required_creating_document: boolean

### バリデーション
- sales_destination_id, article_id, is_required_creating_document: presence
- article_id: uniqueness

### アソシエーション
- belongs_to: [[SalesDestination]], [[Article]]

---

## [[PaymentRequest]]
### 役割
支払申請情報。

### テーブル定義（例）
- article_id: integer, null: false
- user_id: integer, null: false
- status: integer, enum
- ...

### バリデーション
- 支払申請済み後の一部項目: 変更不可バリデーション

### アソシエーション
- belongs_to: [[Article]], [[User]]
- has_many: [[PaymentRequestComment]]

### 主要なメソッド
- `self.bulk_synchronize_with_flow`: FLOW連携
- `sync_flow_comments`: コメント同期

---

## [[BuildingConfirmation]]
### 役割
建物確認情報。

### テーブル定義（例）
- article_id: integer, null: false
- user_id: integer, null: false

### バリデーション
- article_id, user_id: presence

### アソシエーション
- belongs_to: [[Article]], [[User]]

---

（他モデルも必要に応じて追記してください） 