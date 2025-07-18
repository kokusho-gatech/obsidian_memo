# 謄本の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/certified_copy/edit`
- **コントローラー**: `Articles::Inputs::CertifiedCopiesController#edit`
- **ビュー**: `app/views/articles/inputs/certified_copies/edit.html.erb`
- **機能**: 謄本の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 保存ボタン

#### 謄本入力フォーム
##### 基本情報
- **建物名**: 建物の名称
- **専有部分名**: 専有部分の名称
- **土地総数**: 土地の総数
- **土地住所**: 土地の住所（5段階）
- **建物面積**: 建物面積（m²）
- **用途地域**: 用途地域の選択

##### 登記情報
- **登記名義人**: 登記上の所有者名
- **登記名義人住所**: 登記名義人の住所
- **抵当権者**: 抵当権者の情報
- **登記日**: 登記日

##### 権利関係
- **敷地権割合**: 敷地権の割合（分母・分子）
- **所有者反社チェック**: 所有者の反社チェック状況
- **海外所有者反社チェック**: 海外所有者の反社チェック状況
- **差押**: 差押の有無

##### 共同担保情報
- **共同担保**: 共同担保の有無
- **共同担保解除方法**: 解除方法の選択
- **全部解除時の決済日**: 全部解除時の決済日統一

#### 確認・稟議比較セクション
- **確認情報**: 入力内容の確認
- **稟議比較**: 稟議との比較

## データフロー

### コントローラー（`Articles::Inputs::CertifiedCopiesController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 謄本の書類項目
@input_article_item = Input::CertifiedCopy.find_or_initialize_by(...)   # 謄本入力情報
@form_model = Input::CertifiedCopy::Form.new(@input_article_item)       # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::CertifiedCopy**: 謄本入力情報
- **Input::CertifiedCopy::Form**: 謄本入力フォーム
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-252:app/views/articles/inputs/certified_copies/edit.html.erb
<%= form_with model: @form_model, url: inputs_certified_copy_path(@article), method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
  <div class="form-header">
    <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
    <%= form.submit '入力項目を保存する', class: 'submit-button' %>
  </div>
  <%= tag.div class: 'form-main' do %>
    <!-- 入力フィールド群 -->
  <% end %>
<% end %>
```

### 基本情報入力
```erb:12-25:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :building_name, class: 'form-label' %>
  <%= form.text_field :building_name, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :private_area_name, class: 'form-label' %>
  <%= form.text_field :private_area_name, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :total_lands, class: 'form-label' %>
  <%= form.number_field :total_lands, disabled: !@is_editable_input_article_item %>
</div>
```

### 土地住所入力
```erb:26-45:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :land_address_1, class: 'form-label' %>
  <%= form.text_field :land_address_1, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :land_address_2, class: 'form-label' %>
  <%= form.text_field :land_address_2, disabled: !@is_editable_input_article_item %>
</div>
<!-- 土地住所3-5も同様 -->
```

### 建物面積入力
```erb:46-52:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :building_area_floor, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :building_area_floor, step: 0.01, disabled: !@is_editable_input_article_item %>
    <span class="unit">m&sup2</span>
  </div>
</div>
```

### 用途地域選択
```erb:53-58:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :area, class: 'form-label' %>
  <%= form.select :area, Input::CertifiedCopy.area.options, {}, disabled: !@is_editable_input_article_item %>
</div>
```

### 登記情報入力
```erb:59-75:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :registered_owner_name, class: 'form-label' %>
  <%= form.text_field :registered_owner_name, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :registered_owner_address, class: 'form-label' %>
  <%= form.text_field :registered_owner_address, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :mortgage_owner, class: 'form-label' %>
  <%= form.text_field :mortgage_owner, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :registered_date, class: 'form-label' %>
  <%= form.date_field :registered_date, disabled: !@is_editable_input_article_item %>
</div>
```

### 権利関係入力
```erb:76-85:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :site_right_ratio_denominator, class: 'form-label' %>
  <%= form.number_field :site_right_ratio_denominator, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :site_right_ratio_numerator, class: 'form-label' %>
  <%= form.number_field :site_right_ratio_numerator, disabled: !@is_editable_input_article_item %>
</div>
```

### ラジオボタン選択
```erb:86-105:app/views/articles/inputs/certified_copies/edit.html.erb
<div class="form-group">
  <%= form.label :owner_anti_company_check_request, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :owner_anti_company_check_request,
                                      Input::CertifiedCopy.owner_anti_company_check_request.options,
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

### 条件付き表示
```erb:106-150:app/views/articles/inputs/certified_copies/edit.html.erb
<%= tag.div data: { controller: 'conditional-toggle', conditional_toggle_show_value_value: 'exist' } do %>
  <div class="form-group">
    <%= form.label :joint_mortgage, class: 'form-label' %>
    <div class="radio-buttons">
      <%= form.collection_radio_buttons :joint_mortgage,
                                        Input::CertifiedCopy.joint_mortgage.options,
                                        :second,
                                        :first do |b| %>
        <div>
          <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item,
                             data: { conditional_toggle_target: 'togglable', action: 'conditional-toggle#toggle' } %>
          <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
        </div>
      <% end %>
    </div>
  </div>
  <%= tag.div data: { conditional_toggle_target: 'item' } do %>
    <h2>共同担保がありの場合</h2>
    <!-- 共同担保関連の追加フィールド -->
  <% end %>
<% end %>
```

## 主要なアクション

### 謄本入力更新（PATCH `/articles/:id/inputs/certified_copy`）
- **コントローラー**: `Articles::Inputs::CertifiedCopiesController#update`
- **処理**: 謄本の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 基本情報
- **建物名**: 建物の正式名称
- **専有部分名**: 専有部分の名称
- **土地総数**: 土地の総数
- **土地住所**: 土地の住所（5段階で入力）
- **建物面積**: 建物面積（小数点2桁まで）
- **用途地域**: 用途地域の選択

### 登記情報
- **登記名義人**: 登記上の所有者名
- **登記名義人住所**: 登記名義人の住所
- **抵当権者**: 抵当権者の情報
- **登記日**: 登記日

### 権利関係
- **敷地権割合**: 敷地権の割合（分母・分子）
- **所有者反社チェック**: 所有者の反社チェック状況
- **海外所有者反社チェック**: 海外所有者の反社チェック状況
- **差押**: 差押の有無

### 共同担保情報
- **共同担保**: 共同担保の有無
- **共同担保解除方法**: 解除方法の選択
- **全部解除時の決済日**: 全部解除時の決済日統一

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/certified_copies_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/certified_copies/edit.html.erb`
- **謄本入力モデル**: `app/models/input/certified_copy.rb`
- **謄本入力フォーム**: `app/models/input/certified_copy/form.rb` 