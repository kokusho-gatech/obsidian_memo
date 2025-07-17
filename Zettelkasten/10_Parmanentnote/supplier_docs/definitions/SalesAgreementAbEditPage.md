# 売買契約書の書類入力(AB間)編集ページ

## 概要
- **URL**: `/articles/:id/inputs/sales_agreement_ab/edit`
- **コントローラー**: `Articles::Inputs::SalesAgreementAbsController#edit`
- **ビュー**: `app/views/articles/inputs/sales_agreement_abs/edit.html.erb`
- **機能**: 売買契約書の書類入力(AB間)情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 売買契約書(ドラフト)入力結果のポップオーバー表示
- 保存ボタン

#### 売買契約書(AB間)入力フォーム
##### 契約情報
- **仕入取引日**: 仕入取引日

##### 契約内容
- **中間省略備考**: 中間省略の備考
- **予約備考**: 予約の備考
- **署名捺印**: 署名捺印の有無
- **印紙**: 印紙の有無

#### 確認・チェックセクション
- **確認情報**: 入力内容の確認
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::SalesAgreementAbsController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 売買契約書ABの書類項目
@input_article_item = Input::SalesAgreementAb.find_or_initialize_by(...) # 売買契約書AB入力情報
@form_model = Input::SalesAgreementAb::Form.new(@input_article_item)    # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報

# 追加で売買契約書(ドラフト)入力情報を取得
@input_sales_agreement_on_purchase = ::Input::SalesAgreementOnPurchase.find_by(
  article_item: @article.article_items.find_by(
    item: Item.find_by(name: Item::SALES_AGREEMENT_ON_PURCHASE)
  )
)
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::SalesAgreementAb**: 売買契約書AB入力情報
- **Input::SalesAgreementAb::Form**: 売買契約書AB入力フォーム
- **Input::SalesAgreementOnPurchase**: 売買契約書(ドラフト)入力情報（参照用）
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-105:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_sales_agreement_ab_path(@article), method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
    <div class="form-header">
      <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
      <div class="tw-flex tw-items-center" data-controller="popover">
        <!-- 売買契約書(ドラフト)入力結果のポップオーバー -->
        <%= form.submit '入力項目を保存する', class: 'submit-button' %>
      </div>
    </div>
    <div class="form-main">
      <!-- 入力フィールド群 -->
    </div>
  <% end %>
<% end %>
```

### 売買契約書(ドラフト)入力結果のポップオーバー
```erb:10-25:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<div class="tw-flex tw-items-center" data-controller="popover">
  <div class="tw-relative" data-action="mouseenter->popover#show mouseleave->popover#hide">
    <div class="tw-px-2 tw-text-xl">
      <i class="bi bi-exclamation-circle-fill"></i>
    </div>
    <div data-popover-target="content" class='tw-hidden'>
      <div class="tw-absolute tw-p-4 tw-rounded-md tw-bg-white tw-w-96 tw--left-56 tw-shadow-xl">
        <h3><%= Item::SALES_AGREEMENT_ON_PURCHASE %>の入力結果</h3>
        <% if @input_sales_agreement_on_purchase.nil? %>
          <p><%= Item::SALES_AGREEMENT_ON_PURCHASE %>はまだ入力されていません。</p>
        <% else %>
          <dl class="tw-flex tw-items-center tw-justify-between">
            <dt>約定日</dt>
            <dd><%= @input_sales_agreement_on_purchase.procurement_transaction_date&.strftime('%Y/%m/%d') %></dd>
          </dl>
        <% end %>
      </div>
    </div>
  </div>
  <%= form.submit '入力項目を保存する', class: 'submit-button' %>
</div>
```

### 仕入取引日入力
```erb:26-32:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<div class="form-main">
  <div class="form-group">
    <%= form.label :procurement_transaction_date, class: 'form-label' %>
    <%= form.date_field :procurement_transaction_date, disabled: !@is_editable_input_article_item %>
  </div>
</div>
```

### 中間省略備考選択
```erb:33-47:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<div class="form-group">
  <%= form.label :middle_omission_remarks, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :middle_omission_remarks,
                                      Input::SalesAgreementAb.middle_omission_remarks.options,
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

### 予約備考選択
```erb:48-62:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<div class="form-group">
  <%= form.label :reservation_remarks, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :reservation_remarks,
                                      Input::SalesAgreementAb.reservation_remarks.options,
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

### 署名捺印選択
```erb:63-77:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<div class="form-group">
  <%= form.label :signature_seal, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :signature_seal,
                                      Input::SalesAgreementAb.signature_seal.options,
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

### 印紙選択
```erb:78-92:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<div class="form-group">
  <%= form.label :issue_stamp, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :issue_stamp,
                                      Input::SalesAgreementAb.issue_stamp.options,
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
```erb:93-105:app/views/articles/inputs/sales_agreement_abs/edit.html.erb
<%= render 'articles/inputs/confirmation',
           input_article_item: @input_article_item,
           input_confirmation_article_item: @input_confirmation_article_item,
           url: inputs_sales_agreement_ab_confirmation_path(@article) %>
<%= render 'articles/inputs/check',
           input_article_item: @input_article_item,
           input_check_article_item: @input_check_article_item,
           url: inputs_sales_agreement_ab_checks_path %>
```

## 主要なアクション

### 売買契約書AB入力更新（PATCH `/articles/:id/inputs/sales_agreement_ab`）
- **コントローラー**: `Articles::Inputs::SalesAgreementAbsController#update`
- **処理**: 売買契約書ABの入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 契約情報
- **仕入取引日**: 仕入取引日

### 契約内容
- **中間省略備考**: 中間省略の備考（あり/なし/不明）
- **予約備考**: 予約の備考（あり/なし/不明）
- **署名捺印**: 署名捺印の有無（あり/なし/不明）
- **印紙**: 印紙の有無（あり/なし/不明）

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[SalesAgreementOnPurchaseEditPage]] - 売買契約書(ドラフト)の書類入力編集ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/sales_agreement_abs_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/sales_agreement_abs/edit.html.erb`
- **売買契約書AB入力モデル**: `app/models/input/sales_agreement_ab.rb`
- **売買契約書AB入力フォーム**: `app/models/input/sales_agreement_ab/form.rb` 