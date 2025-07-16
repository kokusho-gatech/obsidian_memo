# ConsumptionTaxVersionsController（Articles::ConsumptionTaxVersionsController）

## 概要
- 消費税計算履歴の新規作成・表示・保存・最新取得。
- `/articles/:id/consumption_tax_versions` で利用。

## アクション一覧

### show（8-12行目）
- **受け取るもの**: params[:id], params[:consumption_tax_version_id]
- **処理内容**: Article・SalesContractField・ConsumptionTaxVersionを取得。
- **返すもの**: 各インスタンス変数（ビューで利用）

### new（14-20行目）
- **受け取るもの**: params[:id]
- **処理内容**: Article・SalesContractFieldを取得し、新規ConsumptionTaxVersionを初期化。
- **返すもの**: 各インスタンス変数（ビューで利用）

### create（22-36行目）
- **受け取るもの**: params[:id], consumption_tax_version_params
- **処理内容**: Article・SalesContractFieldを取得し、消費税計算結果を保存。
- **返すもの**: フラッシュメッセージ、詳細画面へリダイレクト

### last（38-66行目）
- **受け取るもの**: params[:id]
- **処理内容**: Article・SalesContractField・最新ConsumptionTaxVersionを取得し、状態に応じて分岐。
- **返すもの**: 詳細画面表示または新規作成画面へリダイレクト

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 