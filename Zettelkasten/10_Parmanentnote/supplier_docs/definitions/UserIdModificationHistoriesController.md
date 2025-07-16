# UserIdModificationHistoriesController（IntermediaryCompanies::UserIdModificationHistoriesController）

## 概要
- 仲介会社のユーザーID変更履歴一覧ページのコントローラー。
- `/intermediary_companies/:intermediary_company_id/user_id_modification_histories` で利用。

## アクション一覧

### index（6-9行目）
- **受け取るもの**: params[:intermediary_company_id]
- **処理内容**: IntermediaryCompanyを取得し、そのuser_id_modification_historiesを取得。
- **返すもの**: @intermediary_company, @user_id_modification_histories

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 