# SaleManagementInfosController

> 本来のクラス名は SaleManagementInfosController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/sale_management_infos_controller.rb:6)

* **機能概要:**
  売上管理情報の一覧を検索・集計し、画面表示する。
* **処理フロー:**
    1. 検索パラメータを取得・初期化（`params[:q]` or `default_search_articles`、:7-10）
    2. 金額系パラメータを変換（`convert_man_yen_attributes`、:11）
    3. Ransackで検索条件を構築（`Article.ransack(param)`、:12）
    4. 検索条件があれば、物件一覧・合計金額等を集計（:15-27）
    5. 検索条件がなければ空リスト（:29）
* **返すもの:**
    - 一覧画面のHTML

---

### `download` (出典: app/controllers/sale_management_infos_controller.rb:32)

* **機能概要:**
  売上管理情報のCSVダウンロード。
* **処理フロー:**
    1. 検索パラメータ取得・初期化（:33-36）
    2. Ransackで検索条件を構築（:37-38）
    3. 検索条件があれば物件一覧を取得（:41-48）
    4. CSV種別に応じて出力クラスを選択（:51-58）
    5. 一時ファイルにCSVを書き出し（:60-66）
    6. send_dataでダウンロードレスポンス（:68-72）
    7. 一時ファイル削除（:74）
* **返すもの:**
    - CSVファイルのダウンロードレスポンス

---

## 関連リンク
- [[Article]]
- [[売上管理]]
- [[CSV出力]] 