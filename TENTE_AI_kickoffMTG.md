---
tags: []
creation-date: "20250806"
---

# タイトル

AIを選んだ目的：
　馬場さん：
　 - AIについて詳しくなる
　 - PdM間でのAIについての共通認識を作りたい
	　 - どういうツールを使うなど
　 - 他社事例

　栗原さん：
　　- TENETの企画目的
	　　- 活動を通したPdMのエキスパート化
	　　- 集合知を作って共通認識をつくる

　しょうさん：
　　- AI関連の共通した社内ノウハウを集めたい


メンバーのAI利用
- 利用ツールとどのような使い方をしている
	- 

　



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