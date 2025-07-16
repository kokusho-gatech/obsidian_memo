# SUPPLIER by RENOSY コントローラードキュメント

---

## [[users_controller.rb]]

### 役割
- [[User]]モデルの管理（一覧・詳細・新規作成・編集・認証連携など）を担当するコントローラー。

### アクション一覧
- `index`: ユーザー一覧を表示。[[index.html.erb]]をレンダリング。
- `show`: ユーザー詳細を表示。[[show.html.erb]]をレンダリング。
- `new`: 新規ユーザー作成フォームを表示。[[new.html.erb]]をレンダリング。
- `edit`: ユーザー編集フォームを表示。[[edit.html.erb]]をレンダリング。
- `create`: ユーザー新規作成。成功時は一覧へリダイレクト、失敗時は[[new.html.erb]]。
- `update`: ユーザー情報更新。成功時は一覧へリダイレクト、失敗時は[[edit.html.erb]]。
- `login`: Google認証のためのリダイレクト処理。
- `authorize_gmail`: Gmail認証連携処理。
- `clear_gmail_authorization`: Gmail認証情報の削除。

### コールバック
- `before_action :authenticate_user!`（except: :login）: ログイン必須
- `skip_before_action :verify_authenticity_token`（only: :create）
- `skip_before_action :reject_unauthorized_user`（only: :create）

### Strong Parameters
- `create_params`: `:name, :email, :mobile_phone, :leave, :type, authority: []`
- `update_params`: `:name, :mobile_phone, :leave, :type, authority: []`
- `search_params`: `:name, :email, :leave, :type, :authority`

---

## [[articles_controller.rb]]

### 役割
- [[Article]]モデルの物件管理（詳細表示・新規作成・更新・削除・ゴミ箱管理など）を担当するコントローラー。

### アクション一覧
- `show`: 物件詳細を表示。[[show.html.erb]]をレンダリング。
- `create`: 新規物件を作成し、編集画面へリダイレクト。
- `update`: 物件情報を更新。JSONで結果返却。
- `bulk_delete`: 複数物件をゴミ箱に移動。
- `back_from_trash`: ゴミ箱から物件を復元。
- `maisoku`, `approval_document`, `change_approval`: 画像セクションのJSON返却。
- `update_with_tech_building`: BLDG連携・建物情報更新。
- その他、多数の物件管理系アクション。

### コールバック
- `skip_before_action :verify_authenticity_token`（only: bulk_delete, back_from_trash, update）
- `before_action :set_article`（only: show, update, row, back_from_trash, maisoku, approval_document, change_approval）

### Strong Parameters
- `article_params`, `registration_and_assessment_params`, `management_and_contract_params` などで各種属性をpermit。
- `page_params`, `maisoku_params` などもあり。

---

## [[sale_management_infos_controller.rb]]

### 役割
- 販売管理情報（[[SaleManagementInfo]]）の一覧表示・CSVダウンロードを担当。

### アクション一覧
- `index`: 販売管理情報の一覧を表示。[[index.html.erb]]をレンダリング。
- `download`: 条件に応じたCSVファイルを生成しダウンロード。

### コールバック
- なし

### Strong Parameters
- 検索条件（params[:q]）やページネーション用のパラメータ。
- `convert_man_yen_attributes`で金額系パラメータを変換。

---

## [[intermediary_companies_controller.rb]]

### 役割
- [[IntermediaryCompany]]モデルの仲介会社情報の管理（一覧・新規作成・編集・削除）を担当。

### アクション一覧
- `index`: 仲介会社一覧を表示。[[index.html.erb]]をレンダリング。
- `new`: 新規仲介会社作成フォームを表示。[[new.html.erb]]をレンダリング。
- `edit`: 仲介会社編集フォームを表示。[[edit.html.erb]]をレンダリング。
- `create`: 仲介会社新規作成。成功時は一覧へリダイレクト、失敗時は[[new.html.erb]]。
- `update`: 仲介会社情報更新。成功時は編集画面へリダイレクト、失敗時は[[edit.html.erb]]。
- `destroy`: 仲介会社の削除。権限チェックあり。

### コールバック
- なし（privateメソッドでパラメータ制御）

### Strong Parameters
- `intermediary_company_params`で許可される属性を制御（権限や編集状態によって動的に変化）。

---

（他コントローラーも順次追記してください） 