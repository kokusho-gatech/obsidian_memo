# NegotiationSchedulesController（Articles::NegotiationSchedulesController）

## 概要
- 交渉スケジュールの作成・更新。
- `/articles/:article_id/negotiation_schedules` で利用。

## アクション一覧

### create（6-7行目）
- **受け取るもの**: params[:article_id], negotiation_schedule_params
- **処理内容**: updateアクションを呼び出し。
- **返すもの**: updateの返り値

### update（9-20行目）
- **受け取るもの**: params[:article_id], negotiation_schedule_params
- **処理内容**: Articleを取得し、交渉スケジュールを更新。
- **返すもの**: フラッシュメッセージ、:saveビュー

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 