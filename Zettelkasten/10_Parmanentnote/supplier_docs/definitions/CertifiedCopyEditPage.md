# CertifiedCopyEditPage

## 概要
物件の謄本（登記簿謄本）情報を入力・編集する画面。OCRやファイルアップロード機能と連携し、謄本データを管理します。

## 画面構成
- 謄本情報入力フォーム
- ファイルアップロード・OCRボタン
- 入力内容の保存ボタン

## データの流れ
- コントローラ: `articles/inputs/certified_copy_controller.rb`（推定）
- モデル: `InputCertifiedCopy`, `Article` など
- OCR・ファイルアップロードはバックグラウンドジョブ（UpdateModelsWithCertifiedCopyReaderJob等）と連携

## UIとデータの対応
- 入力フォームで謄本情報を登録・編集
- ファイルアップロード・OCRボタンで自動入力
- 保存ボタンで内容を保存

## 関連リンク
- [[InputCertifiedCopy]]
- [[Article]]
- [[UpdateModelsWithCertifiedCopyReaderJob]] 