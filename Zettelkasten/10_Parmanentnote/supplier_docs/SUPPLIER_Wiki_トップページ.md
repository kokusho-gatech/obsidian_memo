---
tag: wiki/ページ名
alias:
  - 別名1
  - 別名2
status: draft # draft, review, published など
created: <% tp.file.creation_date("YYYY-MM-DD") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD") %>
related: # 関連する他のWikiページへの内部リンク
  - "[[関連ページ1]]"
  - "[[関連ページ2]]"
projects: # 関連するプロジェクトの内部リンク
  - "[[プロジェクトA]]"
  - "[[プロジェクトB]]"
---

# {{title}}

---

## 概要

このセクションには、ページの主題に関する簡潔な説明を記述します。読者が一目で内容を理解できるよう、要点をまとめてください。

---

## 詳細

ページの主題に関する具体的な情報、詳細な説明、背景などを記述します。必要に応じて、サブセクションを設けて情報を整理してください。

### サブセクション1

- 項目1
- 項目2

### サブセクション2

- 項目A
- 項目B

---

## 関連情報・参照

- 関連する外部サイトや資料へのリンク
  - [外部サイト名](URL)
  - [参照資料名](URL)
- 補足事項や追加情報

---

## Dataviewクエリ例

このページに関連する情報をDataviewで表示するためのクエリ例をここに記述しておくと便利です。例えば、このページを`related`に含む他のページをリストアップするなど。

```dataviewjs
LIST FROM [[{{title}}]]
WHERE related = this.file.link
SORT file.name ASC
```