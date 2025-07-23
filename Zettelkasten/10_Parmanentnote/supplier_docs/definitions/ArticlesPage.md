---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# ArticlesPage

SUPPLIER by RENOSYの物件管理の中核となる画面・コントローラーの仕様まとめ。

---

## アクション一覧と詳細

（以下、ArticlesController.mdの内容をそのまま記載）

# ArticlesController

SUPPLIER by RENOSYの物件管理の中核となるコントローラー。

---

## アクション一覧と詳細

### `show` (出典: `app/controllers/articles_controller.rb:38`)

* **機能概要:**
  物件詳細ページを表示。物件の状態に応じて査定編集や交渉詳細ページへリダイレクトも行う。
* **処理フロー:**
    1. `@article`をセット（`set_article`、`articles_controller.rb:261`）
    2. 物件が査定中なら査定編集へリダイレクト（`articles_controller.rb:40`）
    3. 物件が交渉中なら交渉詳細へリダイレクト（`articles_controller.rb:41`）
    4. 物件・契約・所有者・ファイルタブ等の情報をインスタンス変数に格納（`articles_controller.rb:43-66`）
    5. 必要に応じてGoogle認証URLや購入契約情報も取得
* **返すもの:**
    - 物件詳細ページのHTML
    - 状況によりリダイレクト

---

### `create` (出典: `app/controllers/articles_controller.rb:72`)

* **機能概要:**
  新規物件を作成し、査定編集ページへ遷移。
* **処理フロー:**
    1. `Article.new`で新規インスタンス作成（`articles_controller.rb:73`）
    2. 投資用物件・初期ステータス・査定フェーズをセット（`articles_controller.rb:74-76`）
    3. 保存し、コメントを残す（`articles_controller.rb:78-79`）
    4. 査定編集ページへリダイレクト（`articles_controller.rb:81`）
* **返すもの:**
    - 査定編集ページへのリダイレクト

---

### `update` (出典: `app/controllers/articles_controller.rb:85`)

* **機能概要:**
  物件情報の更新。リリース済みの場合は外部連携も実施。
* **処理フロー:**
    1. 顧客情報の挿入可否を判定（`customer_info_not_insertable?`、`articles_controller.rb:366`）
    2. 更新・ファイルアップロード処理（`update_and_upload!`、`articles_controller.rb:266`）
    3. リリース済みなら`@article.release!`で外部連携（`articles_controller.rb:92`）
    4. コメント追加やJSONレスポンス返却（`articles_controller.rb:99-110`）
    5. 例外時はエラーレスポンス
* **外部連携:**
    - `Connectors::TechConsul`（`articles_controller.rb:90`）
    - `@article.release!`（`articles_controller.rb:92`）
* **返すもの:**
    - 更新結果のJSONまたはエラーメッセージ

---

### `bulk_delete` (出典: `app/controllers/articles_controller.rb:126`)

* **機能概要:**
  複数物件をゴミ箱に移動（論理削除）。
* **処理フロー:**
    1. 対象物件を取得（`Article.where(id: params[:ids])`、`articles_controller.rb:127`）
    2. リリース済み・管理替え物件・LancersOperatorの制約を判定（`articles_controller.rb:128-139`）
    3. 各物件を論理削除し、コメント追加（`articles_controller.rb:142-144`）
    4. 成功レスポンスをJSONで返却（`articles_controller.rb:145`）
* **返すもの:**
    - 成功メッセージのJSON

---

### `back_from_trash` (出典: `app/controllers/articles_controller.rb:153`)

* **機能概要:**
  ゴミ箱から物件を復元。
* **処理フロー:**
    1. `@article`の`deleted`フラグをfalseに（`update_column`、`articles_controller.rb:154`）
    2. コメント追加（`articles_controller.rb:155`）
    3. レスポンス形式に応じてJSONまたはリダイレクト（`articles_controller.rb:157-165`）
* **返すもの:**
    - 復元メッセージのJSONまたはリダイレクト

---

### `maisoku` (出典: `app/controllers/articles_controller.rb:169`)

* **機能概要:**
  マイソク画像のHTML断片を返すAPI。
* **処理フロー:**
    1. `@article.signed_maisoku_url`をHTML化しJSONで返却（`articles_controller.rb:170`）
* **返すもの:**
    - 画像HTML断片のJSON

---

### `approval_document` (出典: `app/controllers/articles_controller.rb:173`)

* **機能概要:**
  承認書類画像のHTML断片を返すAPI。
* **処理フロー:**
    1. `@article.target_approval&.name_url`をHTML化しJSONで返却（`articles_controller.rb:174`）
* **返すもの:**
    - 画像HTML断片のJSON

---

### `change_approval` (出典: `app/controllers/articles_controller.rb:177`)

* **機能概要:**
  承認書類（変更後）画像のHTML断片を返すAPI。
* **処理フロー:**
    1. `@article.target_approval&.change_name_url`をHTML化しJSONで返却（`articles_controller.rb:179`）
* **返すもの:**
    - 画像HTML断片のJSON

---

### `update_with_tech_building` (出典: `app/controllers/articles_controller.rb:180`)

* **機能概要:**
  TechBuilding連携による建物情報の更新。
* **処理フロー:**
    1. `params[:tech_building_id]`のバリデーション（`articles_controller.rb:183`）
    2. `tech_building_id`の更新・建物情報の上書き（`articles_controller.rb:185-186`）
    3. 成功/失敗時のフラッシュメッセージ設定（`articles_controller.rb:188-191`）
    4. リダイレクト（`articles_controller.rb:193`）
* **返すもの:**
    - フラッシュメッセージ付きリダイレクト

---

### `move_to_trash` (出典: `app/controllers/articles_controller.rb:195`)

* **機能概要:**
  物件をゴミ箱に移動（論理削除）。
* **処理フロー:**
    1. 物件取得・リリース済み/管理替え判定（`articles_controller.rb:196-201`）
    2. 論理削除・コメント追加（`articles_controller.rb:203-204`）
    3. リダイレクト（`articles_controller.rb:206`）
* **返すもの:**
    - フラッシュメッセージ付きリダイレクト

---

### `create_tech_building` (出典: `app/controllers/articles_controller.rb:214`)

* **機能概要:**
  TechBuildingに建物情報を新規作成し、物件と連携。
* **処理フロー:**
    1. 建物名・住所の入力チェック（`articles_controller.rb:215-218`）
    2. TechBuilding::Building.create_or_update呼び出し（`articles_controller.rb:220`）
    3. 物件にtech_building_idをセット（`articles_controller.rb:224`）
    4. リダイレクト（`articles_controller.rb:227`）
* **外部連携:**
    - `TechBuilding::Building`（`articles_controller.rb:220`）
* **返すもの:**
    - フラッシュメッセージ付きリダイレクト

---

### `activate_certified_copy_uploader` (出典: `app/controllers/articles_controller.rb:236`)

* **機能概要:**
  謄本取得APIの起動。
* **処理フロー:**
    1. 物件の所有者情報チェック（`articles_controller.rb:238`）
    2. `article.activate_certified_copy_uploader`呼び出し（`articles_controller.rb:240`）
    3. 成功/失敗時のフラッシュ・Rollbar通知（`articles_controller.rb:242-251`）
    4. リダイレクト（`articles_controller.rb:253`）
* **外部連携:**
    - 謄本取得API（`articles_controller.rb:240`）
* **返すもの:**
    - フラッシュメッセージ付きリダイレクト

---

## 関連リンク
- [[Article]]
- [[TechBuilding]]
- [[認証・権限]]
- [[ファイル管理]]
- [[外部API連携]] 