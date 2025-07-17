# 賃貸借契約書(出先)の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/tenant_lease_agreement/edit`
- **コントローラー**: `Articles::Inputs::TenantLeaseAgreementsController#edit`
- **ビュー**: `app/views/articles/inputs/tenant_lease_agreements/edit.html.erb`
- **機能**: 賃貸借契約書(出先)の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 謄本入力結果・物件情報のポップオーバー表示
- 保存ボタン

#### 賃貸借契約書(出先)入力フォーム
##### 賃料・保証金情報
- **賃料**: 賃料（円）
- **保証金**: 保証金（円）
- **敷金**: 敷金（円）

##### 契約期間
- **賃貸借契約期間**: 契約期間（開始日〜終了日）
- **契約期間警告**: 決済月から一定期間内に期限を迎える場合の警告

##### 賃借人情報
- **賃借人種別**: 賃借人の種別
- **賃借人反社チェック**: 賃借人の反社チェック状況

##### 更新・管理情報
- **更新管理会社**: 更新管理会社の有無
- **更新方法**: 更新方法
- **賃貸借契約書原本**: 賃貸借契約書原本の有無
- **賃貸借契約書備考**: 賃貸借契約書の備考
- **敷金承継**: 敷金承継の有無

##### 保険情報
- **保険会社**: 保険会社の有無
- **保険会社名**: 保険会社名（保険会社がある場合のみ表示）

#### 確認・稟議比較・チェックセクション
- **確認情報**: 入力内容の確認
- **稟議比較**: 稟議との比較（入力済みの場合のみ表示）
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::TenantLeaseAgreementsController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 賃貸借契約書の書類項目
@input_article_item = Input::TenantLeaseAgreement.find_or_initialize_by(...) # 賃貸借契約書入力情報
@form_model = Input::TenantLeaseAgreement::Form.new(@input_article_item)     # フォームモデル
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
- **Input::TenantLeaseAgreement**: 賃貸借契約書入力情報
- **Input::TenantLeaseAgreement::Form**: 賃貸借契約書入力フォーム
- **Input::CertifiedCopy**: 謄本入力情報（参照用）
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-279:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_tenant_lease_agreement_path(@article), method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
    <div class="form-header">
      <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
      <div class="tw-flex tw-items-center" data-controller="popover">
        <!-- 謄本入力結果・物件情報のポップオーバー -->
        <%= form.submit '入力項目を保存する', class: 'submit-button' %>
      </div>
    </div>
    <div class="form-main">
      <!-- 入力フィールド群 -->
    </div>
  <% end %>
<% end %>
```

### 謄本入力結果・物件情報のポップオーバー
```erb:10-30:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="tw-flex tw-items-center" data-controller="popover">
  <div class="tw-relative" data-action="mouseenter->popover#show mouseleave->popover#hide">
    <div class="tw-px-2 tw-text-xl">
      <i class="bi bi-exclamation-circle-fill"></i>
    </div>
    <div data-popover-target="content" class='tw-hidden'>
      <div class="tw-absolute tw-p-4 tw-rounded-md tw-bg-white tw-w-96 tw--left-56 tw-shadow-xl">
        <h3><%= Item::COPY_OF_REGISTRATION %>の入力結果</h3>
        <% if @input_certified_copy.nil? %>
          <p><%= Item::COPY_OF_REGISTRATION %>はまだ入力されていません。</p>
        <% else %>
          <dl class="tw-flex tw-items-center tw-justify-between">
            <dt>登記名義人</dt>
            <dd><%= @input_certified_copy.registered_owner_name %></dd>
          </dl>
        <% end %>
        <h3 class="tw-mt-2.5">物件の情報</h3>
        <dl class="tw-flex tw-items-center tw-justify-between">
          <dt>決済月</dt>
          <dd><%= display_year_month(@article.settlement_month) %></dd>
        </dl>
      </div>
    </div>
  </div>
  <%= form.submit '入力項目を保存する', class: 'submit-button' %>
</div>
```

### 賃料・保証金入力
```erb:31-50:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-main">
  <div class="form-group">
    <%= form.label :rental_price, class: 'form-label' %>
    <div class="with-unit">
      <%= form.number_field :rental_price, disabled: !@is_editable_input_article_item %>
      <span class="unit">円</span>
    </div>
  </div>
  <div class="form-group">
    <%= form.label :security_deposit, class: 'form-label' %>
    <div class="with-unit">
      <%= form.number_field :security_deposit, disabled: !@is_editable_input_article_item %>
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
</div>
```

### 契約期間入力
```erb:51-60:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :lease_agreement_period_from, class: 'form-label' %>
  <div class="date-period">
    <%= form.date_field :lease_agreement_period_from, disabled: !@is_editable_input_article_item %>
    <span class="date-span">~</span>
    <%= form.date_field :lease_agreement_period_to, disabled: !@is_editable_input_article_item %>
  </div>
</div>
<% if @input_article_item.lease_agreement_period_from_settlement_end? %>
  <p class="tw-text-right tw-text-red-500">
    当物件は、決済月から<%= Input::TenantLeaseAgreement::ALERT_LEASE_AGREEMENT_PERIOD_FROM_SETTLEMENT_MONTHS %>ヶ月以内に賃貸借契約期間の期限を迎えます。
  </p>
<% end %>
```

### 賃借人種別選択
```erb:61-68:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :tenant_kind, class: 'form-label' %>
  <%= form.select :tenant_kind,
                  Input::TenantLeaseAgreement.tenant_kind.options,
                  {},
                  disabled: !@is_editable_input_article_item %>
</div>
```

### 賃借人反社チェック選択
```erb:69-83:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :tenant_anti_company_check, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :tenant_anti_company_check,
                                      Input::TenantLeaseAgreement.tenant_anti_company_check.options,
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

### 更新管理会社選択
```erb:84-98:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :renewal_management_company, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :renewal_management_company,
                                      Input::TenantLeaseAgreement.renewal_management_company.options,
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

### 更新方法選択
```erb:99-113:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :renewal_method, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :renewal_method,
                                      Input::TenantLeaseAgreement.renewal_method.options,
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

### 賃貸借契約書原本選択
```erb:114-128:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :lease_agreement_original_copy, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :lease_agreement_original_copy,
                                      Input::TenantLeaseAgreement.lease_agreement_original_copy.options,
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

### 賃貸借契約書備考選択
```erb:129-143:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :lease_agreement_remarks, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :lease_agreement_remarks,
                                      Input::TenantLeaseAgreement.lease_agreement_remarks.options,
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

### 敷金承継選択
```erb:144-158:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<div class="form-group">
  <%= form.label :deposit_inheritance, class: 'form-label' %>
  <div class="radio-buttons">
    <%= form.collection_radio_buttons :deposit_inheritance,
                                      Input::TenantLeaseAgreement.deposit_inheritance.options,
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

### 保険会社情報（条件付き表示）
```erb:159-185:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<%= tag.div data: { controller: 'conditional-toggle', conditional_toggle_show_value_value: 'exist' } do %>
  <div class="form-group">
    <%= form.label :insurance_company, class: 'form-label' %>
    <div class="radio-buttons">
      <%= form.collection_radio_buttons :insurance_company,
                                        Input::TenantLeaseAgreement.insurance_company.options,
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
      <%= form.label :insurance_company_name, class: 'form-label' %>
      <%= form.text_field :insurance_company_name, disabled: !@is_editable_input_article_item %>
    </div>
  <% end %>
<% end %>
```

### 確認セクション
```erb:186-192:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<%= render 'articles/inputs/confirmation',
           input_article_item: @input_article_item,
           input_confirmation_article_item: @input_confirmation_article_item,
           url: inputs_tenant_lease_agreement_confirmation_path(@article) %>
```

### 稟議比較セクション（入力済みの場合のみ）
```erb:193-279:app/views/articles/inputs/tenant_lease_agreements/edit.html.erb
<% if @input_article_item.persisted? %>
  <!-- 稟議比較の内容 -->
<% end %>
```

## 主要なアクション

### 賃貸借契約書入力更新（PATCH `/articles/:id/inputs/tenant_lease_agreement`）
- **コントローラー**: `Articles::Inputs::TenantLeaseAgreementsController#update`
- **処理**: 賃貸借契約書の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 賃料・保証金情報
- **賃料**: 賃料（円）
- **保証金**: 保証金（円）
- **敷金**: 敷金（円）

### 契約期間
- **賃貸借契約期間**: 契約期間（開始日〜終了日）
- **契約期間警告**: 決済月から一定期間内に期限を迎える場合の警告表示

### 賃借人情報
- **賃借人種別**: 賃借人の種別
- **賃借人反社チェック**: 賃借人の反社チェック状況（あり/なし/不明）

### 更新・管理情報
- **更新管理会社**: 更新管理会社の有無（あり/なし/不明）
- **更新方法**: 更新方法
- **賃貸借契約書原本**: 賃貸借契約書原本の有無（あり/なし/不明）
- **賃貸借契約書備考**: 賃貸借契約書の備考（あり/なし/不明）
- **敷金承継**: 敷金承継の有無（あり/なし/不明）

### 保険情報
- **保険会社**: 保険会社の有無（あり/なし/不明）
- **保険会社名**: 保険会社名（保険会社がある場合のみ表示）

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[CertifiedCopyEditPage]] - 謄本の書類入力編集ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/tenant_lease_agreements_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/tenant_lease_agreements/edit.html.erb`
- **賃貸借契約書入力モデル**: `app/models/input/tenant_lease_agreement.rb`
- **賃貸借契約書入力フォーム**: `app/models/input/tenant_lease_agreement/form.rb` 