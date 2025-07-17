# ForSaleMaisokuEditPage

## 概要
物件のマイソク（販売図面）を作成・編集する画面。物件情報や画像をもとにマイソクを生成し、販売資料として活用します。

## 画面構成
- 物件情報入力フォーム
- 画像アップロード・プレビュー
- マイソク生成ボタン

## データの流れ
- コントローラ: `articles/for_sale_maisoku_controller.rb`（推定）
- モデル: `Article`, `ArticleItemFile` など
- マイソク生成処理はバックグラウンドジョブ（ReplaceMaisokuForSbjJob等）と連携

## UIとデータの対応
- 入力フォームで物件情報・画像を登録
- 生成ボタンでマイソクPDF等を作成
- 生成結果のダウンロード・プレビュー

## 関連リンク
- [[Article]]
- [[ReplaceMaisokuForSbjJob]] 