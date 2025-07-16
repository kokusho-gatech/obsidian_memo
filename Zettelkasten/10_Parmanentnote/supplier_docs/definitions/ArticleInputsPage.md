# 書類入力一覧ページ

## 概要
- **URL**: `/articles/:id/inputs`
- **コントローラー**: `Articles::InputsController#index`
- **ビュー**: `app/views/articles/inputs/index.html.erb`
- **機能**: 物件の書類入力状況を一覧表示し、各書類の入力編集ページへのナビゲーションを提供

## 画面構成

### 左サイドバー（`_sidebar.html.erb`）
#### ナビゲーションメニュー
- **ドラフトTOP**: 書類入力一覧ページ
- **謄本**: 謄本の書類入力編集
- **売買契約書(ドラフト)**: 売買契約書の書類入力編集
- **重要事項調査報告書**: 重要事項調査報告書の書類入力編集
- **報酬支払約定書(ドラフト)**: 報酬支払約定書の書類入力編集
- **パンフレット**: パンフレットの書類入力編集
- **賃貸借契約書(出先)**: 賃貸借契約書の書類入力編集
- **評価証明書**: 評価証明書の書類入力編集
- **コンサルティング業務委託契約書(ドラフト)**: コンサル業務委託契約書の書類入力編集
- **売買契約書(AB間)**: 売買契約書(AB間)の書類入力編集

#### 追加機能
- **ヒアリング**: 建物確認ページへのリンク

### メインコンテンツ
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 書類回収完了予定日の表示・編集

#### 書類入力状況テーブル
- **書類名**: 入力対象の書類名
- **ステータス**: チェック状況（未チェック、チェック済み、不備あり）
- **タスクメモ**: 確認内容のメモ
- **稟議比較**: 稟議との比較状況（完了、未完了）

## データフロー

### コントローラー（`Articles::InputsController#index`）
```ruby
# インスタンス変数
@article = Article.find(params[:id])                                    # 対象物件
@article_item_inputs = @article.article_items                          # 書類入力情報
                .preload(:item)
                .where(item: Item.for_input)
                .sort_by { |article_item| Item::FOR_INPUT.index(article_item.item.name) }
                .map { |article_item| article_item.input || article_item.build_input }
@purchase_contract = @article.purchase_contract                        # 仕入契約情報
@sales_info = @article.sales_info || @article.build_sales_info        # 販売情報
```

### モデル
- **Article**: 物件の基本情報
- **ArticleItem**: 物件と書類の関連情報
- **Item**: 書類の基本情報
- **Input**: 書類入力の詳細情報
- **Check**: 書類チェック情報
- **Confirmation**: 確認情報
- **Compare**: 稟議比較情報

## UIとデータの対応

### サイドバーナビゲーション
```erb:1-89:app/views/articles/inputs/_sidebar.html.erb
<%= tag.ul class: %w[tw-w-40 ...] do %>
  <li class="<%= 'active' if current_path == inputs_path(article) %>">
    <%= link_to 'ドラフトTOP', inputs_path(article) %>
  </li>
  <li class="<%= 'active' if [edit_inputs_certified_copy_path(article), inputs_certified_copy_path(article)].include?(current_path) %>
             <%= 'disable' unless article.uploaded_files.include?(Item::COPY_OF_REGISTRATION) %>">
    <%= link_to Item::COPY_OF_REGISTRATION, edit_inputs_certified_copy_path(article) %>
  </li>
  <!-- 他の書類リンク -->
<% end %>
```

### 書類入力状況テーブル
```erb:30-100:app/views/articles/inputs/index.html.erb
<%= tag.table class: %w[tw-w-full tw-bg-white tw-border tw-border-gray-200] do %>
  <thead>
    <tr>
      <th class="tw-w-[4%]"></th>
      <th class="tw-w-[16%]">書類名</th>
      <th class="tw-w-[8%] tw-text-center">ステータス</th>
      <th class="tw-w-[40%]">タスクメモ</th>
      <th class="tw-w-[8%] tw-text-center">稟議比較</th>
      <th class="tw-w-[4%]"></th>
    </tr>
  </thead>
  <tbody>
    <% @article_item_inputs.each do |article_item_input| %>
      <tr>
        <td></td>
        <td><%= article_item_input.article_item.item.name %></td>
        <td class="tw-text-center">
          <% if article_item_input.latest_check.nil? %>
            <span>-</span>
          <% elsif article_item_input.latest_check.checked? %>
            <span class="status tw-bg-gray-400"><%= article_item_input.latest_check.status_text %></span>
          <% else %>
            <span class="status tw-bg-red-500"><%= article_item_input.latest_check.status_text %></span>
          <% end %>
        </td>
        <td>
          <div class="confirmation-content">
            <%= simple_format(article_item_input.confirmation&.content) %>
          </div>
        </td>
        <td class="tw-text-center">
          <% input_compare = article_item_input.compare || article_item_input.build_compare %>
          <% if input_compare.nil? %>
            <span>-</span>
          <% elsif input_compare.all_ok? %>
            <span class="status tw-bg-lime-600">完了</span>
          <% else %>
            <span class="status tw-bg-red-500">未完了</span>
          <% end %>
        </td>
        <td></td>
      </tr>
    <% end %>
  </tbody>
<% end %>
```

## 書類入力対象の詳細

### 入力対象書類（`Item::FOR_INPUT`）
1. **謄本** (`COPY_OF_REGISTRATION`)
2. **売買契約書(ドラフト)** (`SALES_AGREEMENT_ON_PURCHASE`)
3. **重要事項調査報告書** (`REPORT_OF_IMPORTANT_INFO_SURVEY`)
4. **報酬支払約定書(ドラフト)** (`COMPENSATION_PAYMENT_AGREEMENT_ON_PURCHASE`)
5. **パンフレット** (`PAMPHLET`)
6. **賃貸借契約書(出先)** (`TENANT_LEASE_AGREEMENT`)
7. **評価証明書** (`VALUATION_CERTIFICATE`)
8. **コンサルティング業務委託契約書(ドラフト)** (`CONSULTING_OUTSOURCING_AGREEMENT_ON_PURCHASE`)
9. **売買契約書(AB間)** (`SALES_AGREEMENT_AB`)

### 各書類の編集ページURL
- `/articles/:id/inputs/certified_copy/edit` - 謄本
- `/articles/:id/inputs/sales_agreement_on_purchase/edit` - 売買契約書(ドラフト)
- `/articles/:id/inputs/report_of_important_info_survey/edit` - 重要事項調査報告書
- `/articles/:id/inputs/compensation_payment_agreement/edit` - 報酬支払約定書(ドラフト)
- `/articles/:id/inputs/pamphlet/edit` - パンフレット
- `/articles/:id/inputs/tenant_lease_agreement/edit` - 賃貸借契約書(出先)
- `/articles/:id/inputs/valuation_certificate/edit` - 評価証明書
- `/articles/:id/inputs/consulting_outsourcing_agreement/edit` - コンサル業務委託契約書(ドラフト)
- `/articles/:id/inputs/sales_agreement_ab/edit` - 売買契約書(AB間)

## 関連ノート
- [[ArticleDetailPage]] - 発表詳細ページ
- [[DocumentProgressesPage]] - 契約書作成進捗一覧ページ
- [[BuildingConfirmationsPage]] - 建物確認ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/inputs_controller.rb`
- **メインビュー**: `app/views/articles/inputs/index.html.erb`
- **サイドバー**: `app/views/articles/inputs/_sidebar.html.erb`
- **書類モデル**: `app/models/item.rb`
- **入力モデル**: `app/models/input.rb`
- **チェックモデル**: `app/models/check.rb` 