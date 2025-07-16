# NegotiatedSameBuildingAndFloorArticlesController

> 本来のクラス名は Articles::NegotiatedSameBuildingAndFloorArticlesController です

---

## アクション一覧と詳細

### `index` (出典: app/controllers/articles/negotiated_same_building_and_floor_articles_controller.rb:6)

* **機能概要:**
  同一建物・同一階の交渉物件一覧を表示。
* **処理フロー:**
    1. ArticleをIDで取得（:7）
    2. negotiated_same_building_and_floor_inをpreloadで取得（:8-13）
* **返すもの:**
    - 一覧画面のHTML

---

## 関連リンク
- [[Article]]
- [[NegotiationHistory]] 