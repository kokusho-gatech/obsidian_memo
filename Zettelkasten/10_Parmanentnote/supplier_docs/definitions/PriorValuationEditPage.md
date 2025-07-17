# PriorValuationEditPage

## 概要
仕入評価（PriorValuation）を編集する画面。評価内容や担当者、回答状況などを入力・修正します。

## 画面構成
- 評価内容入力フォーム
- 担当者・回答状況表示
- 保存ボタン

## データの流れ
- コントローラ: `articles/prior_valuations_controller.rb`（推定）
- モデル: `PriorValuation`, `Article` など

## UIとデータの対応
- 入力フォームで評価内容を登録・編集
- 担当者・回答状況を表示
- 保存ボタンで更新

## 関連リンク
- [[PriorValuation]]
- [[Article]]
 