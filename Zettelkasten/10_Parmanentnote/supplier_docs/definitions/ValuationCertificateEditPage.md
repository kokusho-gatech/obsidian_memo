# 評価証明書の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/valuation_certificate/edit`
- **コントローラー**: `Articles::Inputs::ValuationCertificatesController#edit`
- **ビュー**: `app/views/articles/inputs/valuation_certificates/edit.html.erb`
- **機能**: 評価証明書の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 謄本入力結果のポップオーバー表示
- 保存ボタン

#### 評価証明書入力フォーム
##### 土地情報
- **土地総数**: 土地の総数（筆数）

#### 確認・チェックセクション
- **確認情報**: 入力内容の確認
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::ValuationCertificatesController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # 評価証明書の書類項目
@input_article_item = Input::ValuationCertificate.find_or_initialize_by(...) # 評価証明書入力情報
@form_model = Input::ValuationCertificate::Form.new(@input_article_item)     # フォームモデル
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
- **Input::ValuationCertificate**: 評価証明書入力情報
- **Input::ValuationCertificate::Form**: 評価証明書入力フォーム
- **Input::CertifiedCopy**: 謄本入力情報（参照用）
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-49:app/views/articles/inputs/valuation_certificates/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_valuation_certificate_path, method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
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
```erb:10-25:app/views/articles/inputs/valuation_certificates/edit.html.erb
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
            <dt>筆数</dt>
            <dd><%= @input_certified_copy.total_lands %></dd>
          </dl>
        <% end %>
      </div>
    </div>
  </div>
  <%= form.submit '入力項目を保存する', class: 'submit-button' %>
</div>
```

### 土地総数入力
```erb:26-32:app/views/articles/inputs/valuation_certificates/edit.html.erb
<div class="form-main">
  <div class="form-group">
    <%= form.label :total_lands, class: 'form-label' %>
    <%= form.number_field :total_lands, disabled: !@is_editable_input_article_item %>
  </div>
</div>
```

### 確認・チェックセクション
```erb:33-49:app/views/articles/inputs/valuation_certificates/edit.html.erb
<%= render 'articles/inputs/confirmation',
           input_article_item: @input_article_item,
           input_confirmation_article_item: @input_confirmation_article_item,
           url: inputs_valuation_certificate_confirmation_path(@article) %>
<%= render 'articles/inputs/check',
           input_article_item: @input_article_item,
           input_check_article_item: @input_check_article_item,
           url: inputs_valuation_certificate_checks_path %>
```

## 主要なアクション

### 評価証明書入力更新（PATCH `/articles/:id/inputs/valuation_certificate`）
- **コントローラー**: `Articles::Inputs::ValuationCertificatesController#update`
- **処理**: 評価証明書の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 土地情報
- **土地総数**: 土地の総数（筆数）

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[CertifiedCopyEditPage]] - 謄本の書類入力編集ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/valuation_certificates_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/valuation_certificates/edit.html.erb`
- **評価証明書入力モデル**: `app/models/input/valuation_certificate.rb`
- **評価証明書入力フォーム**: `app/models/input/valuation_certificate/form.rb` 