---
tags:
  - definition
  - ruby-on-rails
  - active-job
  - background-job
  - parmanentnote
---

# ApplicationJob

## 概要
SUPPLIER by RENOSYの全てのバックグラウンドジョブの基底クラス。共通のログ機能とエラーハンドリングを提供します。

## 主な用途・処理内容
- 他のジョブクラスが継承して使用
- around_performコールバックでジョブ開始・完了時のログ出力
- エラー発生時はエラーログとバックトレースを出力

## トリガー
- 直接実行されることはなく、他のジョブの基底クラスとして機能

## 扱うデータ
- なし（基底クラス） 