# Comment

## 役割
コメントを管理するモデル。

## 主なリレーション
- belongs_to: [[Article]]
- belongs_to: [[User]]

## テーブル定義

| カラム名 | データ型 | 備考 |
|---|---|---|
| id | bigint | 主キー |
| article_id | integer | 物件ID（articleへの外部キー） |
| user_id | integer | ユーザーID（userへの外部キー） |
| content | text | コメント内容 |
| created_at | datetime | null: false |
| updated_at | datetime | null: false |

## 出典
- schema.rb: comments テーブル定義
- モデル: app/models/comment.rb 