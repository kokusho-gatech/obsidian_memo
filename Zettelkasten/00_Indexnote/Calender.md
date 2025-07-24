---
tags:
  - indexnote
creation-date: "20250724"
---

```dataviewjs
const _month = dv.date(dv.current().file.frontmatter.creation-date);
const monthTest = new RegExp(_month.toFormat("yyyy年MM月"))
const groupByDate = Object.groupBy(dv.pages('"Zettelkasten"')
  .filter(p => monthTest.test(p.file.frontmatter["endDate"])) , (p => {
  return p.file.frontmatter["endDate"]
}))
const table = Object.keys(groupByDate)
.map(key => {
  const links = groupByDate[key].map(p =>
    `[[${p.file.path}|${p.file.frontmatter.title.substring(0, 28)}]]`
  )
  return {
    date: key,
    content: links.join("\n\n"),
    link: groupByDate[key][0].file.path,
  }
})
renderHabitCalendar(this.container, dv, {
  format: "markdown",
  year: _month.year,
  month: _month.month,
  data: table
})
```





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