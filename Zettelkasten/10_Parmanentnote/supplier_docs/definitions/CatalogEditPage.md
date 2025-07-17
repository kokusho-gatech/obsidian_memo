# カタログ編集ページ

## 概要
- **URL**: `/articles/:id/catalog/edit`
- **コントローラー**: `Articles::CatalogsController#edit`
- **ビュー**: リダイレクト機能のみ
- **機能**: 物件のカタログ（マイソク・シミュレーション）編集ページへのリダイレクト

## 画面構成

このページは単純なリダイレクト機能を提供し、実際の編集画面は以下のページに転送されます：

### リダイレクト先
#### マイソク編集ページ（デフォルト）
- **URL**: `/articles/:id/for_sale_maisoku/edit`
- **機能**: 営業図面（マイソク）の編集

#### シミュレーション編集ページ
- **URL**: `/articles/:id/for_simulation/edit`
- **機能**: 利回りシミュレーションの編集

## データフロー

### コントローラー（`Articles::CatalogsController#edit`）
```ruby
# パラメータによる分岐処理
@article = Article.find(params[:id])

if params[:document_type].blank? || params[:document_type] == 'maisoku'
  redirect_to edit_for_sale_maisoku_path(@article)      # マイソク編集へ
elsif params[:document_type] == 'simulation'
  redirect_to edit_for_simulation_path(@article)        # シミュレーション編集へ
else
  routing_error                                         # エラー
end
```

### リダイレクト条件
- **デフォルト**: `params[:document_type]`が空または`'maisoku'`の場合
- **シミュレーション**: `params[:document_type]`が`'simulation'`の場合
- **エラー**: 上記以外の値の場合

## URLパターン

### マイソク編集へのアクセス
```
/articles/:id/catalog/edit?document_type=maisoku
/articles/:id/catalog/edit
```

### シミュレーション編集へのアクセス
```
/articles/:id/catalog/edit?document_type=simulation
```

## 関連ノート
- [[ForSaleMaisokuEditPage]] - マイソク編集ページ
- [[ForSimulationEditPage]] - シミュレーション編集ページ
- [[ArticleDetailPage]] - 発表詳細ページ

## 参考ファイル
- **コントローラー**: `app/controllers/articles/catalogs_controller.rb`
- **ルーティング**: `config/routes.rb`（`resource :catalog, only: %i[edit]`）

## 備考
このページは単純なリダイレクト機能のみを提供し、実際の編集機能は各専用ページで実装されています。統一されたエントリーポイントとして機能します。 