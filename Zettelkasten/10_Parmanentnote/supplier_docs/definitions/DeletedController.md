---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# DeletedController（Articles::DeletedController）

## 概要
- 削除済み物件一覧ページのコントローラー。
- `/articles/deleted` で利用。

## アクション一覧

### index（6-10行目）
- **受け取るもの**: params（フィルタ条件等）
- **処理内容**: IndexFormで絞り込み、更新日時降順でページネーション。
- **返すもの**: @articles（ビューで利用）

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 