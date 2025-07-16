# LatestApprovalsController（Articles::LatestApprovalsController）

## 概要
- 仕入稟議一覧・編集・作成・更新の管理。
- `/articles/latest_approvals` などで利用。

## アクション一覧

### index（6-10行目）
- **受け取るもの**: params（フィルタ条件等）
- **処理内容**: IndexFormで絞り込み、ページネーション。
- **返すもの**: @latest_approvals

### edit（12-28行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleや承認履歴等を取得し、タブHTML生成。
- **返すもの**: 各種インスタンス変数（ビューで利用）

### create（30-41行目）
- **受け取るもの**: params[:id], latest_approval_params
- **処理内容**: Approval作成フォームで保存。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

### update（43-48行目）
- **受け取るもの**: params[:id], latest_approval_params
- **処理内容**: Approvalのハンドラを実行。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 