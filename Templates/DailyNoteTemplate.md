---
tags:
  - daily-note/task
creation-date: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.date.now("YYYY-MM-DD") %>

 

前日のデイリーNote: [[<% tp.date.now("YYMMDD", -1) %>]]
## TODO
- [x] 
- [x] 
- [x] 

## MEMO
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：

## JOURNAL
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：

## STUDY
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：

## EXPERIENCE
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：
# <% tp.date.now("YYYY-MM-DD") %>

 

前日のデイリーNote: [[<% tp.date.now("YYMMDD", -1) %>]]
## TODO
- [x] 
- [x] 
- [x] 

## MEMO
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：

## JOURNAL
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：

## STUDY
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：

## EXPERIENCE
- <% tp.date.now("HH:mm") %> ：
- <% tp.date.now("HH:mm") %> ：


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