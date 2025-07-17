# パンフレットの書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/pamphlet/edit`
- **コントローラー**: `Articles::Inputs::PamphletsController#edit`
- **ビュー**: `app/views/articles/inputs/pamphlets/edit.html.erb`
- **機能**: パンフレットの書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 保存ボタン

#### パンフレット入力フォーム
##### 物件概要
- **物件概要**: 物件概要の有無

##### 図面情報
- **1階平面図**: 1階平面図の有無
- **各階平面図**: 各階平面図の有無
- **部屋平面図**: 部屋平面図の有無

#### 確認・チェックセクション
- **確認情報**: 入力内容の確認
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::PamphletsController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # パンフレットの書類項目
@input_article_item = Input::Pamphlet.find_or_initialize_by(...)        # パンフレット入力情報
@form_model = Input::Pamphlet::Form.new(@input_article_item)            # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::Pamphlet**: パンフレット入力情報
- **Input::Pamphlet::Form**: パンフレット入力フォーム
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-81:app/views/articles/inputs/pamphlets/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_pamphlet_path(@article), method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
    <div class="form-header">
      <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
      <%= form.submit '入力項目を保存する', class: 'submit-button' %>
    </div>
    <div class="form-main">
      <!-- 入力フィールド群 -->
    </div>
  <% end %>
<% end %>
```

### 物件概要選択
```erb:12-25:app/views/articles/inputs/pamphlets/edit.html.erb
<div class="form-group">
  <%= form.label :article_summary, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :article_summary,
                                      Input::Pamphlet.article_summary.options,
                                      :second,
                                      :first do |b| %>
      <div>
        <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
        <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
      </div>
    <% end %>
  </div>
</div>
```

### 1階平面図選択
```erb:26-39:app/views/articles/inputs/pamphlets/edit.html.erb
<div class="form-group">
  <%= form.label :first_floor_plan, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :first_floor_plan,
                                      Input::Pamphlet.first_floor_plan.options,
                                      :second,
                                      :first do |b| %>
      <div>
        <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
        <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
      </div>
    <% end %>
  </div>
</div>
```

### 各階平面図選択
```erb:40-53:app/views/articles/inputs/pamphlets/edit.html.erb
<div class="form-group">
  <%= form.label :each_floor_plan, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :each_floor_plan,
                                      Input::Pamphlet.each_floor_plan.options,
                                      :second,
                                      :first do |b| %>
      <div>
        <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
        <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
      </div>
    <% end %>
  </div>
</div>
```

### 部屋平面図選択
```erb:54-67:app/views/articles/inputs/pamphlets/edit.html.erb
<div class="form-group">
  <%= form.label :room_plan, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :room_plan,
                                      Input::Pamphlet.room_plan.options,
                                      :second,
                                      :first do |b| %>
      <div>
        <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
        <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
      </div>
    <% end %>
  </div>
</div>
```

### 確認・チェックセクション
```erb:68-81:app/views/articles/inputs/pamphlets/edit.html.erb
<%= render 'articles/inputs/confirmation',
           input_article_item: @input_article_item,
           input_confirmation_article_item: @input_confirmation_article_item,
           url: inputs_pamphlet_confirmation_path(@article) %>
<%= render 'articles/inputs/check',
           input_article_item: @input_article_item,
           input_check_article_item: @input_check_article_item,
           url: inputs_pamphlet_checks_path %>
```

## 主要なアクション

### パンフレット入力更新（PATCH `/articles/:id/inputs/pamphlet`）
- **コントローラー**: `Articles::Inputs::PamphletsController#update`
- **処理**: パンフレットの入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 物件概要
- **物件概要**: 物件概要の有無（あり/なし/不明）

### 図面情報
- **1階平面図**: 1階平面図の有無（あり/なし/不明）
- **各階平面図**: 各階平面図の有無（あり/なし/不明）
- **部屋平面図**: 部屋平面図の有無（あり/なし/不明）

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/pamphlets_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/pamphlets/edit.html.erb`
- **パンフレット入力モデル**: `app/models/input/pamphlet.rb`
- **パンフレット入力フォーム**: `app/models/input/pamphlet/form.rb` 