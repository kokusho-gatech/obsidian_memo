---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# ForSimulationEditPage

## 概要
物件のシミュレーション（収支・投資効果等）を作成・編集する画面。入力した条件に基づき、収支計算や投資指標を自動算出します。

## 画面構成
- シミュレーション条件入力フォーム
- 計算結果表示エリア
- グラフ・チャート表示

## データの流れ
- コントローラ: `articles/for_simulation_controller.rb`（推定）
- モデル: `Article`, `Simulation` など

## UIとデータの対応
- 入力フォームで条件を登録
- 計算ボタンで収支・指標を算出
- 結果をグラフや表で表示

## 関連リンク
- [[Article]]
- [[Simulation]] 