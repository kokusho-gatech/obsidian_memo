---
tags:
  - definition
  - user
  - model
  - parmanentnote
---

# User

## 役割
ユーザー情報を管理するモデル。

## 主なリレーション
- has_many: [[Article]]
- has_many: [[Approval]]
- has_many: [[IntermediaryCompany]]
- has_many: [[IntermediaryDomain]]
- has_many: [[IntermediaryStaff]]
- has_many: [[SupplierMail]]
- has_many: [[PaymentRequest]]
- has_many: [[BuildingConfirmation]]
- has_many: [[SaleMaisokuProgress]]
- has_many: [[ConsumptionTaxVersion]]
- has_many: [[PriorValuation]]
- has_many: [[Comment]]
- has_one: [[UsersSetting]]
- has_many: [[IntermediaryStaffUser]]
- has_many: [[ApprovalStatusHistory]]（as actor）
- has_many: [[SaleApproval::StatusHistory]]（as actor）

## テーブル定義

※カラム数が多いため省略。詳細は[[schema.rb]]を参照。

## 出典
- schema.rb: users テーブル定義
- モデル: app/models/user.rb 