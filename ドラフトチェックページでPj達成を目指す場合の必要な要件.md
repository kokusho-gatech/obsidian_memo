---
tags:
  - 書類重複確認削減Pj
creation-date: "20250730"
---

# Pjの目的

Acqusition事業部ないの各部署での同一書類に関する重複確認をなくすこと

対象部署：Contract, Settlement, Document/Main Document/Maisoku, Succession


必要な機能：
　

　

制約１：コントラクトチームが確認している項目のみに限定される

現状のドラフトチェックページに記載の情報のみの場合
　マイソク作成チーム　20項目⇨6項目
　契約書作成チーム　 80項目⇨16項目

　





```dataviewjs
dv.header(3, "関連ノート");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}

for (let outgo of dv.pages('outgoing([[' + dv.current().file.name + ']])')) {
    dv.header(4, outgo.file.name);
    dv.list(outgo.file.inlinks.sort());
}

// バックリンクがあるノートも出力
let backlinks = dv.pages().where(p => p.file.inlinks && p.file.inlinks.map(l=>l.path).includes(dv.current().file.path));
if (backlinks.length > 0) {
    dv.header(3, "このノートへのバックリンク");
    dv.list(backlinks.file.link);
}

```