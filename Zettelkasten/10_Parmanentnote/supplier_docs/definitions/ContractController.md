---
tags:
  - definition
  - controller
  - ruby-on-rails
  - supplier
  - parmanentnote
---

# ContractController

> 本来のクラス名は ContractController です

---

## アクション一覧と詳細

### `release` (出典: app/controllers/contract_controller.rb:6)

* **機能概要:**
  物件情報を外部サービス（TechConsul）へ連携・リリースする。
* **処理フロー:**
    1. 物件取得・ユーザー情報セット（:7-9）
    2. update_and_upload!で物件情報・ファイルを更新（private:19-22）
    3. Connectors::TechConsul経由でrelease!（:11-12）
    4. 成功時はJSONメッセージ、失敗時はエラーレスポンス（:13-18）
* **外部連携:**
    - Connectors::TechConsul（:12）
    - Notifier（:16）
* **返すもの:**
    - 成功時はJSON、失敗時はエラーメッセージ

---

## 関連リンク
- [[Article]]
- [[TechConsul]]
- [[外部API連携]] 