# 報酬支払約定書(ドラフト)の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/compensation_payment_agreement/edit`
- **コントローラー**: `Articles::Inputs::CompensationPaymentAgreementsController#edit`
- **ビュー**: `app/views/articles/inputs/compensation_payment_agreements/edit.html.erb`
- **機能**: 報酬支払約定書(ドラフト)の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 売買契約書(ドラフト)・謄本入力結果のポップオーバー表示
- 保存ボタン

#### 報酬支払約定書(ドラフト)入力フォーム
##### 報酬情報
- **仲介手数料**: 仲介手数料（円）

#### 確認・稟議比較・チェックセクション
- **確認情報**: 入力内容の確認
- **稟議比較**: 稟議との比較
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::CompensationPaymentAgreementsController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 報酬支払約定書の書類項目
@input_article_item = Input::CompensationPaymentAgreement.find_or_initialize_by(...) # 報酬支払約定書入力情報
@form_model = Input::CompensationPaymentAgreement::Form.new(@input_article_item)     # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報

# 追加で他の書類入力情報を取得
@input_certified_copy = ::Input::CertifiedCopy.find_by(...)             # 謄本入力情報
@input_sales_agreement_on_purchase = ::Input::SalesAgreementOnPurchase.find_by(...) # 売買契約書入力情報
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::CompensationPaymentAgreement**: 報酬支払約定書入力情報
- **Input::CompensationPaymentAgreement::Form**: 報酬支払約定書入力フォーム
- **Input::CertifiedCopy**: 謄本入力情報（参照用）
- **Input::SalesAgreementOnPurchase**: 売買契約書入力情報（参照用）
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-101:app/views/articles/inputs/compensation_payment_agreements/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_compensation_payment_agreement_path(@article), method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
    <div class="form-header">
      <h2><%= link_to @article.building_name, @article, target: :_blank %></h2>
      <div class="tw-flex tw-items-center" data-controller="popover">
        <!-- 売買契約書・謄本入力結果のポップオーバー -->
        <%= form.submit '入力項目を保存する', class: 'submit-button' %>
      </div>
    </div>
    <div class="form-main">
      <!-- 入力フィールド群 -->
    </div>
  <% end %>
<% end %>
```

### 売買契約書・謄本入力結果のポップオーバー
```erb:10-35:app/views/articles/inputs/compensation_payment_agreements/edit.html.erb
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
            <dt>売買価格</dt>
            <dd><%= divide_10000(@input_sales_agreement_on_purchase.sale_price)&.to_fs(:delimited)&.concat('万円') %></dd>
          </dl>
        <% end %>
        <h3 class="tw-mt-2.5"><%= Item::COPY_OF_REGISTRATION %>の入力結果</h3>
        <% if @input_certified_copy.nil? %>
          <p><%= Item::COPY_OF_REGISTRATION %>はまだ入力されていません。</p>
        <% else %>
          <dl class="tw-flex tw-items-center tw-justify-between">
            <dt>建物の名称(一棟の建物の表示)</dt>
            <dd><%= @input_certified_copy.building_name %></dd>
          </dl>
          <dl class="tw-flex tw-items-center tw-justify-between">
            <dt>建物の名称(専用の建物の表示)</dt>
            <dd><%= @input_certified_copy.private_area_name %></dd>
          </dl>
        <% end %>
      </div>
    </div>
  </div>
  <%= form.submit '入力項目を保存する', class: 'submit-button' %>
</div>
```

### 仲介手数料入力
```erb:36-44:app/views/articles/inputs/compensation_payment_agreements/edit.html.erb
<div class="form-main">
  <div class="form-group">
    <%= form.label :intermediary_commissions, class: 'form-label' %>
    <div class="with-unit">
      <%= form.number_field :intermediary_commissions, disabled: !@is_editable_input_article_item %>
      <span class="unit">円</span>
    </div>
  </div>
</div>
```

### 確認セクション
```erb:45-50:app/views/articles/inputs/compensation_payment_agreements/edit.html.erb
<%= render 'articles/inputs/confirmation',
           input_article_item: @input_article_item,
           input_confirmation_article_item: @input_confirmation_article_item,
           url: inputs_compensation_payment_agreement_confirmation_path(@article) %>
```

### 稟議比較セクション
```erb:51-85:app/views/articles/inputs/compensation_payment_agreements/edit.html.erb
<%= tag.div class: 'input-compare' do %>
  <div class="form-header">
    <h2>稟議項目</h2>
  </div>
  <%= tag.div class: 'form-main' do %>
    <div class="compare-group">
      <div class="compare-title">
        仕入れ契約稟議
      </div>
      <div class="approval-statuses">
        <div class="approval-status <%= @article.target_approval&.status&.approved? ? 'tw-bg-lime-600' : 'tw-bg-gray-400' %>">
          承認済み
        </div>
        <div class="approval-status <%=  !@article.target_approval&.status&.approved? ? 'tw-bg-red-500' : 'tw-bg-gray-400'  %>">
          未承認
        </div>
      </div>
    </div>
    <div class="compare-group">
      <div class="compare-title">
        仲介手数料
      </div>
      <div class="compare-result">
        <div class="compare-status <%= @input_compare_article_item.intermediary_commissions.ok? ? 'tw-text-lime-600' : 'tw-text-gray-400' %>">
          <i class="bi bi-check-circle-fill"></i>
        </div>
        <div class="compare-status <%= @input_compare_article_item.intermediary_commissions.ng? ? 'tw-text-red-500' : 'tw-text-gray-400' %>">
          <i class="bi bi-exclamation-circle-fill"></i>
        </div>
        <div class="compare-value">
          <%= @article.brokerage_commissions&.to_fs(:delimited)&.concat('円') %>
        </div>
      </div>
    </div>
  <% end %>
<% end %>
```

### チェックセクション
```erb:86-101:app/views/articles/inputs/compensation_payment_agreements/edit.html.erb
<%= render 'articles/inputs/check',
           input_article_item: @input_article_item,
           input_check_article_item: @input_check_article_item,
           url: inputs_compensation_payment_agreement_checks_path %>
```

## 主要なアクション

### 報酬支払約定書入力更新（PATCH `/articles/:id/inputs/compensation_payment_agreement`）
- **コントローラー**: `Articles::Inputs::CompensationPaymentAgreementsController#update`
- **処理**: 報酬支払約定書の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 報酬情報
- **仲介手数料**: 仲介手数料（円）

## 稟議比較機能

### 仕入れ契約稟議
- **承認済み**: 稟議が承認済みの場合に表示
- **未承認**: 稟議が未承認の場合に表示

### 仲介手数料比較
- **OK**: 入力値と稟議値が一致する場合
- **NG**: 入力値と稟議値が一致しない場合
- **稟議値**: 稟議で設定された仲介手数料

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[SalesAgreementOnPurchaseEditPage]] - 売買契約書(ドラフト)の書類入力編集ページ
- [[CertifiedCopyEditPage]] - 謄本の書類入力編集ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/compensation_payment_agreements_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/compensation_payment_agreements/edit.html.erb`
- **報酬支払約定書入力モデル**: `app/models/input/compensation_payment_agreement.rb`
- **報酬支払約定書入力フォーム**: `app/models/input/compensation_payment_agreement/form.rb` 