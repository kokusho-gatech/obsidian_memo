# AssessmentNgController（Articles::AssessmentNgController）

## 概要
- 査定NG一覧ページのコントローラー。
- `/articles/assessment_ng` で利用。

## アクション一覧

### index（6-10行目）
- **受け取るもの**: params（フィルタ条件等）
- **処理内容**:
  - `Article::AssessmentNg::IndexForm`をパラメータ付きで生成。
  - callで絞り込み、ID降順でページネーション。
- **返すもの**: @articles（ビューで利用）
- **外部API連携**: なし

#### index_form_permitted_params（13-16行目）
- paramsから許可された値のみを抽出。

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 