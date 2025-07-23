---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# BuildingConfirmationsPage

## 概要
物件ごとの建物確認情報を一覧・管理する画面。現地調査や確認事項の記録・進捗管理が可能です。

## 画面構成
- 建物確認一覧テーブル
- 詳細リンク・編集ボタン
- 進捗ステータス表示

## データの流れ
- コントローラ: `articles/building_confirmations_controller.rb`（推定）
- モデル: `BuildingConfirmation`, `Article` など

## UIとデータの対応
- 一覧テーブルで確認情報を表示
- 詳細・編集ボタンで内容を確認・修正
- 進捗状況を表示

## 関連リンク
- [[BuildingConfirmation]]
- [[Article]] 