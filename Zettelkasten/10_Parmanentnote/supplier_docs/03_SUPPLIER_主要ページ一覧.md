# SUPPLIER by RENOSY 主要ページ一覧

本ノートは、SUPPLIER by RENOSYの主要な画面・機能ページのURLパス一覧と、その詳細解説ノートへのリンク集です。

---

## 査定ページ
- [[AssessmentPage]] `/articles/assessment` : 査定一覧
- [[AssessmentNgPage]] `/articles/assessment_ng` : 査定NG一覧
- [[UnassociatedPage]] `/articles/unassociated` : 仲介担当なし一覧
- [[AssessmentEditPage]] `/articles/assessment/:id/edit` : 査定編集

## 交渉ページ
- [[ManagementPage]] `/articles/management` : 交渉一覧
- [[ManagementForApprovalEditPage]] `/articles/:id/management/for_approval/edit` : 交渉詳細(バイヤー用)
- [[ManagementForPaymentRequestEditPage]] `/articles/:id/management/for_payment_request/edit` : 交渉詳細(コントラクト用)

## 発表ページ
- [[SaleManagementInfosPage]] `/sale_management_infos` : 発表管理一覧
- [[ArticleDetailPage]] `/articles/:id` : 発表詳細
- [[ArticleItemsPage]] `/articles/:id/article_items` : ファイルチェックページ

## その他の物件ページ
- [[DeletedArticlesPage]] `/articles/deleted` : 削除済み物件一覧

## 仕入評価ページ
- [[PriorValuationsPage]] `/articles/prior_valuations` : 仕入評価一覧
- [[PriorValuationEditPage]] `/articles/prior_valuations/:id/edit` : 仕入評価編集

## 仕入稟議ページ
- [[LatestApprovalsPage]] `/articles/latest_approvals` : 仕入稟議一覧
- [[LatestApprovalEditPage]] `/articles/:id/latest_approval/edit` : 仕入稟議編集

## 販売稟議ページ
- [[LatestSaleApprovalsPage]] `/articles/latest_sale_approvals` : 販売稟議一覧
- [[LatestSaleApprovalEditPage]] `/articles/:id/latest_sale_approval/edit` : 販売稟議編集

## 銀行評価ページ
- [[ValuationHistoriesEditPage]] `/articles/prior_valuations/:id/valuation_histories/edit` : 銀行評価編集

## 仕入契約ページ
- [[PurchaseContractsPage]] `/purchase_contracts` : 仕入契約一覧

## ドラフトチェックページ
- [[InputsPage]] `/articles/:id/inputs` : 書類入力一覧
- [[CertifiedCopyEditPage]] `/articles/:id/inputs/certified_copy/edit` : 謄本の書類入力編集
- ...（他、書類入力編集系）

## 契約書作成進捗ページ
- [[DocumentProgressesPage]] `/articles/document_progresses` : 契約書作成進捗一覧

## 建物情報確認ページ
- [[BuildingInformationEditPage]] `/articles/:id/building_information/edit` : 建物情報編集
- ...（他、建物関連編集系）

## マイソク・シミュレーション作成ページ
- [[ForSaleMaisokuEditPage]] `/articles/:id/for_sale_maisoku/edit` : マイソク作成
- [[ForSimulationEditPage]] `/articles/:id/for_simulation/edit` : シミュレーション作成

## 契約書ページ
- [[SalesAgreementSetPage]] `/articles/:id/sales_contract_fields/:sales_contract_field_id/sales_agreement_set` : 契約書セット
- ...（他、多数）

## 消費税計算ページ
- [[ConsumptionTaxVersionsNewPage]] `/articles/:id/consumption_tax_versions/new` : 消費税計算新規作成
- ...（他）

## 顧客契約書類ページ
- [[SoldDocumentsPage]] `/articles/:id/sold/documents` : 顧客契約書類

## 建物確認ページ
- [[BuildingConfirmationsPage]] `/articles/:id/building_confirmations` : 建物確認一覧
- ...（他）

## 仲介会社ページ
- [[IntermediaryCompaniesPage]] `/intermediary_companies` : 仲介会社一覧
- ...（他、多数）

## ユーザーページ
- [[UsersPage]] `/users` : ユーザー一覧
- ...（他）

## マスタ管理ページ
- [[SalesContractTemplatesPage]] `/sales_contract_templates` : 売買契約テンプレート一覧
- ...（他）

---

※各リンク先ノートで、画面の詳細・データフロー・UI要素と裏側実装の対応を解説しています。 