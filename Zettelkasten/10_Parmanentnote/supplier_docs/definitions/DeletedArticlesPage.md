---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# DeletedArticlesPage

## 概要
削除済み物件の一覧を表示・管理する画面。復元や完全削除などの操作が可能です。

## 画面構成
- 削除済み物件一覧テーブル
- 復元ボタン・完全削除ボタン

## データの流れ
- コントローラ: `articles/deleted_controller.rb`（推定）
- モデル: `Article` など

## UIとデータの対応
- 一覧テーブルで削除済み物件を表示
- 復元・削除ボタンで操作

## 関連リンク
- [[Article]] 