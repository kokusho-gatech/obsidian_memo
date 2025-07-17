# 重要事項調査報告書の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/report_of_important_info_survey/edit`
- **コントローラー**: `Articles::Inputs::ReportOfImportantInfoSurveysController#edit`
- **ビュー**: `app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb`
- **機能**: 重要事項調査報告書の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 保存ボタン
- 築年数警告（築年数が古い場合）

#### 重要事項調査報告書入力フォーム
##### 管理費・修繕積立金
- **管理費**: 管理費（円）
- **修繕積立金**: 修繕積立金（円）
- **修繕履歴**: 修繕履歴の有無
- **修繕履歴なし理由**: 修繕履歴がない場合の理由

##### その他の費用
- **その他費用**: その他の費用（円）
- **町内会費**: 町内会費（円）
- **町内会費現在支払経路**: 町内会費の現在の支払経路
- **町内会費承継後支払経路**: 町内会費の承継後の支払経路

##### 水道料金
- **水道料金**: 水道料金（円）
- **水道料金現在支払経路**: 水道料金の現在の支払経路
- **水道料金承継後支払経路**: 水道料金の承継後の支払経路

##### 修繕積立金・滞納
- **修繕積立金合計**: 修繕積立金の合計（円）
- **建物滞納**: 建物の滞納の有無
- **所有者滞納**: 所有者の滞納の有無
- **所有者滞納返済期間**: 所有者滞納の返済期間

##### 債務情報
- **債務**: 債務の有無
- **債務当初金額**: 債務の当初金額
- **債務残高**: 債務の残高
- **債務残高時点**: 債務残高の時点
- **債務先**: 債務先
- **債務目的**: 債務目的
- **債務返済期間**: 債務返済期間（開始日〜終了日）
- **債務返済期間聴取日**: 債務返済期間の聴取日
- **債務返済期間聴取先**: 債務返済期間の聴取先

##### 修繕・管理計画
- **費用変更予定**: 費用変更の予定
- **大規模修繕予定**: 大規模修繕の予定
- **心理的瑕疵**: 心理的瑕疵の有無
- **長期修繕計画**: 長期修繕計画の有無

##### 管理・運営
- **管理人勤務形態**: 管理人の勤務形態
- **管理人組合形態**: 管理人組合の形態
- **総会月**: 総会の月
- **取得日**: 取得日

#### 確認・稟議比較・チェックセクション
- **確認情報**: 入力内容の確認
- **稟議比較**: 稟議との比較（入力済みの場合のみ表示）
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::ReportOfImportantInfoSurveysController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 重要事項調査報告書の書類項目
@input_article_item = Input::ReportOfImportantInfoSurvey.find_or_initialize_by(...) # 重要事項調査報告書入力情報
@form_model = Input::ReportOfImportantInfoSurvey::Form.new(@input_article_item)     # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報

# 追加で他の情報を取得
@input_certified_copy = ::Input::CertifiedCopy.find_by(...)             # 謄本入力情報
@approval = @article.target_approval                                    # 稟議情報
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::ReportOfImportantInfoSurvey**: 重要事項調査報告書入力情報
- **Input::ReportOfImportantInfoSurvey::Form**: 重要事項調査報告書入力フォーム
- **Input::CertifiedCopy**: 謄本入力情報（参照用）
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-390:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_report_of_important_info_survey_path, method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
    <div class="form-header">
      <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
      <%= form.submit '入力項目を保存する', class: 'submit-button' %>
    </div>
    <!-- 築年数警告 -->
    <div class="form-main">
      <!-- 入力フィールド群 -->
    </div>
  <% end %>
<% end %>
```

### 築年数警告
```erb:12-16:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<% if @input_certified_copy&.building_age_old? %>
  <p class="tw-text-right tw-text-red-500">
    本日時点で、築<%= Input::CertifiedCopy::OLD_BUILDING_AGE %>年を経過する物件です。
  </p>
<% end %>
```

### 管理費・修繕積立金入力
```erb:17-30:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<div class="form-main">
  <div class="form-group">
    <%= form.label :administrative_cost, class: 'form-label' %>
    <div class="with-unit">
      <%= form.number_field :administrative_cost, disabled: !@is_editable_input_article_item %>
      <span class="unit">円</span>
    </div>
  </div>
  <div class="form-group">
    <%= form.label :repair_reserve_fund, class: 'form-label' %>
    <div class="with-unit">
      <%= form.number_field :repair_reserve_fund, disabled: !@is_editable_input_article_item %>
      <span class="unit">円</span>
    </div>
  </div>
</div>
```

### 修繕履歴選択（条件付き表示）
```erb:31-55:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<%= tag.div data: { controller: 'conditional-toggle', conditional_toggle_show_value_value: 'none' } do %>
  <div class="form-group">
    <%= form.label :repair_history, class: 'form-label' %>
    <div class="radio-buttons">
      <%= form.collection_radio_buttons :repair_history,
                                        Input::ReportOfImportantInfoSurvey.repair_history.options,
                                        :second,
                                        :first do |b| %>
        <div>
          <%= b.radio_button disabled: !@is_editable_input_article_item,
                             class: 'tw-peer',
                             data: { conditional_toggle_target: 'togglable', action: 'conditional-toggle#toggle' } %>
          <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
        </div>
      <% end %>
    </div>
  </div>
  <%= tag.div data: { conditional_toggle_target: 'item' } do %>
    <div class="tw-flex tw-items-start tw-w-full">
      <%= form.label :repair_history_none_reason, class: 'tw-flex-1 tw-basis-full' %>
      <%= form.text_area :repair_history_none_reason, rows: 8, disabled: !@is_editable_input_article_item %>
    </div>
  <% end %>
<% end %>
```

### その他費用入力
```erb:56-65:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<div class="form-group">
  <%= form.label :other_cost, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :other_cost, disabled: !@is_editable_input_article_item %>
    <span class="unit">円</span>
  </div>
</div>
```

### 町内会費入力
```erb:66-85:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<div class="form-group">
  <%= form.label :town_council_fee, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :town_council_fee, disabled: !@is_editable_input_article_item %>
    <span class="unit">円</span>
  </div>
</div>
<h2>関東物件以外の場合</h2>
<div class="tw-ml-3">
  <div class="form-group">
    <%= form.label :town_council_fee_current_payment_route, class: 'form-label' %>
    <%= form.select :town_council_fee_current_payment_route,
                    Input::ReportOfImportantInfoSurvey.town_council_fee_current_payment_route.options,
                    {},
                    disabled: !@is_editable_input_article_item %>
  </div>
  <div class="form-group">
    <%= form.label :town_council_fee_payment_route_after_succession, class: 'form-label' %>
    <%= form.select :town_council_fee_payment_route_after_succession,
                    Input::ReportOfImportantInfoSurvey.town_council_fee_payment_route_after_succession.options,
                    {},
                    disabled: !@is_editable_input_article_item %>
  </div>
</div>
```

### 水道料金入力
```erb:86-105:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<div class="form-group">
  <%= form.label :water_bill, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :water_bill, disabled: !@is_editable_input_article_item %>
    <span class="unit">円</span>
  </div>
</div>
<h2>関東物件以外の場合</h2>
<div class="tw-ml-3">
  <div class="form-group">
    <%= form.label :water_bill_current_payment_route, class: 'form-label' %>
    <%= form.select :water_bill_current_payment_route,
                    Input::ReportOfImportantInfoSurvey.water_bill_current_payment_route.options,
                    {},
                    disabled: !@is_editable_input_article_item %>
  </div>
  <div class="form-group">
    <%= form.label :water_bill_payment_route_after_succession, class: 'form-label' %>
    <%= form.select :water_bill_payment_route_after_succession,
                    Input::ReportOfImportantInfoSurvey.water_bill_payment_route_after_succession.options,
                    {},
                    disabled: !@is_editable_input_article_item %>
  </div>
</div>
```

### 修繕積立金合計入力
```erb:106-114:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<div class="form-group">
  <%= form.label :total_repair_reserve_fund, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :total_repair_reserve_fund, disabled: !@is_editable_input_article_item %>
    <span class="unit">円</span>
  </div>
</div>
```

### 建物滞納選択
```erb:115-129:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<div class="form-group">
  <%= form.label :building_arrears, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :building_arrears,
                                      Input::ReportOfImportantInfoSurvey.building_arrears.options,
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

### 所有者滞納選択（条件付き表示）
```erb:130-160:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<%= tag.div data: { controller: 'conditional-toggle', conditional_toggle_show_value_value: 'exist' } do %>
  <div class="form-group">
    <%= form.label :owner_arrears, class: 'form-label' %>
    <div class="radio-buttons">
      <%= form.collection_radio_buttons :owner_arrears,
                                        Input::ReportOfImportantInfoSurvey.owner_arrears.options,
                                        :second,
                                        :first do |b| %>
        <div>
          <%= b.radio_button disabled: !@is_editable_input_article_item,
                             class: 'tw-peer',
                             data: { conditional_toggle_target: 'togglable', action: 'conditional-toggle#toggle' } %>
          <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
        </div>
      <% end %>
    </div>
  </div>
  <%= tag.div data: { conditional_toggle_target: 'item' } do %>
    <div class="form-group">
      <%= form.label :owner_arrears_repayment_period, class: 'form-label' %>
      <div class="radio-buttons">
        <%= form.collection_radio_buttons :owner_arrears_repayment_period,
                                          Input::ReportOfImportantInfoSurvey.owner_arrears_repayment_period.options,
                                          :second,
                                          :first do |b| %>
          <div>
            <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
            <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
          </div>
        <% end %>
      </div>
    </div>
  <% end %>
<% end %>
```

### 債務選択（条件付き表示）
```erb:161-390:app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb
<%= tag.div data: { controller: 'conditional-toggle', conditional_toggle_show_value_value: 'exist' } do %>
  <div class="form-group">
    <%= form.label :debt, class: 'form-label' %>
    <div class="radio-buttons">
      <%= form.collection_radio_buttons :debt,
                                        Input::ReportOfImportantInfoSurvey.debt.options,
                                        :second,
                                        :first do |b| %>
        <div>
          <%= b.radio_button disabled: !@is_editable_input_article_item,
                             class: 'tw-peer',
                             data: { conditional_toggle_target: 'togglable', action: 'conditional-toggle#toggle' } %>
          <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
        </div>
      <% end %>
    </div>
  </div>
  <!-- 債務詳細情報（債務がある場合のみ表示） -->
<% end %>
```

## 主要なアクション

### 重要事項調査報告書入力更新（PATCH `/articles/:id/inputs/report_of_important_info_survey`）
- **コントローラー**: `Articles::Inputs::ReportOfImportantInfoSurveysController#update`
- **処理**: 重要事項調査報告書の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 管理費・修繕積立金
- **管理費**: 管理費（円）
- **修繕積立金**: 修繕積立金（円）
- **修繕履歴**: 修繕履歴の有無（あり/なし/不明）
- **修繕履歴なし理由**: 修繕履歴がない場合の理由（テキストエリア）

### その他の費用
- **その他費用**: その他の費用（円）
- **町内会費**: 町内会費（円）
- **町内会費現在支払経路**: 町内会費の現在の支払経路（関東物件以外）
- **町内会費承継後支払経路**: 町内会費の承継後の支払経路（関東物件以外）

### 水道料金
- **水道料金**: 水道料金（円）
- **水道料金現在支払経路**: 水道料金の現在の支払経路（関東物件以外）
- **水道料金承継後支払経路**: 水道料金の承継後の支払経路（関東物件以外）

### 修繕積立金・滞納
- **修繕積立金合計**: 修繕積立金の合計（円）
- **建物滞納**: 建物の滞納の有無（あり/なし/不明）
- **所有者滞納**: 所有者の滞納の有無（あり/なし/不明）
- **所有者滞納返済期間**: 所有者滞納の返済期間（あり/なし/不明）

### 債務情報
- **債務**: 債務の有無（あり/なし/不明）
- **債務当初金額**: 債務の当初金額
- **債務残高**: 債務の残高
- **債務残高時点**: 債務残高の時点
- **債務先**: 債務先
- **債務目的**: 債務目的
- **債務返済期間**: 債務返済期間（開始日〜終了日）
- **債務返済期間聴取日**: 債務返済期間の聴取日
- **債務返済期間聴取先**: 債務返済期間の聴取先

### 修繕・管理計画
- **費用変更予定**: 費用変更の予定（あり/なし/不明）
- **大規模修繕予定**: 大規模修繕の予定（あり/なし/不明）
- **心理的瑕疵**: 心理的瑕疵の有無（あり/なし/不明）
- **長期修繕計画**: 長期修繕計画の有無（あり/なし/不明）

### 管理・運営
- **管理人勤務形態**: 管理人の勤務形態
- **管理人組合形態**: 管理人組合の形態
- **総会月**: 総会の月
- **取得日**: 取得日

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[CertifiedCopyEditPage]] - 謄本の書類入力編集ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/report_of_important_info_surveys_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/report_of_important_info_surveys/edit.html.erb`
- **重要事項調査報告書入力モデル**: `app/models/input/report_of_important_info_survey.rb`
- **重要事項調査報告書入力フォーム**: `app/models/input/report_of_important_info_survey/form.rb` 