# ApprovedApprovalsController

> 本来のクラス名は Articles::ApprovedApprovalsController です

---

## アクション一覧と詳細

### `show` (出典: app/controllers/articles/approved_approvals_controller.rb:6)

* **機能概要:**
  承認詳細の表示。条件によりリダイレクト。
* **処理フロー:**
    1. Article・Approval・ApprovalDetailをIDで取得（:7-9）
    2. dealt_articles・last_acted_approval_status_historyを取得（:10-11）
    3. 承認済みかつ詳細があれば表示、それ以外はリダイレクト（:13-15）
* **返すもの:**
    - 詳細画面のHTMLまたはリダイレクト

---

## 関連リンク
- [[Article]]
- [[Approval]] 