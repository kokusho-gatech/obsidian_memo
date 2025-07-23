---
tags:
  - spec
  - supplier
  - controller
  - parmanentnote
---
# SUPPLIER by RENOSY コントローラー一覧

本ドキュメントは、主要なコントローラーの一覧と、その詳細解説ノートへのリンク集です。

---

## コントローラー一覧

- [ArticlesController](./definitions/ArticlesController.md)
- [SaleManagementInfosController](./definitions/SaleManagementInfosController.md)
- [SalesContractTemplatesController](./definitions/SalesContractTemplatesController.md)
- [SaleMaisokuProgresses\:\:CheckersController](./definitions/SaleMaisokuProgresses__CheckersController.md)
- [MultipleSelectOptionsController](./definitions/MultipleSelectOptionsController.md)
- [UnprocessedMailsController](./definitions/UnprocessedMailsController.md)
- [IntermediaryCompaniesController](./definitions/IntermediaryCompaniesController.md)
- [BanksController](./definitions/BanksController.md)
- [AssessmentController](./definitions/AssessmentController.md)
- [CancellationsController](./definitions/CancellationsController.md)
- [HomeController](./definitions/HomeController.md)
- [FilePublishedDatesController](./definitions/FilePublishedDatesController.md)
- [UserIdModificationHistoriesController](./definitions/UserIdModificationHistoriesController.md)
- [IntermediaryCompanies__StatusesController](./definitions/IntermediaryCompanies__StatusesController.md)
- [UsersController](./definitions/UsersController.md)
- [IntermediaryCompanies\:\:ArticlesController](./definitions/IntermediaryCompanies__ArticlesController.md)
- [LabelsController](./definitions/LabelsController.md)
- [PurchaseContractsController](./definitions/PurchaseContractsController.md)
- [IntermediaryDomainsController](./definitions/IntermediaryDomainsController.md)
- [ContractController](./definitions/ContractController.md)
- [BuildingConfirmationsController](./definitions/BuildingConfirmationsController.md)
- [AssessmentNgController](./definitions/AssessmentNgController.md)
- [ShootingInfosController](./definitions/ShootingInfosController.md)
- [Articles\:\:AssessmentController](./definitions/Articles__AssessmentController.md)
- [CatalogsController](./definitions/CatalogsController.md)
- [SalesContractFieldsController](./definitions/SalesContractFieldsController.md)
- [ApprovedApprovalsController](./definitions/ApprovedApprovalsController.md)
- [NegotiatedSameBuildingAndFloorArticlesController](./definitions/NegotiatedSameBuildingAndFloorArticlesController.md)
- [SaleStatesController](./definitions/SaleStatesController.md)
- [InputsController](./definitions/InputsController.md)
- [DeletedController](./definitions/DeletedController.md)
- [ConsumptionTaxVersionsController](./definitions/ConsumptionTaxVersionsController.md)
- [ArticleItemsController](./definitions/ArticleItemsController.md)
- [LatestApprovalsController](./definitions/LatestApprovalsController.md)
- [PaymentRequestsController](./definitions/PaymentRequestsController.md)
- [ArticleItemFilesController](./definitions/ArticleItemFilesController.md)
- [UwanoseMaisokusController](./definitions/UwanoseMaisokusController.md)
- [InventoriesController](./definitions/InventoriesController.md)
- [NegotiationHistoriesController](./definitions/NegotiationHistoriesController.md)
- [NgsController](./definitions/NgsController.md)
- [OksController](./definitions/OksController.md)
- [RegistrationDocumentsController](./definitions/RegistrationDocumentsController.md)
- [Articles\:\:PriorValuationsController](./definitions/Articles__PriorValuationsController.md)
- [ValuationHistoriesController](./definitions/ValuationHistoriesController.md)
- [DocumentProgressesController](./definitions/DocumentProgressesController.md)
- [ForSaleMaisokusController](./definitions/ForSaleMaisokusController.md)
- [Articles\:\:OwnrInfosController](./definitions/Articles__OwnrInfosController.md)
- [BuildingInformationsController](./definitions/BuildingInformationsController.md)
- [LatestSaleApprovalsController](./definitions/LatestSaleApprovalsController.md)
- [NegotiationSchedulesController](./definitions/NegotiationSchedulesController.md)

---

各コントローラーの詳細は、上記リンク先のノートを参照してください。 


```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}
```