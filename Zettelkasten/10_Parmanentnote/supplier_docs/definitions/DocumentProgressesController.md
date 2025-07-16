# DocumentProgressesController（Articles::DocumentProgressesController）

## 概要
- 契約書作成進捗一覧・編集・更新。
- `/articles/document_progresses` で利用。

## アクション一覧

### index（6-23行目）
- **受け取るもの**: params（検索条件等）
- **処理内容**: 検索条件を取得し、カードリストビルダーで進捗情報を生成。
- **返すもの**: @document_progress_info, @labels, @search_conditions

### edit（25-38行目）
- **受け取るもの**: params[:id]
- **処理内容**: Article・DocumentProgress・ラベル・履歴・管理者情報をセット。
- **返すもの**: 各種インスタンス変数（ビューで利用）

### update（40-67行目）
- **受け取るもの**: params[:id], document_progress_params
- **処理内容**: Article・DocumentProgressを取得し、管理者権限チェック・更新。
- **返すもの**: フラッシュメッセージ、編集画面へリダイレクト or エラー時は再描画

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 