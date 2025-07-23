---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# InputsController（Articles::InputsController）

## 概要
- 書類入力一覧ページのコントローラー。
- `/articles/:id/inputs` で利用。

## アクション一覧

### index（6-16行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、入力対象のArticleItemや契約・販売情報をセット。
- **返すもの**: @article, @article_item_inputs, @purchase_contract, @sales_info

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 