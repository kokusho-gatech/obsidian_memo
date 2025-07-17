# SoldDocumentsPage

## 概要
成約済み物件の顧客契約書類を一覧・管理する画面。各種契約書類のダウンロードや進捗確認が可能です。

## 画面構成
- 契約書類一覧テーブル
- ダウンロードボタン
- 進捗ステータス表示

## データの流れ
- コントローラ: `articles/sold/documents_controller.rb`（推定）
- モデル: `Article`, `SoldDocument` など

## UIとデータの対応
- 一覧テーブルで書類を表示
- ダウンロードボタンで取得
- 進捗状況を表示

## 関連リンク
- [[Article]]
- [[SoldDocument]] 