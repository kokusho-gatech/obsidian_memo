# 仕入契約一覧ページ

## 概要
- **URL**: `/purchase_contracts`
- **コントローラー**: `PurchaseContractsController#index`
- **ビュー**: `app/views/purchase_contracts/index.html.erb`
- **機能**: 仕入契約の管理・検索・CSV出力を行うページ

## 画面構成

### 検索フォーム（`_search_form.html.erb`）
#### 物件情報セクション
- **決済月**: 物件の決済予定月
- **販売月**: 物件の販売予定月
- **物件名**: 建物名での検索
- **BLDG**: BLDG連携での検索
- **号室**: 部屋番号での検索
- **仕入れ担当**: 仕入れ担当者の選択
- **コントラクト担当**: コントラクト担当者の選択
- **フェーズ**: 物件のフェーズ（査定、交渉、発表等）
- **販売先**: 販売先の選択
- **稟議ステータス**: 仕入稟議のステータス
- **仕入契約解除**: 契約解除の有無

#### 発表関係セクション
- **仲介会社名**: 仲介会社名での検索・除外
- **CRM販売ステータス**: TechConsulの販売ステータス
- **仕入契約予定期日**: 契約予定日の範囲指定
- **仕入契約予定日**: 契約予定日の範囲指定
- **書類回収完了予定日**: 書類回収予定日の範囲指定
- **売主決済日**: 売主決済日の範囲指定

#### 物件概要セクション
- **現況**: 物件の現況（空室、入居中、サブリース等）

### 検索結果（`_search_result.html.erb`）
#### データテーブル
- **販売月・決済月**: 物件の月次情報
- **物件名号室**: 物件の基本情報（発表詳細ページへのリンク）
- **担当者情報**: 仕入担当、コントラクト担当
- **フェーズ・稟議**: 物件の進行状況
- **物件公開コメント**: 発表時のコメント
- **仲介会社**: 仲介会社情報
- **契約関連日付**: 各種予定日・実績日
- **建物管理会社**: 管理会社情報
- **総会・重調**: 総会月、重要事項調査取得月
- **ヒアリング**: ヒアリング日・備考・有無
- **決済パターン**: 決済方法
- **CRM販売ステータス**: TechConsul連携状況
- **不備書類**: 未回収書類
- **現況・販売先**: 物件の最終情報

## データフロー

### コントローラー（`PurchaseContractsController#index`）
```ruby
# デフォルト検索条件
default_search_articles = {
  sales_month_eq: SalesTerm.current_target,                    # 現在の販売月
  tech_consul_status_in: Article::TECH_CONSUL_STATUS_NOT_SUSPENSION,  # 停止以外のCRMステータス
  purchase_contract_cancellation_id_not_null: false            # 契約解除以外
}

# 検索結果
@articles = @q.result(distinct: true)
              .preload(:user, :intermediary_company, :purchase_contract, ...)
              .undeleted
              .negotiation_status_very_good
              .page(params[:page])
              .per(100)
```

### モデル
- **Article**: 物件の基本情報
- **PurchaseContract**: 仕入契約情報
- **User**: 仕入担当者情報
- **IntermediaryCompany**: 仲介会社情報
- **SalesDestination**: 販売先情報
- **Approval**: 稟議情報

## UIとデータの対応

### 検索フォーム
```erb:8-156:app/views/purchase_contracts/_search_form.html.erb
<%= search_form_for(@q, url: purchase_contracts_path) do |f| %>
  <div class="content">
    <h2>物件情報</h2>
    <div class="search-form-item">
      <p>決済月</p>
      <%= f.number_field :settlement_month_eq %>
    </div>
    <!-- 他の検索項目 -->
  </div>
  <ul class="button-list">
    <li><%= f.submit '条件で絞り込む', class: 'button-submit' %></li>
    <li><%= link_to '仕入契約CSV出力', download_purchase_contracts_path(params.permit(q: {})), class: 'button-download' %></li>
  </ul>
<% end %>
```

### 検索結果テーブル
```erb:1-127:app/views/purchase_contracts/_search_result.html.erb
<table id="purchase-contracts-table" class="stripe order-column cell-border">
  <thead>
    <tr>
      <th>販売月</th>
      <th>決済月</th>
      <th>物件名号室</th>
      <!-- 他のヘッダー -->
    </tr>
  </thead>
  <tbody>
    <% @articles.each do |article| %>
      <tr>
        <td><%= article.sales_month %></td>
        <td><%= article.settlement_month %></td>
        <td><%= link_to article.article_name, article_path(article), target: '_blank' %></td>
        <!-- 他のデータ -->
      </tr>
    <% end %>
  </tbody>
</table>
```

## 主要なアクション

### 検索実行（GET `/purchase_contracts`）
- **コントローラー**: `PurchaseContractsController#index`
- **処理**: Ransackを使用した検索条件の適用
- **ページネーション**: 100件ずつ表示

### CSV出力（GET `/purchase_contracts/download`）
- **コントローラー**: `PurchaseContractsController#download`
- **処理**: `Csv::PurchaseContract`を使用してCSV生成
- **ファイル名**: `仕入契約管理.csv`

## 検索条件の詳細

### デフォルト検索条件
- **販売月**: 現在の販売月
- **CRMステータス**: 停止以外（正常、保留等）
- **契約解除**: 未解除のみ

### 検索対象物件
- **削除済み除外**: `undeleted`
- **交渉感触**: `negotiation_status_very_good`（◎のみ）

## 関連ノート
- [[ManagementPage]] - 交渉一覧ページ
- [[LatestApprovalEditPage]] - 仕入稟議編集ページ
- [[ArticleDetailPage]] - 発表詳細ページ

## 参考ファイル
- **コントローラー**: `app/controllers/purchase_contracts_controller.rb`
- **メインビュー**: `app/views/purchase_contracts/index.html.erb`
- **検索フォーム**: `app/views/purchase_contracts/_search_form.html.erb`
- **検索結果**: `app/views/purchase_contracts/_search_result.html.erb`
- **CSV生成**: `app/models/csv/purchase_contract.rb`
- **仕入契約モデル**: `app/models/purchase_contract.rb` 