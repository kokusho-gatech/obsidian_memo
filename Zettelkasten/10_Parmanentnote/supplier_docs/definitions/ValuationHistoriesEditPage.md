# 査定履歴編集ページ

## 概要
- **URL**: `/articles/:id/valuation_histories/edit`
- **コントローラー**: `Articles::ValuationHistoriesController#edit`
- **ビュー**: `app/views/articles/valuation_histories/edit.html.erb`
- **機能**: 物件の査定履歴を編集するページ（権限が必要）

## 画面構成

### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 査定履歴のタイトル

### 査定履歴フォーム
- 各銀行の査定情報を編集可能なフォーム
- 銀行ごとに査定ステータスを表示
- 権限がある場合のみ保存ボタンを表示

### 銀行別査定項目
各銀行（JACCS、ORIX、SBJ、楽天、東日本銀行等）に対して以下を表示：
- **査定ステータス**: 査定の進行状況
- **TAS価格**: 査定価格（万円単位で入力、内部で円に変換）
- **TAS金利**: 査定時の金利
- **二当事者確認**: 確認状況
- **銀行確認状況**: 銀行側の確認状況
- **ネット価格結果**: 最終的な査定価格
- **備考**: 査定に関する特記事項

## データフロー

### コントローラー（`Articles::ValuationHistoriesController#edit`）
```ruby
# インスタンス変数
@article = Article.find(params[:id])                                    # 対象物件
@is_valuation_histories_editable_user = current_user.has_auth?(:valuation_histories_editable)  # 編集権限
@valuation_histories_form = Form::ValuationHistories.new(              # 査定履歴フォーム
  @article.valuations
          .preload(:bank, :last_valuation_history)
          .bank_sort
          .map(&:last_valuation_history)
          .compact
)
```

### モデル
- **Article**: 物件の基本情報
- **Valuation**: 銀行査定の基本情報
- **ValuationHistory**: 銀行査定の履歴情報
- **Bank**: 銀行の基本情報（JACCS、ORIX、SBJ等）
- **Form::ValuationHistories**: 査定履歴の一括更新フォーム

## UIとデータの対応

### 査定履歴フォーム
```erb:8-15:app/views/articles/valuation_histories/edit.html.erb
<%= form_for(@valuation_histories_form, url: valuation_histories_path(@article), method: :patch, html: { id: 'valuation-histories-form' }) do |form| %>
  <% @valuation_histories_form.valuation_histories.each do |valuation_history| %>
    <% if valuation_history.bank.valuation_available? %>
      <div class="bank-header">
        <div class="bank-header-name"><%= valuation_history.bank.name %></div>
        <div class="bank-header-label <%= valuation_history.status %>">
          査定ステータス: <%= valuation_history.status_text %>
        </div>
      </div>
```

### 銀行別査定項目
```erb:16-30:app/views/articles/valuation_histories/edit.html.erb
<%= form.fields_for valuation_history, index: valuation_history.bank.name_sym do |valuation_history_form| %>
  <div class="bank-container">
    <% valuation_history.bank.editable_attributes.each do |attribute| %>
      <%= render "articles/valuation_histories/banks/valuation_available/#{attribute}",
                 valuation_history_form: valuation_history_form %>
    <% end %>
    <% valuation_history.bank.readable_attributes.each do |attribute| %>
      <%= render "articles/valuation_histories/banks/valuation_available/#{attribute}",
                 valuation_history: valuation_history %>
    <% end %>
  </div>
<% end %>
```

### 保存ボタン（権限チェック）
```erb:32-34:app/views/articles/valuation_histories/edit.html.erb
<% if @is_valuation_histories_editable_user %>
  <%= form.submit '保存', class: 'button-submit', id: 'valuation-histories-submit-button' %>
<% end %>
```

## 主要なアクション

### 査定履歴更新（PATCH `/articles/:id/valuation_histories`）
- **コントローラー**: `Articles::ValuationHistoriesController#update`
- **処理**: `Form::ValuationHistories`を使用して査定履歴を一括更新
- **権限チェック**: `valuation_histories_editable`権限が必要
- **データ変換**: TAS価格を万円から円に自動変換

## 権限管理
- **編集権限**: `User::AUTH_LEVELS[:valuation_histories_editable]`（レベル210）
- **権限名**: `銀行査定履歴編集権限`
- **権限チェック**: `current_user.has_auth?(:valuation_histories_editable)`

## 銀行別査定項目の詳細

### 編集可能項目（`bank.editable_attributes`）
- **status**: 査定ステータス
- **tas_value**: TAS価格（万円）
- **tas_rate**: TAS金利
- **two_party_confirmation**: 二当事者確認
- **bank_confirmation_status**: 銀行確認状況
- **remarks**: 備考

### 読み取り専用項目（`bank.readable_attributes`）
- **net_value_result**: ネット価格結果

## 関連ノート
- [[PriorValuationEditPage]] - 仕入評価編集ページ
- [[LatestSaleApprovalEditPage]] - 販売稟議編集ページ
- [[ArticleDetailPage]] - 発表詳細ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/valuation_histories_controller.rb`
- **ビュー**: `app/views/articles/valuation_histories/edit.html.erb`
- **銀行別査定項目ビュー**: `app/views/articles/valuation_histories/banks/valuation_available/`
- **査定履歴フォーム**: `app/models/form/valuation_histories.rb`
- **銀行モデル**: `app/models/bank.rb`
- **査定履歴モデル**: `app/models/valuation_history.rb` 