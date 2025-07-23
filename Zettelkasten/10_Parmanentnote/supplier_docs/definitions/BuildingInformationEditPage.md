---
tags:
  - definition
  - page
  - supplier
  - parmanentnote
---

# 建物情報編集ページ

## 概要
- **URL**: `/articles/:id/building_information/edit`
- **コントローラー**: `Articles::BuildingInformationsController#edit`
- **ビュー**: `app/views/articles/building_informations/edit.html.erb`
- **機能**: TechBuildingへ反映する建物情報を編集するページ（権限が必要）

## 画面構成

### 左カラム
- 物件の基本情報表示
- マイソク（営業図面）の表示

### 右カラム
#### ヘッダー部分
- 物件名（発表詳細ページへのリンク）
- 説明文（TechBuilding反映の説明）

#### アクションバー
- **保存**: 建物情報の保存
- **TechBuilding反映**: TechBuildingへの情報反映
- **TechBuildingクリア**: TechBuilding情報のクリア

#### 建物情報フォーム
##### 基本情報
- **建物名**: 建物の名称
- **住所**: 都道府県、市区町村、番地
- **最寄駅情報**: 駅名、徒歩分数、路線名（3駅まで）
- **建物構造**: 建物の構造（RC、SRC等）
- **階数**: 地上階数
- **築年月**: 築年月（YYYYMM形式）
- **総戸数**: 建物の総戸数
- **管理会社**: 建物管理会社名

##### 追加情報
- **総会月**: 管理組合総会月
- **エレベータ**: エレベータの有無
- **外壁要確認**: 外壁確認の必要性
- **半地下**: 1階半地下の有無
- **近隣注意**: 近隣への注意事項
- **近隣注意事項**: 近隣に関する詳細な注意事項

## データフロー

### コントローラー（`Articles::BuildingInformationsController#edit`）
```ruby
# インスタンス変数
@article = Article.find(params[:id])                                    # 対象物件
# 権限チェック
unless current_user.has_any_auth?(:tech_building_data_confirmer, :tech_building_data_authorizer)
  return redirect_to article_path(@article)
end
set_display_elements                                                    # 表示要素の設定
# TechBuilding情報の初期化
@article.build_article_tech_building_information
@article.overwrite_tech_building_information
```

### モデル
- **Article**: 物件の基本情報
- **ArticleTechBuildingInformation**: TechBuilding反映用建物情報
- **TechBuilding::Building**: TechBuildingの建物情報
- **RailwayStation**: 鉄道駅情報

## UIとデータの対応

### メインフォーム
```erb:1-16:app/views/articles/building_informations/edit.html.erb
<%= form_for(@article, url: edit_building_information_path(@article), html: { 'data-article-id' => @article.id, id: 'article-form' }) do |f| %>
  <%= f.fields_for :article_tech_building_information, @article.article_tech_building_information do |ff| %>
    <%= ff.hidden_field :id %>
    <%= render 'edit_base', f: f, ff: ff %>
  <% end %>
<% end %>
```

### 建物名入力
```erb:8-15:app/views/articles/building_informations/partial/_for_information.html.erb
<dd>
  <div class="title<%= ' changed' if tech_building&.name != ff.object.building_name %>">
    <%= ff.label :building_name %>
  </div>
  <div class="content">
    <div class="edit">
      <div class="row">
        <%= ff.text_field :building_name, placeholder: "TB:#{tech_building&.name}", readonly: ff.object.authorized %>
      </div>
    </div>
  </div>
</dd>
```

### 住所入力
```erb:16-35:app/views/articles/building_informations/partial/_for_information.html.erb
<dd>
  <div class="title<%= ' changed' if tech_building&.address != ff.object.address %>">
    <%= ff.label :address %>
  </div>
  <div class="content">
    <div class="edit">
      <div class="row">
        <%= ff.text_field :prefecture, placeholder: "TB:#{tech_building&.prefecture}", readonly: ff.object.authorized %>
      </div>
      <div class="row">
        <%= ff.text_field :state, placeholder: "TB:#{tech_building&.city}", readonly: ff.object.authorized %>
      </div>
      <div class="row">
        <%= ff.text_field :city, placeholder: "TB:#{tech_building&.street}", readonly: ff.object.authorized %>
      </div>
      <div class="row">
        <%= ff.text_field :street, readonly: ff.object.authorized %>
      </div>
    </div>
  </div>
</dd>
```

### 最寄駅情報
```erb:45-65:app/views/articles/building_informations/partial/_for_information.html.erb
<dd class="separate_line">
  <div class="title<%= ' changed' if tech_building&.advertisement_railway_station_id_1 != ff.object.advertisement_railway_station_id_1 %>">
    <%= ff.label :station_name_1 %>
  </div>
  <div class="content">
    <div class="edit">
      <div class="row">
        <%= text_field_tag 'article[article_tech_building_information_attributes][advertisement_railway_station_name_1]', advertisement_railway_station_1&.name, class: 'right', placeholder: "TB:#{tech_building&.advertisement_railway_station_1&.name}", readonly: ff.object.authorized %>
        <span class="unit right">駅</span>
      </div>
    </div>
  </div>
</dd>
```

## 主要なアクション

### 建物情報更新（PATCH `/articles/:id/building_information`）
- **コントローラー**: `Articles::BuildingInformationsController#update`
- **処理**: 建物情報の保存
- **権限チェック**: `tech_building_data_confirmer`または`tech_building_data_authorizer`権限が必要

### TechBuilding反映（PUT `/articles/:id/building_information/update_tech_building`）
- **コントローラー**: `Articles::BuildingInformationsController#update_tech_building`
- **処理**: TechBuildingへの情報反映
- **バリデーション**: 確認済み、建物名、住所、築年月の必須チェック

### TechBuildingクリア（PUT `/articles/:id/building_information/clear_tech_building`）
- **コントローラー**: `Articles::BuildingInformationsController#clear_tech_building`
- **処理**: TechBuilding情報のクリアと再初期化

## 権限管理
- **編集権限**: `tech_building_data_confirmer`または`tech_building_data_authorizer`
- **権限チェック**: `current_user.has_any_auth?(:tech_building_data_confirmer, :tech_building_data_authorizer)`

## TechBuilding連携の詳細

### 変更検知
- タイトルが青色で表示される項目は、現在のTechBuildingから変更があるもの
- プレースホルダーに`TB:`で始まる値は、TechBuildingの現在値

### バリデーション
- **確認済み**: `authorized`フラグの確認
- **建物名**: 必須項目
- **住所**: 必須項目
- **築年月**: 6桁の数字（YYYYMM形式）

### 反映処理
- TechBuilding::Building.updateを使用してTechBuildingに反映
- 反映成功時に`update_tech_building_updater`で更新者を記録

## 関連ノート
- [[ArticleDetailPage]] - 発表詳細ページ
- [[ValuationHistoriesEditPage]] - 銀行評価編集ページ
- [[ArticleInputsPage]] - 書類入力一覧ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/building_informations_controller.rb`
- **メインビュー**: `app/views/articles/building_informations/edit.html.erb`
- **編集ベース**: `app/views/articles/building_informations/_edit_base.html.erb`
- **情報フォーム**: `app/views/articles/building_informations/partial/_for_information.html.erb`
- **アクションバー**: `app/views/articles/building_informations/_action_bar.html.erb`
- **建物情報モデル**: `app/models/article_tech_building_information.rb`
- **TechBuilding連携**: `app/models/concerns/articles/article_tech_building_information.rb` 