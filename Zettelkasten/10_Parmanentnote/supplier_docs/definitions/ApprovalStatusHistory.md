---
tags:
  - definition
  - model
  - supplier
  - parmanentnote
---

# ApprovalStatusHistory

## 役割
稟議のステータス履歴を管理するモデル。

## 主なリレーション
- belongs_to: [[Approval]]
- belongs_to: [[User]]（actor）
- has_one: [[ApprovalStatusHistoryComment]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | integer | 主キー |
| approval_id | integer | 稟議ID（approvalへの外部キー） |
| actor_id | integer | 操作ユーザーID（userへの外部キー） |
| status | integer | ステータス |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: approval_status_histories テーブル定義
- モデル: app/models/approval_status_history.rb 