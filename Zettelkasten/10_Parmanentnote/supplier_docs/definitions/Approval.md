---
tags:
  - definition
  - model
  - supplier
  - parmanentnote
---

# Approval

## 役割
稟議申請管理を行うモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[User]]
- has_one: [[ApprovalDetail]]
- has_many: [[ApprovalStatusHistory]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| name | string | 稟議書（carrierwaveでマウントするカラム） |
| change_name | string | 変更稟議事情説明書（carrierwaveでマウントするカラム） |
| status | integer | 稟議のステータス |
| kintone_id | integer | kintone上でのID |
| no | integer | 稟議申請回数。2以降は変更稟議。 |
| comment | text | コメント |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: approvals テーブル定義
- モデル: app/models/approval.rb 