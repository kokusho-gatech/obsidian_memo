# IntermediaryCompanies__StatusesController

> 本来のクラス名は IntermediaryCompanies::StatusesController です

---

## アクション一覧と詳細

### `update` (出典: app/controllers/intermediary_companies/statuses_controller.rb:5)

* **機能概要:**
  仲介会社のステータスを「確認済み」に更新。
* **処理フロー:**
    1. 仲介会社をIDで取得（:6）
    2. 権限チェック（:8-10）
    3. ステータスを:checkedに更新（:12-16）
    4. 成功/失敗時はフラッシュ・リダイレクト（:17-19）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
- [[IntermediaryCompany]]
- [[権限管理]] 