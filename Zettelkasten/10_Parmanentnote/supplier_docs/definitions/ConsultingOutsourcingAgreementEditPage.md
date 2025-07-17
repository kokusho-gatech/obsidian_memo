# コンサル業務委託契約書の書類入力編集ページ

## 概要
- **URL**: `/articles/:id/inputs/consulting_outsourcing_agreement/edit`
- **コントローラー**: `Articles::Inputs::ConsultingOutsourcingAgreementsController#edit`
- **ビュー**: `app/views/articles/inputs/consulting_outsourcing_agreements/edit.html.erb`
- **機能**: コンサル業務委託契約書の書類入力情報を編集するページ（権限が必要）

## 画面構成

### 左サイドバー
- 書類入力一覧ページへのナビゲーション
- ファイルタブ（他の書類へのリンク）

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 保存ボタン

#### コンサル業務委託契約書入力フォーム
##### 手数料情報
- **コンサル手数料**: コンサル手数料（円）

#### 確認・チェックセクション
- **確認情報**: 入力内容の確認
- **チェック情報**: 入力内容のチェック

## データフロー

### コントローラー（`Articles::Inputs::ConsultingOutsourcingAgreementsController#edit`）
```ruby
# BaseControllerから継承
@article = Article.find(params[:id])                                    # 対象物件
@article_item = @article.article_items.find_by(item: item)              # コンサル業務委託契約書の書類項目
@input_article_item = Input::ConsultingOutsourcingAgreement.find_or_initialize_by(...) # コンサル業務委託契約書入力情報
@form_model = Input::ConsultingOutsourcingAgreement::Form.new(@input_article_item)     # フォームモデル
@article_item_files = @article_item.article_item_files                  # ファイル一覧
@input_check_article_item = @input_article_item.checks.new              # チェック情報
@input_confirmation_article_item = @input_article_item.confirmation     # 確認情報
@input_compare_article_item = @input_article_item.compare               # 比較情報

# 追加で稟議情報を取得
@approval = @article.target_approval                                    # 稟議情報
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 書類項目情報
- **Input::ConsultingOutsourcingAgreement**: コンサル業務委託契約書入力情報
- **Input::ConsultingOutsourcingAgreement::Form**: コンサル業務委託契約書入力フォーム
- **Input::Check**: チェック情報
- **Input::Confirmation**: 確認情報
- **Input::Compare**: 比較情報

## UIとデータの対応

### メインフォーム
```erb:1-32:app/views/articles/inputs/consulting_outsourcing_agreements/edit.html.erb
<%= render 'articles/inputs/base', article: @article, article_item: @article_item, article_item_files: @article_item_files do %>
  <%= form_with model: @form_model, url: inputs_consulting_outsourcing_agreement_path(@article), method: :patch, html: { class: 'input-form', data: { controller: 'dirty-check' } } do |form| %>
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

### コンサル手数料入力
```erb:12-20:app/views/articles/inputs/consulting_outsourcing_agreements/edit.html.erb
<div class="form-main">
  <div class="form-group">
    <%= form.label :consulting_commissions, class: 'form-label' %>
    <div class="with-unit">
      <%= form.number_field :consulting_commissions, disabled: !@is_editable_input_article_item %>
      <span class="unit">円</span>
    </div>
  </div>
</div>
```

### 確認セクション
```erb:21-26:app/views/articles/inputs/consulting_outsourcing_agreements/edit.html.erb
<%= render 'articles/inputs/confirmation',
           input_article_item: @input_article_item,
           input_confirmation_article_item: @input_confirmation_article_item,
           url: inputs_consulting_outsourcing_agreement_confirmation_path(@article) %>
```

### チェックセクション
```erb:27-32:app/views/articles/inputs/consulting_outsourcing_agreements/edit.html.erb
<%= render 'articles/inputs/check',
           input_article_item: @input_article_item,
           input_check_article_item: @input_check_article_item,
           url: inputs_consulting_outsourcing_agreement_checks_path %>
```

## 主要なアクション

### コンサル業務委託契約書入力更新（PATCH `/articles/:id/inputs/consulting_outsourcing_agreement`）
- **コントローラー**: `Articles::Inputs::ConsultingOutsourcingAgreementsController#update`
- **処理**: コンサル業務委託契約書の入力情報を保存
- **権限チェック**: `contract_manager`権限が必要
- **バリデーション**: 確認済みの場合は更新不可

## 権限管理
- **編集権限**: `contract_manager`権限
- **権限チェック**: `current_user.contract_manager?`
- **確認済みチェック**: `@input_article_item.latest_check&.checked?`

## 入力項目の詳細

### 手数料情報
- **コンサル手数料**: コンサル手数料（円）

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs/consulting_outsourcing_agreements_controller.rb`
- **ベースコントローラー**: `app/controllers/articles/inputs/base_controller.rb`
- **ビュー**: `app/views/articles/inputs/consulting_outsourcing_agreements/edit.html.erb`
- **コンサル業務委託契約書入力モデル**: `app/models/input/consulting_outsourcing_agreement.rb`
- **コンサル業務委託契約書入力フォーム**: `app/models/input/consulting_outsourcing_agreement/form.rb` 