# LatestSaleApprovalsController（Articles::LatestSaleApprovalsController）

## 概要
- 販売稟議一覧・編集・作成・更新の管理。
- `/articles/latest_sale_approvals` などで利用。

## アクション一覧

### index（6-10行目）
- **受け取るもの**: params（フィルタ条件等）
- **処理内容**: IndexFormで絞り込み、ページネーション。
- **返すもの**: @latest_sale_approvals

### edit（12-32行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleや承認履歴等を取得し、フォームや履歴をセット。
- **返すもの**: 各種インスタンス変数（ビューで利用）

### create（34-44行目）
- **受け取るもの**: params[:id], latest_sale_approval_create_params
- **処理内容**: SaleApproval作成フォームで保存。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

### update（46-51行目）
- **受け取るもの**: params[:id], latest_sale_approval_update_params
- **処理内容**: SaleApprovalのハンドラを実行。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 