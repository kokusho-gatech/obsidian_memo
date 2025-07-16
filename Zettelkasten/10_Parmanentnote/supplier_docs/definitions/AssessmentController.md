# AssessmentController

> 本来のクラス名は AssessmentController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/assessment_controller.rb:5)

* **機能概要:**
  査定物件の一覧を検索・集計し、画面表示する。
* **処理フロー:**
    1. 検索パラメータを取得（:6-7）
    2. サプライヤーユーザーの場合は自身のメールアドレスで絞り込み（:8-11）
    3. left_outer_joinsで関連テーブルを結合（:13-15, private:28-47）
    4. active/on_sale/assessmentな物件を絞り込み（:16-19）
    5. select_queryで必要カラムのみ取得（private:49-63）
    6. Ransackで検索条件を構築（:21）
    7. 検索結果をincludesで関連情報を付与し、ページネーション（:22-27）
    8. 仲介会社一覧も取得（:28）
* **返すもの:**
    - 一覧画面のHTML

---

## 関連リンク
- [[Article]]
- [[査定]] 