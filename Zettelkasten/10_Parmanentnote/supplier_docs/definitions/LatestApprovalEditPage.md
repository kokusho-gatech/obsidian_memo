# 仕入稟議編集ページ

## 概要
- **URL**: `/articles/:id/latest_approval/edit`
- **コントローラー**: `Articles::LatestApprovalsController#edit`
- **ビュー**: `app/views/articles/latest_approvals/edit.html.erb`
- **機能**: 物件の仕入稟議の申請・承認・却下・取り下げを行うページ

## 画面構成

### 左カラム
- 物件の基本情報表示
- マイソク（営業図面）の表示
- ネット利回りシミュレーション

### 右カラム
#### ヘッダー部分
- 稟議ステータス表示（未申請、審査中、承認済み、却下、取り下げ）
- 物件名（発表詳細ページへのリンク）
- 稟議申請ボタン（未申請時のみ表示）
- 再稟議ボタン（承認済み時のみ表示）
- 稟議取り下げボタン（審査中時のみ表示）

#### コンテンツ部分
- 仕入条件詳細（価格、利回り、粗利等）
- 収入・支出詳細（賃料、管理費等）
- 物件概要（住所、最寄駅、築年月等）
- 物件補足情報（所在階、間取り等）
- 稟議承認状況履歴（複数回の稟議履歴を表示）

## データフロー

### コントローラー（`Articles::LatestApprovalsController#edit`）
```ruby
# インスタンス変数
@article = Article.find(params[:id])                    # 対象物件
@latest_approval = @article.target_approval            # 最新の稟議
@approval_detail = build_approval_detail               # 稟議詳細情報
@approval_status_histories = Approval::StatusHistory   # 稟議履歴
@approved_approvals = @article.approvals               # 承認済み稟議一覧
@dealt_articles = @article.dealt_articles(count: 3)    # 関連物件
```

### モデル
- **Article**: 物件の基本情報
- **Approval**: 稟議の基本情報（ステータス、申請者等）
- **Approval::Detail**: 稟議時の物件詳細情報
- **Approval::StatusHistory**: 稟議のステータス変更履歴
- **Article::ApprovalDetailBuilder**: 稟議詳細情報の構築

## UIとデータの対応

### 稟議ステータス表示
```erb:23-32:app/views/articles/latest_approvals/edit.html.erb
<% if @latest_approval.present? %>
  <span class="<%= approval_status_label(@latest_approval.status) %>">
    <%= @latest_approval.status_text %>
  </span>
<% else %>
  <span class="<%= approval_status_label(Approval.status.before_send) %>">
    <%= Approval.status.before_send.text %>
  </span>
<% end %>
```

### 稟議申請フォーム
```erb:80-82:app/views/articles/latest_approvals/edit.html.erb
<%= render 'components/modal', id: 'approval-apply-form-modal' do %>
  <%= render Approval::ApplyFormComponent.new(article: @article, latest_approval: @latest_approval) %>
<% end %>
```

### 稟議詳細情報表示
```erb:47:app/views/articles/latest_approvals/edit.html.erb
<%= render 'articles/approvals/detail', approval_detail: @approval_detail, article: @article, dealt_articles: @dealt_articles %>
```

### 稟議履歴表示
```erb:48-62:app/views/articles/latest_approvals/edit.html.erb
<% [nil, *@approval_status_histories].each_cons(2) do |previous_approval_status_history, approval_status_history| %>
  <%= render Approval::StatusHistory::BeforeSendComponent.new(...) %>
  <%= render Approval::StatusHistory::FirstReviewComponent.new(...) %>
  <%= render Approval::StatusHistory::SecondReviewComponent.new(...) %>
  <%= render Approval::StatusHistory::AccountingReviewComponent.new(...) %>
  <%= render Approval::StatusHistory::LegalReviewComponent.new(...) %>
  <%= render Approval::StatusHistory::ApprovedComponent.new(...) %>
  <%= render Approval::StatusHistory::CanceledComponent.new(...) %>
<% end %>
```

## 主要なアクション

### 稟議申請（POST `/articles/:id/latest_approval`）
- **コントローラー**: `Articles::LatestApprovalsController#create`
- **処理**: `Approval::CreateForm`を使用して稟議を作成
- **ステータス変更**: `before_send` → `at_leader`

### 稟議ステータス更新（PATCH `/articles/:id/latest_approval`）
- **コントローラー**: `Articles::LatestApprovalsController#update`
- **処理**: `Approval::Status::Handler`を使用してステータスを変更
- **アクション**: `next`（次へ進む）、`remand`（差し戻し）、`cancel`（取り下げ）

## 関連ノート
- [[AssessmentPage]] - 査定一覧ページ
- [[ManagementPage]] - 交渉一覧ページ
- [[LatestApprovalsPage]] - 仕入稟議一覧ページ
- [[LatestSaleApprovalsPage]] - 販売稟議一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/latest_approvals_controller.rb`
- **ビュー**: `app/views/articles/latest_approvals/edit.html.erb`
- **稟議詳細ビュー**: `app/views/articles/approvals/_detail.html.erb`
- **稟議申請フォーム**: `app/components/approval/apply_form_component.html.erb`
- **稟議取り下げフォーム**: `app/views/articles/latest_approvals/_cancel_form.html.erb`
- **稟議作成フォーム**: `app/models/approval/create_form.rb`
- **稟議ステータスハンドラー**: `app/models/approval/status/handler.rb`
- **稟議詳細ビルダー**: `app/models/article/approval_detail_builder.rb` 