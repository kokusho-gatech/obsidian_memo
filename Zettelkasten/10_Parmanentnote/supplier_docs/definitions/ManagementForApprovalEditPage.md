# ManagementForApprovalEditPage

## 概要
交渉中物件のバイヤー担当者向け詳細編集画面。交渉内容や進捗、履歴の確認・編集が可能です。

## 画面構成
- 交渉内容入力フォーム
- 進捗・履歴表示
- 保存ボタン

## データの流れ
- コントローラ: `articles/management/for_approval_controller.rb`（推定）
- モデル: `Article`, `NegotiationHistory` など

## UIとデータの対応
- 入力フォームで交渉内容を登録・編集
- 進捗・履歴を表示
- 保存ボタンで更新

## 関連リンク
- [[Article]]
- [[NegotiationHistory]] 