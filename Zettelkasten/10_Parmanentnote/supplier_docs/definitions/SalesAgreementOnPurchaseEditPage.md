# 売買契約書(ドラフト)の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/sales_agreement_on_purchase/edit`
- **コントローラー**: `Articles::Inputs::SalesAgreementOnPurchasesController#edit`
- **ビュー**: `app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb`
- **機能**: 売買契約書(ドラフト)の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 謄本入力結果のポップオーバー表示
- 保存ボタン

#### 売買契約書(ドラフト)入力フォーム
##### 基本情報
- **建物面積**: 建物面積（m²）
- **部屋番号**: 部屋番号
- **売買価格**: 売買価格（万円）
- **消費税**: 消費税（円）
- **手付金**: 手付金（円）
- **所有者名**: 所有者名

##### 契約条件
- **印紙代支払方法**: 印紙代の支払方法
- **決済パターン**: 決済パターン
- **仕入取引日**: 仕入取引日
- **仕入取引日種別**: 仕入取引日の種別
- **税決済開始月**: 税決済開始月

##### 契約内容
- **中間省略**: 中間省略の有無
- **予約可能性**: 予約可能性
- **重要事項調査報告書備考**: 重要事項調査報告書の備考
- **賃貸借契約書備考**: 賃貸借契約書の備考
- **建物管理会社解除備考**: 建物管理会社解除の備考
- **明渡し所有者負担備考**: 明渡し所有者負担の備考

##### 特殊契約
- **売買契約書AB**: 売買契約書ABの有無
- **売買契約書AB契約備考**: 売買契約書AB契約の備考
- **特約内容**: 特約内容
- **登記名義人差押履歴**: 登記名義人の差押履歴
- **決済日末日設定**: 決済日末日の設定
- **手付金受取人**: 手付金受取人

#### 確認・稟議比較セクション
- **確認情報**: 入力内容の確認
- **稟議比較**: 稟議との比較

## データフロー

### コントローラー（`Articles::Inputs::SalesAgreementOnPurchasesController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 売買契約書の書類項目
@input_article_item = Input::SalesAgreementOnPurchase.find_or_initialize_by(...) # 売買契約書入力情報
@form_model = Input::SalesAgreementOnPurchase::Form.new(@input_article_item)     # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報

# 追加で謄本入力情報を取得
@input_certified_copy = ::Input::CertifiedCopy.find_by(
  article_item: @article.article_items.find_by(
    item: Item.find_by(name: Item::COPY_OF_REGISTRATION)
  )
)
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::SalesAgreementOnPurchase**: 売買契約書入力情報
- **Input::SalesAgreementOnPurchase::Form**: 売買契約書入力フォーム
- **Input::CertifiedCopy**: 謄本入力情報（参照用）
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-502:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_sales_agreement_on_purchase_path, method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
    <div class="form-header">
      <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
      <div class="tw-flex tw-items-center" data-controller="popover">
        <!-- 謄本入力結果のポップオーバー -->
        <%= form.submit '入力項目を保存する', class: 'submit-button' %>
      </div>
    </div>
    <div class="form-main">
      <!-- 入力フィールド群 -->
    </div>
  <% end %>
<% end %>
```

### 謄本入力結果のポップオーバー
```erb:10-25:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<div class="tw-flex tw-items-center" data-controller="popover">
  <div class="tw-relative" data-action="mouseenter->popover#show mouseleave->popover#hide">
    <div class="tw-px-2 tw-text-xl">
      <i class="bi bi-exclamation-circle-fill"></i>
    </div>
    <div data-popover-target="content" class='tw-hidden'>
      <div class="tw-absolute tw-p-4 tw-rounded-md tw-bg-white tw-w-96 tw--left-56 tw-shadow-xl">
        <h3><%= Item::COPY_OF_REGISTRATION %>の入力結果</h3>
        <% if @input_certified_copy.nil? %>
          <p><%= Item::COPY_OF_REGISTRATION %>は入力されていません</p>
        <% else %>
          <dl class="tw-flex tw-items-center tw-justify-between">
            <dt>登記名義人</dt>
            <dd><%= @input_certified_copy.registered_owner_name %></dd>
          </dl>
          <dl class="tw-flex tw-items-center tw-justify-between">
            <dt>延床面積</dt>
            <dd><%= @input_certified_copy.building_area_floor&.to_s&.concat('㎡') %></dd>
          </dl>
        <% end %>
      </div>
    </div>
  </div>
  <%= form.submit '入力項目を保存する', class: 'submit-button' %>
</div>
```

### 基本情報入力
```erb:26-45:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<div class="form-group">
  <%= form.label :building_area_floor, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :building_area_floor, step: 0.01, disabled: !@is_editable_input_article_item %>
    <span class="unit">m&sup2</span>
  </div>
</div>
<div class="form-group">
  <%= form.label :room_number, class: 'form-label' %>
  <%= form.text_field :room_number, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :sale_price, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :sale_price, value: divide_10000(@input_article_item.sale_price), disabled: !@is_editable_input_article_item %>
    <span class="unit">万円</span>
  </div>
</div>
```

### 価格・手付金入力
```erb:46-60:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<div class="form-group">
  <%= form.label :consumption_tax, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :consumption_tax, disabled: !@is_editable_input_article_item %>
    <span class="unit">円</span>
  </div>
</div>
<div class="form-group">
  <%= form.label :deposit, class: 'form-label' %>
  <div class="with-unit">
    <%= form.number_field :deposit, disabled: !@is_editable_input_article_item %>
    <span class="unit">円</span>
  </div>
</div>
<div class="form-group">
  <%= form.label :owner_name, class: 'form-label' %>
  <%= form.text_field :owner_name, disabled: !@is_editable_input_article_item %>
</div>
```

### 契約条件選択
```erb:61-75:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<div class="form-group">
  <%= form.label :issue_stamp_cost_payment_method, class: 'form-label' %>
  <%= form.select :issue_stamp_cost_payment_method,
                  Input::SalesAgreementOnPurchase.issue_stamp_cost_payment_method.options,
                  {},
                  disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :settlement_pattern, class: 'form-label' %>
  <%= form.select :settlement_pattern,
                  Input::SalesAgreementOnPurchase.settlement_pattern.options,
                  {},
                  disabled: !@is_editable_input_article_item %>
</div>
```

### 日付入力
```erb:76-85:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<div class="form-group">
  <%= form.label :procurement_transaction_date, class: 'form-label' %>
  <%= form.date_field :procurement_transaction_date, disabled: !@is_editable_input_article_item %>
</div>
<div class="form-group">
  <%= form.label :procurement_transaction_date_kind, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :procurement_transaction_date_kind,
                                      Input::SalesAgreementOnPurchase.procurement_transaction_date_kind.options,
                                      :second,
                                      :first  do |b| %>
      <div>
        <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
        <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
      </div>
    <% end %>
  </div>
</div>
```

### ラジオボタン選択
```erb:86-150:app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb
<div class="form-group">
  <%= form.label :tax_settlement_start_date_month, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :tax_settlement_start_date_month,
                                      Input::SalesAgreementOnPurchase.tax_settlement_start_date_month.options,
                                      :second,
                                      :first  do |b| %>
      <div>
        <%= b.radio_button class: 'tw-peer', disabled: !@is_editable_input_article_item %>
        <%= b.label class: b.value == 'unknown' ? "peer-checked:tw-bg-button-gray" : "peer-checked:tw-bg-button-green" %>
      </div>
    <% end %>
  </div>
</div>
<!-- 他のラジオボタン選択も同様 -->
```

## 主要なアクション

### 売買契約書入力更新（PATCH `/articles/:id/inputs/sales_agreement_on_purchase`）
- **コントローラー**: `Articles::Inputs::SalesAgreementOnPurchasesController#update`
- **処理**: 売買契約書の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可
- **価格変換**: 売買価格は万円から円に変換して保存

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 基本情報
- **建物面積**: 建物面積（小数点2桁まで）
- **部屋番号**: 部屋番号
- **売買価格**: 売買価格（万円単位で入力、内部で円に変換）
- **消費税**: 消費税（円）
- **手付金**: 手付金（円）
- **所有者名**: 所有者名

### 契約条件
- **印紙代支払方法**: 印紙代の支払方法
- **決済パターン**: 決済パターン
- **仕入取引日**: 仕入取引日
- **仕入取引日種別**: 仕入取引日の種別
- **税決済開始月**: 税決済開始月

### 契約内容
- **中間省略**: 中間省略の有無
- **予約可能性**: 予約可能性
- **重要事項調査報告書備考**: 重要事項調査報告書の備考
- **賃貸借契約書備考**: 賃貸借契約書の備考
- **建物管理会社解除備考**: 建物管理会社解除の備考
- **明渡し所有者負担備考**: 明渡し所有者負担の備考

### 特殊契約
- **売買契約書AB**: 売買契約書ABの有無
- **売買契約書AB契約備考**: 売買契約書AB契約の備考
- **特約内容**: 特約内容
- **登記名義人差押履歴**: 登記名義人の差押履歴
- **決済日末日設定**: 決済日末日の設定
- **手付金受取人**: 手付金受取人

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[CertifiedCopyEditPage]] - 謄本の書類入力編集ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/sales_agreement_on_purchases_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/sales_agreement_on_purchases/edit.html.erb`
- **売買契約書入力モデル**: `app/models/input/sales_agreement_on_purchase.rb`
- **売買契約書入力フォーム**: `app/models/input/sales_agreement_on_purchase/form.rb` 