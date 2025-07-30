---
tags:
  - 書類重複確認削減Pj
creation-date: "20250730"
---

# Pjの目的

Acqusition事業部ないの各部署での同一書類に関する重複確認をなくすこと

対象部署：Contract, Settlement, Document/Main Document/Maisoku, Succession


◎：対応不要、◯：現状対応不要、△：対応必要、✖️：対応必須
必要な機能：
- 書類転記画面
	- 書類の種別選択：◯
	  6種類のみの場合対応不要。書類種別を追加する際には種別ごとのテーブルの追加やビューの調整が必要。
	  
	- 書類のバージョン選択：△
	  書類のバージョン管理を行わないスコープにした場合は対応不要。
	  
	- 書面のグラフィカル表示：対応不要
	  
	- 書類の転記入力欄と保存処理：◯
	  現状の項目のみの場合対応不要。項目追加する際にはデータカラムの追加とビューの調整が必要。
	  
	- 前回確定情報の表示機能：△
	  書類のバージョン管理を行わないスコープにした場合は対応不要。
	  
	- 確定申請/承認機能：✖️
	  現状、ステータスの単一選択のみであるため、対応必須
	  　・一定権限以上のユーザのみ確定が可能
	  　・承認、確定フェーズではデータロックをかける
	  
	- 書類紐付け：△
	  書類ファイルに対してではなく案件に対して情報を持つという方針の場合、対応不要
	  
	- 過去書類の情報をコピー：△
	  書類のバージョン管理を行わないスコープにした場合は対応不要。
	  
	- OCR読み取り結果の入力補助：◯
	  現状の項目のみの場合対応不要。項目を増やしていく場合、対応必要
	  
 - ドラフトチェックページの改修
	 - 書類情報の引用表示：◎
	 - 書類情報画面への遷移：◎
	   
 - その他画面からの遷移
	 - ファイルチェックページからの遷移：◎
	 - 一致比較info表示からの遷移：◎
	   
- その他の機能
	- 各方針で差異がないため省略

　

制約１：コントラクトチームが確認している項目のみに限定される

現状のドラフトチェックページに記載の情報のみの場合
　マイソク作成チーム　20項目⇨6項目
　契約書作成チーム　 80項目⇨16項目
　決済（FLOWユーザ）　15項目⇨
　承継（MNGユーザ）　？？





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