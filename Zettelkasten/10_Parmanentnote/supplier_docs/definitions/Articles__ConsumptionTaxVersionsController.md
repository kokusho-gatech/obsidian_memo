# Articles__ConsumptionTaxVersionsController

> 本来のクラス名は Articles::ConsumptionTaxVersionsController です

---

## アクション一覧と詳細

### `show` (出典: app/controllers/articles/consumption_tax_versions_controller.rb:8)

* **機能概要:**
  消費税計算結果の表示。
* **処理フロー:**
    1. Article・SalesContractField・ConsumptionTaxVersionをIDで取得（:9-11）
* **返すもの:**
    - 計算結果画面のHTML

---

### `new` (出典: app/controllers/articles/consumption_tax_versions_controller.rb:13)

* **機能概要:**
  新規消費税計算画面の表示。
* **処理フロー:**
    1. Article・SalesContractFieldをIDで取得（:14-15）
    2. new_consumption_tax_versionで初期化（:16）
    3. input_logical_values_on_new_page・calculation_process_templateを実行（:17-18）
* **返すもの:**
    - 新規作成画面のHTML

---

### `create` (出典: app/controllers/articles/consumption_tax_versions_controller.rb:21)

* **機能概要:**
  消費税計算の新規作成。
* **処理フロー:**
    1. Article・SalesContractFieldをIDで取得（:22-23）
    2. ユーザー情報セット・new_consumption_tax_versionで初期化（:24-25）
    3. パラメータセット・update_articles_consumption_tax!で保存（:26-27）
    4. 成功時はリダイレクト、失敗時はエラー表示（:29-33）
* **返すもの:**
    - リダイレクトまたはエラー表示

---

### `last` (出典: app/controllers/articles/consumption_tax_versions_controller.rb:35)

* **機能概要:**
  最新消費税計算の表示・分岐。
* **処理フロー:**
    1. Article・SalesContractField・last_consumption_tax_versionを取得（:36-38）
    2. TechConsul成約・決済時や計算値相違時の分岐（:40-54）
    3. 最終計算結果があればshow、なければnewへ（:55-59）
* **返すもの:**
    - 計算結果画面のHTMLまたはリダイレクト

---

## 関連リンク
- [[Article]]
- [[ConsumptionTaxVersion]]
- [[消費税計算]] 