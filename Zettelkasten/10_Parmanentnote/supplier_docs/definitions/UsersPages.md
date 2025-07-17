# ユーザー一覧画面（/users）

> [[UsersController]] `index`アクション & `app/views/users/index.html.erb` による描画

---

## 1. データの流れ

- **コントローラ:** `app/controllers/users_controller.rb:10`
    - `@users = User.search(search_params).order(id: :desc)`
        - [[User]] モデルの `search` メソッドで、検索条件に合致するユーザー一覧を取得。
        - 検索条件は `search_params`（:name, :email, :leave, :type, :authority）で受け取る。
    - `@modeled_types = User.modeled_types`
        - [[User]] モデルの `modeled_types` メソッドで、ユーザー種別のリストを取得。

---

## 2. UIとデータの対応

- **検索フォーム:**
    - `render 'search_form', modeled_types: @modeled_types` (`app/views/users/index.html.erb:5`)
        - 検索条件（名前・メールアドレス・離職・タイプ・権限）を入力できるフォーム。
        - 詳細: `app/views/users/_search_form.html.erb:1-26`
        - `modeled_types`は「タイプ」プルダウンの選択肢として利用。

- **新規作成ボタン:**
    - `link_to('新規作成', new_user_path, class: 'Component__button-sub')` (`app/views/users/index.html.erb:8`)
        - ユーザー新規作成画面（[[UsersController]] `new`アクション）への遷移ボタン。

- **ユーザー一覧テーブル:**
    - `<% @users.each do |user| %> ... </tr> <% end %>` (`app/views/users/index.html.erb:21-34`)
        - [[User]] 一覧を1行ずつ表示。
        - 各カラムの対応：
            - **id:** `user.id` (`index.html.erb:23`)
            - **名前:** `link_to(user.name, edit_user_path(user), target: :_blank)` (`index.html.erb:24`)
                - ユーザー編集画面（[[UsersController]] `edit`アクション）へのリンク。
            - **メールアドレス:** `user.email` (`index.html.erb:25`)
            - **タイプ:** `user.type` (`index.html.erb:26`)
            - **権限:** `user.authority` (`index.html.erb:27`)
            - **最終ログイン:** `user.last_sign_in_at&.strftime('%F') || '-'` (`index.html.erb:28`)
            - **離職:** `show_boolean(user.leave, '◯', '×')` (`index.html.erb:29`)
                - [[show_boolean]]: `app/helpers/application_helper.rb:27` で定義。真偽値を「◯」「×」で表示。

---

## 関連リンク
- [[UsersController]]
- [[User]]
- [[show_boolean]]

---

## 参考ファイル
- コントローラ: `app/controllers/users_controller.rb`
- モデル: `app/models/user.rb`
- ビュー: `app/views/users/index.html.erb`, `app/views/users/_search_form.html.erb`
- ヘルパー: `app/helpers/application_helper.rb` 