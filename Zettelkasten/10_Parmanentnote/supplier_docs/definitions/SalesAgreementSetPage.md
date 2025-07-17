# SalesAgreementSetPage

## 概要
物件ごとの売買契約書類一式（PDF等）を生成・ダウンロードできる画面。必要な契約書類をまとめて出力します。

## 画面構成
- 契約書類選択リスト
- PDF生成・ダウンロードボタン

## データの流れ
- コントローラ: `articles/sales_contract_fields_controller.rb`（推定）
- モデル: `SalesContractField`, `Article` など

## UIとデータの対応
- 必要な契約書類を選択
- 生成ボタンでPDF一式を作成
- ダウンロードリンクで取得

## 関連リンク
- [[SalesContractField]]
- [[Article]] 