---
title: "Obsidianおすすめプラグイン 〜日常記録、コードスニペット、ブログの下書きに〜  | necco Note | necco inc.（ネッコ）"
source: "https://necco.inc/note/49799/"
author:
  - "[[佐藤 あゆみ]]"
published: 2025-05-09
created: 2025-07-24
description: "Obsidian（オブシディアン）は、Markdownベースでテキストを管理できる、テキストエディターです。 私もここ2〜3年ほど、下記のような用途でObsidianを活用しています。 Obsidianといえば「Zett […]"
tags:
  - "web-info"
---
## 🚀 要約
- 

## 💡 学び・考察
- 

## ❓ 疑問点
- 

## 🔗 関連
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
```

---

### 元記事のハイライト
> 

### 元記事の全文
[Obsidian](https://obsidian.md/) （オブシディアン）は、Markdownベースでテキストを管理できる、テキストエディターです。 私もここ2〜3年ほど、下記のような用途でObsidianを活用しています。

- 日々の行動・思考記録
- コードスニペット集
- AIプロンプト集
- ブログの下書き
- Web Clipper（気になるウェブページのメモ）

Obsidianといえば「Zettelkasten（ツェッテルカステン）」のメモ術を採用しているユーザーが多いですが、私は現状ではZettelkastenを採用せず、Obsidianを「Markdownファイルを管理できる、動作が軽快で拡張性の高いテキストエディタ」として、ゆるく使っています。

最近では、Obsidianがプレーンテキストであることを活かし、CursorのAI機能と組み合わせても利用しています。AIがあればタグ付けや文書のまとめなども半自動で行えるので、Zettelkastenを始めてもいいかも…と考え始めているところです。

さて、 **Obsidianはさまざまなプラグインで拡張でき、自分好みのエディタに育てられる** のが大きな魅力の一つです。そこで、ここでは、私が使っているおすすめのObsidianプラグインをご紹介します。痒い所に手が届く素敵なプラグインたちです。

## 日々の記録に便利なプラグイン

### Thino

**日記やメモを、X（旧Twitter）のタイムラインのように残せる** プラグインです。

特に文字数制限などもなく、自分専用のXのタイムラインのようなものが作れます。 思いついたことをすぐに記録でき、日々のログやアイデアの蓄積に最適です。私はXの投稿の下書きにも使っています。スマホ版Obsidianでも同様に利用できるため、思いついたことをスマホでも気軽に保存できます。

![「Thino」のスクリーンショット。ダークモードで表示されており、メモのリストや「Archive」「Recycle bin」などのオプション、タグ機能が見える。](https://wordpress.necco.inc/wp-content/uploads/2025/05/theno-01.png)

「Thino」のスクリーンショット。ダークモードで表示されており、メモのリストや「Archive」「Recycle bin」などのオプション、タグ機能が見える。

ここで入力した内容は、日々のDaily Noteに反映され、通常のマークダウンファイルとして管理できます。

Twitterクローンは、少しでもプログラムを書いたことがあれば誰もが自作したことがあると思いますが、実用するとなると、メンテナンスが大変ですよね。テキストファイルの状態であれば、システムのアップデートにも影響されず、サービス終了などの恐れもなく続けられるのが良いです。

![Obsidianアプリケーションの日付が2025-05-07の日報ページのスクリーンショット。17:29にテストのメモが記載されている。](https://wordpress.necco.inc/wp-content/uploads/2025/05/theno-02.png)

Obsidianアプリケーションの日付が2025-05-07の日報ページのスクリーンショット。17:29にテストのメモが記載されている。

- [Thino](https://github.com/Quorafind/Obsidian-Thino)

### Dataview

Dataviewは、 **メモを自動で一覧表示できる** プラグインです。

日記やタスク、プロジェクトの進捗管理など、データベース的な使い方ができます。  
コードスニペットや、WebClipperで保存したメモなどを一覧表示するのに利用しています。

私はフォルダ内のファイルを一覧表示するというシンプルな用途で使っていますが、まるでSQLのような、Dataview Query Language (DQL) が用意されており、ちょっと凝ったクエリも書けるようです。

![Dataviewのスクリーンショット。フォルダ内のファイルやタグが表形式で表示されている。](https://wordpress.necco.inc/wp-content/uploads/2025/05/Dataview.png)

Dataviewのスクリーンショット。フォルダ内のファイルやタグが表形式で表示されている。

- [Dataview](https://blacksmithgu.github.io/obsidian-dataview/)

### Tag Wrangler

Obsidian上での **タグの一覧に、コンテクストメニューを表示でき** 、その場でタグのリネームなどができようになるプラグインです。地味な点かもしれませんが、便利になります。

![3Dタグのコンテクストメニューを表示した状態のスクリーンショット。Rename #3Dなど、タグに対して行える操作が表示されている。](https://wordpress.necco.inc/wp-content/uploads/2025/05/tag.png)

3Dタグのコンテクストメニューを表示した状態のスクリーンショット。Rename #3Dなど、タグに対して行える操作が表示されている。

- [Tag Wrangler](https://github.com/pjeby/tag-wrangler)

### Recent Files for Obsidian

Obsidian上で **「最近使ったファイル」の一覧** を表示できます。ファイルにすぐアクセスできるようになるので、便利です。

![左側のサイドバーに、最近開いたファイルのリストが表示されている。](https://wordpress.necco.inc/wp-content/uploads/2025/05/recent.png)

左側のサイドバーに、最近開いたファイルのリストが表示されている。

- [Recent Files for Obsidian](https://github.com/tgrosinger/recent-files-obsidian)

### Various Complements

テキストの入力時に、 **フロントマターの内容や内部リンクを補完してくれる** 、オートコンプリートプラグインです。  
実は私は現在オフにしているのですが、特にZettelkastenを実践する場合など、メモからメモにリンクを張る機会が多い場合にはとても便利なプラグインなので、ご紹介しました。

- [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin)

## コードスニペット管理に便利なプラグイン

### シンタックスハイライト

Obsidianのコードブロックは、デフォルトではプレーンなテキスト表示になります。ただ、コードはやはりシンタックスハイライトが効いている方が読みやすいですよね。  
私は [Editor Syntax Highlight Obsidian Plugin](https://github.com/deathau/cm-editor-syntax-highlight-obsidian) というプラグインで、コードのシンタックスハイライトを有効にしているのですが、どうやらこのプラグインは現在はアクティブではないようです。  
これからインストールされる方は [Obsidian Shiki Plugin](https://github.com/mProjectsCode/obsidian-shiki-plugin) など、開発が継続されているプラグインを入れると良いですね。

### Obsidian Embedded Code Title Plugin

**コードブロックでタイトルを表示できる** プラグインです。これもまた小さな部分ですが、ぱっと見で内容を把握しやすくなるのでおすすめです。

![コードスニペットのスクリーンショット。コードの上部に「css:sample.css」などのファイル名が記載されている](https://wordpress.necco.inc/wp-content/uploads/2025/05/title-01.png)

コードスニペットのスクリーンショット。コードの上部に「css:sample.css」などのファイル名が記載されている

![メモのプレビュー状態のスクリーンショット。コードの上部に「sample.css」 のファイル名が表示されている。](https://wordpress.necco.inc/wp-content/uploads/2025/05/title-02.png)

メモのプレビュー状態のスクリーンショット。コードの上部に「sample.css」 のファイル名が表示されている。

- [Obsidian Embedded Code Title Plugin](https://github.com/tadashi-aikawa/obsidian-embedded-code-title)

## ブログ下書き・執筆に役立つプラグイン

### Templater Obsidian Plugin

使っていないObsidianユーザーはいないのでは、と思われる超有名プラグインです。  
充実したオプションを持った **テンプレート機能で、メモの作成を効率化** できます。  
あるフォルダでファイルを新規作成したら、この形式のテンプレートを適用する、日付を変数として設定できるなど、様々なオプションがあります。

- [Templater Obsidian Plugin](https://github.com/SilentVoid13/Templater)
- [ObsidianのTemplaterの使い方と設定（eiji.page）](https://eiji.page/blog/obsidian-templater-howto/)

### Obsidian Auto Link Title

URLを入力したときに、 **自動的にページタイトルを取得してマークダウン形式で記述してくれる** プラグインです。  
参考リンクの整理や引用が楽になります。

- [Obsidian Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title)

### Obsidian Hover Editor

他のメモを **ポップアップで開けて** 、そのまま編集できるようになるプラグインです。

![メモを開いた画面のスクリーンショット。小さなポップアップが出ており、そこに別のメモの内容が表示されている。](https://wordpress.necco.inc/wp-content/uploads/2025/05/hover-editor.png)

メモを開いた画面のスクリーンショット。小さなポップアップが出ており、そこに別のメモの内容が表示されている。

- [Obsidian Hover Editor](https://github.com/nothingislost/obsidian-hover-editor)

## その他の便利プラグイン

### Local REST API for Obsidian

Chrome拡張機能の [Obsidian Web](https://chromewebstore.google.com/detail/obsidian-web/edoacekkjanmingkbkgjndndibhkegad?pli=1) など、外部ツールと連携したいときに役立つREST APIプラグインです。…が、改めて調べたところ、現在、公式からリリースされている [Obsidian Web Clipper](https://obsidian.md/clipper) を使う場合には、このプラグインなしでも動作するようです。  
公式のObsidian Web Clipperはまだ試していませんが、Obsidian Webの方がテンプレートなどでアレンジできる範囲が広そうです。

- [Local REST API for Obsidian](https://github.com/coddingtonbear/obsidian-local-rest-api)

### Obsidian Emo Uploader

**画像やファイルを、自動で外部サーバにアップロードできるようになる** プラグインです。  
私は文書とその他のファイルの保管場所を分けたいので、画像ファイルなどはCloudinaryにアップロードするように設定しています。人それぞれの要望に寄り添うプラグインが開発されているのが嬉しいですね。

- [Obsidian Emo Uploader](https://github.com/yaleiyale/obsidian-emo-uploader)

### Hide Folders

フォルダの一覧から、 **不要なフォルダを非表示に** できます。

私の場合、ObsidianをCursorなど別のツールで利用しているため、「node\_modules」などのObsisianでは不要なフォルダを、このプラグインで非表示にしています。  
プラグインの設定にて、「Add Hidden Folders to Obsidian Exclusion-List」オプションを有効にすれば、Obsidianの検索結果などからも該当フォルダを除外できます。

- [Hide Folders](https://github.com/JonasDoesThings/obsidian-hide-folders)

## まとめ

Obsidianはプラグインを活用することで、日々の記録からコード管理、ブログ執筆まで幅広く便利に使えるようになります。今回紹介したプラグインは、派手なものは少ないかもしれませんが、どれも実際に使って便利だったものばかりです。

プラグインを活用する難点としては、Obsidianのプラグイン開発は多くが個人開発で行われているため、開発が止まってしまうものも多いことです。それでも、開発が継続されている間だけでも「便利に使わせてもらってありがとう」という気持ちで使っています。プラグインによっては、スポンサーを募っていたり、プルリクを送って共同で開発できるようになっていますので、自分にできる形で支援していくのも、また一つの楽しみになります。

今後も、Obsidianを自分好みに楽しく使えるユーザーが増えていくことを願っています。

---

📮 **お仕事のご依頼やご相談、お待ちしております。**

お仕事のご依頼やご相談は、 [お問い合わせ](https://necco.inc/contact) からお願いいたします。

**🤝 一緒に働きませんか？**

下記の職種を募集中です。より良いデザイン、言葉、エンジニアリングをチームで追求していける方をお待ちしております。詳細は [採用情報](https://necco.inc/careers) をご覧ください。

- フロントエンドエンジニア
- アシスタントフロントエンドエンジニア

🗒 **会社案内資料もご活用ください。**

弊社のサービスや制作・活動実績、会社概要、ご契約など各種情報をまとめた資料をご用意しています。 [会社案内資料](https://necco.inc/download) からダウンロード可能ですので、ぜひご活用ください。

![株式会社necco ダウンロード資料へのバナー画像](https://wordpress.necco.inc/wp-content/uploads/2023/05/necco-dl-banner-1.png)

株式会社necco ダウンロード資料へのバナー画像

（2025年6月時点）