# SaleMaisokuProgresses__CheckersController

> 本来のクラス名は SaleMaisokuProgresses::CheckersController です

---

## アクション一覧と詳細

### `update` (出典: app/controllers/sale_maisoku_progresses/checkers_controller.rb:5)

* **機能概要:**
  マイソクチェック担当者の更新。
* **処理フロー:**
    1. SaleMaisokuProgressをIDで取得（:6）
    2. 権限チェック（:8）
    3. update_checkerで担当者を更新（:9-11）
    4. 成功/失敗時はフラッシュ・リダイレクト（:12-18）
* **返すもの:**
    - リダイレクト

---

## 関連リンク
- [[SaleMaisokuProgress]]
- [[権限管理]] 