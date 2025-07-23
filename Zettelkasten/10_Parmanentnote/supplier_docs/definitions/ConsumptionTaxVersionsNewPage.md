---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# ConsumptionTaxVersionsNewPage

## 概要
物件ごとの消費税計算バージョンを新規作成する画面。消費税率や課税区分などを入力し、計算結果を保存します。

## 画面構成
- 消費税率・課税区分入力フォーム
- 計算結果表示
- 保存ボタン

## データの流れ
- コントローラ: `articles/consumption_tax_versions_controller.rb`（推定）
- モデル: `ConsumptionTaxVersion`, `Article` など

## UIとデータの対応
- 入力フォームで税率・区分を登録
- 計算ボタンで結果を表示
- 保存ボタンでバージョンを作成

## 関連リンク
- [[ConsumptionTaxVersion]]
- [[Article]] 