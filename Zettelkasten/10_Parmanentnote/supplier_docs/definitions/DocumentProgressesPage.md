---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# DocumentProgressesPage

## 概要
- **URL**: `/articles/document_progresses`
- **コントローラー**: `Articles::DocumentProgressesController#index`
- **ビュー**: `app/views/articles/document_progresses/index.html.erb`
- **機能**: 契約書作成の進捗状況を一覧表示し、管理するページ

## 画面構成

### 検索フォーム
#### ラベル情報セクション
- **短縮名**: ラベルの複数選択（TomSelect使用）

#### 物件情報セクション
- **販売月**: 対象の販売月（YYYYMM形式）

### 進捗状況カード一覧
#### 未作成セクション（大カード）
- **販売月別・ステータス別の分類**:
  - 販売月：翌月（未着手、マイソク作成済、販売中）
  - 販売月：当月（未着手、マイソク作成済、販売中）

#### その他ステータスセクション（小カード）
- **各ステータス別の分類**:
  - 作成中、作成済み、納品済み等
  - 販売月別（翌月、当月）の件数表示

### 物件カード詳細
各物件に対して以下の情報を表示：

#### ヘッダー部分
- **CRMステータス**: TechConsulの販売ステータス
- **確保状況**: 物件の確保状況
- **担当者名**: 契約書作成担当者
- **アプリ確認**: 契約書ファイルの確認状況
- **ナビゲーションリンク**: 編集、契約書作成、AGNTリンク

#### メイン情報
- **物件名**: 発表詳細ページへのリンク
- **ラベル**: 色付きラベル表示
- **販売状況**: 販売可能状況（仮公開時のみ）
- **アイコン表示**:
  - 添付セット作成状況（ペーパークリップ）
  - 書類回収状況（ファイルアイコン）
  - 備考情報（鉛筆アイコン）

#### 詳細情報
- **契約可能日**: 契約開始可能日
- **謄本日付**: 謄本取得日
- **物件ランク**: TechConsulの物件ランク
- **契約作成期間**:
  - AGNT期間
  - 確保期間
  - SUPP期間

## データフロー

### コントローラー（`Articles::DocumentProgressesController#index`）
```ruby
# インスタンス変数
@search_conditions = search_params.presence || default_search_params    # 検索条件
@labels = Label.for_document_progress.active.display_order.map(&:short_name)  # ラベル一覧
card_list_builder = DocumentProgresses::CardListBuilder.new(            # カードリストビルダー
  @search_conditions[:sales_month],
  @search_conditions[:short_name_labels]
)
@document_progress_info = card_list_builder.call                        # 進捗情報
```

### モデル
- **DocumentProgress**: 契約書作成進捗情報
- **Label**: ラベル情報
- **Article**: 物件の基本情報
- **DocumentProgresses::CardListBuilder**: カードリスト構築
- **DocumentProgresses::ApiClient**: TechConsul連携

## UIとデータの対応

### 検索フォーム
```erb:8-35:app/views/articles/document_progresses/index.html.erb
<%= form_with url: articles_document_progresses_path, method: :get do |form| %>
  <div class="content">
    <h2>ラベル情報</h2>
    <div class="search-form-item">
      <p>短縮名</p>
      <%= form.select :short_name_labels, @labels, { include_hidden: false, selected: @search_conditions[:short_name_labels] }, { multiple: true, class: 'tw-w-96', data: { controller: 'multiple-tom-select' } } %>
    </div>
  </div>
  <div class="content">
    <h2>物件情報</h2>
    <div class="search-form-item">
      <p>販売月</p>
      <%= form.number_field :sales_month, value: @search_conditions[:sales_month] %>
    </div>
  </div>
<% end %>
```

### 未作成セクション
```erb:37-95:app/views/articles/document_progresses/index.html.erb
<li class="item item-large">
  <h2 class="status">
    <span><%= @document_progress_info[:not_created][:status] %></span>
    <%= @document_progress_info[:not_created][:size] %>件
    (販売月：<%= @document_progress_info[:not_created][:next_month] %>　<%= @document_progress_info[:not_created][:document_progresses_next_month].size %>件、
    販売月：<%= @document_progress_info[:not_created][:this_month] %>　<%= @document_progress_info[:not_created][:document_progresses_this_month].size %>件)
  </h2>
  <div class="list leftmost">
    <h3 class="list-title">
      <span>販売月：<%= @document_progress_info[:not_created][:next_month] %></span>
      未着手：<%= @document_progress_info[:not_created][:next_month_before_sale].size %>件
    </h3>
    <%= render 'list_item', document_progresses: @document_progress_info[:not_created][:next_month_before_sale], document_progress_status: @document_progress_info[:not_created][:status] %>
  </div>
  <!-- 他のセクション -->
</li>
```

### 物件カード
```erb:1-171:app/views/articles/document_progresses/_list_item.html.erb
<div class="box-card">
  <div class="el-card <%= 'user' if document_progress[:user_name] %>">
    <div class="el-card__body">
      <div class="header">
        <p class="<%= document_progress_tech_consul_status_class(document_progress[:tech_consul_status]) %>">
          <%= document_progress[:tech_consul_status] %>
        </p>
        <% if document_progress_article_reserved_and_on_sale?(document_progress) %>
          <p class="reserved">確保</p>
        <% end %>
        <% if document_progress[:user_name] %>
          <p class="user-name"><%= document_progress[:user_name] %></p>
        <% end %>
        <ul class="link-navigation">
          <li data-js-tooltip='{"str": "編集ページ"}'>
            <a href="<%= "/articles/#{document_progress[:article_id]}/document_progresses/edit" %>" class="link" target="_blank">
              <i class="fa fa-edit"></i>
            </a>
          </li>
          <li data-js-tooltip='{"str": "契約書作成ページ"}'>
            <a href="<%= "/articles/#{document_progress[:article_id]}/sales_contract_fields/#{document_progress[:sales_contract_field_id]}/sales_agreement/edit" %>" class="link" target="_blank">
              <i class="fa fa-file-text"></i>
            </a>
          </li>
        </ul>
      </div>
      <!-- メイン情報 -->
    </div>
  </div>
</div>
```

## 進捗ステータスの詳細

### ステータス分類
- **未作成**: 契約書作成が未着手
- **作成中**: 契約書作成中
- **作成済み**: 契約書作成完了
- **納品済み**: 契約書納品完了

### 販売月別分類
- **翌月**: 次月の販売月
- **当月**: 現在の販売月

### TechConsulステータス別分類
- **未着手**: 販売開始前
- **マイソク作成済**: 営業図面作成完了
- **販売中**: 販売進行中

## 関連ノート
- [[ArticleInputsPage]] - 書類入力一覧ページ
- [[ArticleDetailPage]] - 発表詳細ページ
- [[SalesContractFieldsPage]] - 契約書作成ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/document_progresses_controller.rb`
- **メインビュー**: `app/views/articles/document_progresses/index.html.erb`
- **リストアイテム**: `app/views/articles/document_progresses/_list_item.html.erb`
- **カードリストビルダー**: `app/models/document_progresses/card_list_builder.rb`
- **APIクライアント**: `app/models/document_progresses/api_client.rb`
- **進捗モデル**: `app/models/document_progress.rb` 