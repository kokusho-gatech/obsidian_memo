# Attachment

## 役割
メール添付ファイルを管理するモデル。

## 主なリレーション
- belongs_to: [[SupplierMail]]
- belongs_to: [[Article]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| supplier_mail_id | integer | 査定メールID（supplier_mailへの外部キー） |
| article_id | integer | 物件ID（articleへの外部キー） |
| file_name | string | ファイル名 |
| file_size | integer | ファイルサイズ |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: attachments テーブル定義
- モデル: app/models/attachment.rb 