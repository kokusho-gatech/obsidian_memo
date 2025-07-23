---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# ファイルチェックページ（/articles/:id/article_items）

> [[Articles__ArticleItemsController]] `index`アクション & `app/views/articles/article_items/index.html.erb` による描画

---

## 画面概要

- 物件（Article）に紐づく各種書類・ファイルのチェック・ダウンロード・アップロードを行う画面。
- 書類の種別ごとにチェックリスト形式で表示し、DLや資料再利用、ヒアリング内容確認などの操作が可能。

---

## 1. データの流れ

- **コントローラ:** `app/controllers/articles/article_items_controller.rb:8-22`
    - `@article` : 対象の[[Article]]
    - `@ownr_info` : OWNR持ち帰り契約書類情報
    - `@modification_histories` : 変更履歴
    - `@article_wrapper_class` : レイアウト用クラス
    - `@is_file_check_page` : ファイルチェックページ判定
    - `@building_confirmations_count` : ヒアリング内容数

- **主なロジック:**
    - Articleの関連情報をpreloadし、ファイルタブや持ち帰り契約書類情報をセット

---

## 2. UIとデータの対応

- **物件名:** `@article.article_name`（リンク付き、`_article_file.html.erb:6`）
- **ファイル操作ボタン:** 謄本取得・前回資料再利用・ヒアリング内容・DLボタン（`_article_file.html.erb:38-45`）
- **書類チェックリスト:** 各種書類種別ごとに`render 'articles/selected/checklist_detail_file'`で表示（`_article_file.html.erb:48-77`）
- **OWNR持ち帰り契約書類:** アラート表示（`_article_file.html.erb:24-33`）
- **ページネーションや各種リンク**

---

## 関連リンク
- [[Articles__ArticleItemsController]]
- [[Article]]

---

## 参考ファイル
- コントローラ: `app/controllers/articles/article_items_controller.rb`
- モデル: `app/models/article.rb`
- ビュー: `app/views/articles/article_items/index.html.erb`, `_article_file.html.erb` 