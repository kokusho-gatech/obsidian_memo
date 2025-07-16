# UwanoseMaisokusController（Articles::UwanoseMaisokusController）

## 概要
- 上乗せ営業図面の表示。
- `/articles/:id/uwanose_maisokus` で利用。

## アクション一覧

### show（6-22行目）
- **受け取るもの**: params[:id]
- **処理内容**: Articleを取得し、HTML/PDFで出力。
- **返すもの**: PDFまたはエラー

---

[コントローラー一覧に戻る](../supplier_controllers_index.md) 