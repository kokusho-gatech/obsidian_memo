# 販売稟議編集ページ

## 概要
- **URL**: `/articles/:id/latest_sale_approval/edit`
- **コントローラー**: `Articles::LatestSaleApprovalsController#edit`
- **ビュー**: `app/views/articles/latest_sale_approvals/edit.html.erb`
- **機能**: 物件の販売稟議の申請・承認・却下・取り下げを行うページ

## 画面構成

### 左カラム
#### ヘッダー部分
- 販売稟議ステータス表示（未申請、審査中、承認済み、却下、取り下げ）
- 物件名（発表詳細ページへのリンク）

#### 販売価格入力フォーム
- 販売価格入力（万円・円の2段階入力）
- 販売稟議申請ボタン（未申請時のみ表示）
- 稟議取り下げボタン（審査中時のみ表示）

#### 稟議承認状況履歴
- 複数回の販売稟議履歴を時系列で表示
- 各ステップの承認状況を表示

### 右カラム
#### 仕入稟議情報
- 販売価格、賃料、管理費、仕入価格等の詳細情報
- 利回り、粗利等の収益性指標
- 物件概要（住所、最寄駅、築年月等）

#### 銀行評価比較
- JACCS、ORIX、SBJ、楽天、東日本銀行の評価比較
- 各銀行の評価履歴を表示

#### キャッシュフロー比較
- 集金代行とNEOインカムの比較
- 現行賃料と想定賃料でのシミュレーション

## データフロー

### コントローラー（`Articles::LatestSaleApprovalsController#edit`）
```ruby
# インスタンス変数
@article = Article.find(params[:id])                                    # 対象物件
@latest_sale_approval = @article.latest_sale_approval                  # 最新の販売稟議
@latest_approved_approval_detail = @article.latest_approved_approval   # 最新承認済み稟議詳細
@create_form = SaleApproval::CreateForm.new(...)                       # 販売稟議作成フォーム
@sale_approval_status_histories = SaleApproval::StatusHistory          # 販売稟議履歴
@valuation_histories = { jaccs: ..., orix: ..., ... }                  # 銀行評価履歴
```

### モデル
- **Article**: 物件の基本情報
- **SaleApproval**: 販売稟議の基本情報（ステータス、申請者等）
- **SaleApproval::Detail**: 販売稟議時の詳細情報
- **SaleApproval::StatusHistory**: 販売稟議のステータス変更履歴
- **SaleApproval::CreateForm**: 販売稟議作成フォーム
- **ValuationHistory**: 銀行評価履歴

## UIとデータの対応

### 販売稟議ステータス表示
```erb:3-9:app/views/articles/latest_sale_approvals/edit.html.erb
<% if @latest_sale_approval.present? %>
  <span class="sale-approval-status-label <%= sale_approval_status_label(@latest_sale_approval.status) %>">
    <%= @latest_sale_approval.status.text %>
  </span>
<% end %>
```

### 販売価格入力フォーム
```erb:11-35:app/views/articles/latest_sale_approvals/edit.html.erb
<%= form_with(model: @create_form, scope: :latest_sale_approval, url: latest_sale_approval_path, method: :post) do |form| %>
  <%= form.label :sale_price, '販売価格' %>
  <div class="form-group-row">
    <div class="form-group">
      <%= form.number_field :sale_price_man_yen %>
      <span class="unit">万</span>
    </div>
    <div class="form-group">
      <%= form.number_field :sale_price_yen %>
      <span class="unit">円</span>
    </div>
  </div>
<% end %>
```

### 販売稟議申請モーダル
```erb:37-47:app/views/articles/latest_sale_approvals/edit.html.erb
<%= button_tag '販売稟議を申請する', type: 'button', class: 'Component__button-sub-reverse Component__modal-opener', 'data-target-modal': '#sale-approval-apply-form-modal' %>
<%= render 'components/modal', id: 'sale-approval-apply-form-modal' do %>
  <div class='sale-apprroval-form-modal'>
    <h2>販売稟議を申請する</h2>
    <%= form.text_area :comment, placeholder: 'コメント(任意)' %>
    <div class="button">
      <%= form.submit '販売稟議を申請する', class: 'Component__button-sub-reverse' %>
    </div>
  </div>
<% end %>
```

### 稟議履歴表示
```erb:58-78:app/views/articles/latest_sale_approvals/edit.html.erb
<% [nil, *@sale_approval_status_histories].each_cons(2) do |previous_sale_approval_status_history, sale_approval_status_history| %>
  <%= render SaleApproval::StatusHistory::BeforeSendComponent.new(...) %>
  <%= render SaleApproval::StatusHistory::FirstReviewComponent.new(...) %>
  <%= render SaleApproval::StatusHistory::ApprovedComponent.new(...) %>
  <%= render SaleApproval::StatusHistory::CanceledComponent.new(...) %>
<% end %>
```

### 詳細情報表示
```erb:82-83:app/views/articles/latest_sale_approvals/edit.html.erb
<%= render 'detail', latest_approved_approval_detail: @latest_approved_approval_detail, valuation_histories: @valuation_histories %>
```

## 主要なアクション

### 販売稟議申請（POST `/articles/:id/latest_sale_approval`）
- **コントローラー**: `Articles::LatestSaleApprovalsController#create`
- **処理**: `SaleApproval::CreateForm`を使用して販売稟議を作成
- **バリデーション**: 仕入稟議が承認済みであることを確認
- **ステータス変更**: `before_send` → `first_reviewing`

### 販売稟議ステータス更新（PATCH `/articles/:id/latest_sale_approval`）
- **コントローラー**: `Articles::LatestSaleApprovalsController#update`
- **処理**: `SaleApproval::Status::Handler`を使用してステータスを変更
- **アクション**: `next`（次へ進む）、`remand`（差し戻し）、`cancel`（取り下げ）

## 関連ノート
- [[LatestApprovalEditPage]] - 仕入稟議編集ページ
- [[LatestSaleApprovalsPage]] - 販売稟議一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[PriorValuationEditPage]] - 仕入評価編集ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/latest_sale_approvals_controller.rb`
- **ビュー**: `app/views/articles/latest_sale_approvals/edit.html.erb`
- **詳細ビュー**: `app/views/articles/latest_sale_approvals/_detail.html.erb`
- **取り下げフォーム**: `app/views/articles/latest_sale_approvals/_cancel_form.html.erb`
- **販売稟議作成フォーム**: `app/models/sale_approval/create_form.rb`
- **販売稟議ステータスハンドラー**: `app/models/sale_approval/status/handler.rb` 