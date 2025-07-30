---
tags: []
creation-date: "20250730"
---

コンフルURL: [査定自動化Ph.1のプロジェクト概要書](https://ga-tech.atlassian.net/wiki/spaces/SUPPLIER/pages/4113498553/SUP+2025+Ph.1)





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