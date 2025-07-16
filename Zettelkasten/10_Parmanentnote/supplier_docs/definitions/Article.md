# Article

## 役割
物件情報を管理するモデル。

## 主なリレーション
- belongs_to: [[User]]
- has_many: [[ArticleItem]]
- has_many: [[NegotiationHistory]]
- has_many: [[Approval]]
- has_many: [[PaymentRequest]]
- has_many: [[SaleMaisokuProgress]]
- has_many: [[SaleManagementInfo]]
- has_many: [[SalesContractField]]
- has_one: [[SalesInfo]]
- has_one: [[SalesPropertiesSheetField]]
- has_many: [[BuildingConfirmation]]
- has_one: [[Janitor]]
- has_many: [[JikoshintakuArticle]]
- has_one: [[OwnrInfo]]
- has_many: [[Comment]]
- has_many: [[PricePrediction]]
- has_many: [[PriorValuation]]
- has_many: [[Valuation]]
- has_many: [[SalesDestinationArticle]]
- has_many: [[ConsumptionTaxVersion]]
- has_many: [[PurchaseContract]]

## テーブル定義

※カラム数が多いため省略。詳細は[[schema.rb]]を参照。

## 出典
- schema.rb: articles テーブル定義
- モデル: app/models/article.rb 