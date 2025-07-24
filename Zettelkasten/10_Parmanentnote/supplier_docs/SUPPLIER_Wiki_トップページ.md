---
tags:
  - spec
  - supplier
  - wiki
  - navigation
  - parmanentnote
---
# SUPPLIER by RENOSY システム仕様Wiki

> **SUPPLIER by RENOSY**は、不動産の仕入れ業務を効率化・高度化するための業務システムです。このWikiでは、システムの技術仕様、アーキテクチャ、機能詳細を体系的に整理しています。

<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wikipedia風ページ</title>
    <style>
        /* style.css の内容をここに直接記述します */
        body {
            font-family: sans-serif;
            margin: 0;
            background-color: #f8f9fa; /* Wikipediaの背景色に近い */
            color: #202122;
        }

        .container {
            max-width: 980px; /* Wikipediaのコンテンツ幅に近い */
            margin: 0 auto;
            padding: 0 20px;
        }

        /* ヘッダー */
        #header {
            background-color: #fbfbfb;
            border-bottom: 1px solid #a7d7f9;
            padding: 10px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        #header .logo a {
            font-weight: bold;
            font-size: 1.5em;
            color: #000;
            text-decoration: none;
        }

        #header .main-nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
        }

        #header .main-nav li {
            margin-right: 20px;
        }

        #header .main-nav a {
            text-decoration: none;
            color: #006621; /* Wikipediaのリンク色に近い */
        }

        #header .search-bar input {
            border: 1px solid #a7d7f9;
            padding: 5px;
            border-radius: 3px;
        }

        #header .search-bar button {
            background-color: #f0f0f0;
            border: 1px solid #a7d7f9;
            padding: 5px 10px;
            border-radius: 3px;
            cursor: pointer;
        }

        /* メインコンテンツ */
        #main-content {
            display: flex;
            padding-top: 20px;
        }

        /* サイドバー */
        #sidebar {
            width: 200px; /* サイドバーの幅 */
            margin-right: 30px;
            padding-right: 20px;
            border-right: 1px solid #eaecf0;
        }

        #sidebar .toc h2,
        #sidebar .sidebar-links h3 {
            font-size: 1.1em;
            border-bottom: 1px solid #eaecf0;
            padding-bottom: 5px;
            margin-bottom: 10px;
        }

        #sidebar ul {
            list-style: none;
            padding: 0;
            margin-bottom: 20px;
        }

        #sidebar li {
            margin-bottom: 5px;
        }

        #sidebar a {
            text-decoration: none;
            color: #006621;
        }

        /* 記事コンテンツ */
        #article-content {
            flex-grow: 1;
        }

        #article-content h1 {
            font-size: 2em;
            border-bottom: 1px solid #eaecf0;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        #article-content h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #a2a9b1; /* Wikipediaの見出し下線色 */
            padding-bottom: 5px;
            margin-top: 30px;
            margin-bottom: 15px;
        }

        #article-content p {
            line-height: 1.6;
            margin-bottom: 1em;
        }

        #article-content ul {
            margin-left: 20px;
            margin-bottom: 1em;
        }

        #article-content a {
            color: #006621;
            text-decoration: none;
        }

        /* フッター */
        #footer {
            background-color: #f8f9fa;
            border-top: 1px solid #eaecf0;
            padding: 20px 0;
            text-align: center;
            margin-top: 40px;
        }

        #footer ul {
            list-style: none;
            padding: 0;
            display: inline-block; /* インラインブロックにして横並びにする */
        }

        #footer li {
            display: inline;
            margin: 0 10px;
        }

        #footer a {
            text-decoration: none;
            color: #006621;
        }
    </style>
</head>
<body>
    <header id="header">
        <div class="container">
            <div class="logo">
                <a href="#">Wikipedia</a>
            </div>
            <nav class="main-nav">
                <ul>
                    <li><a href="#">メインページ</a></li>
                    <li><a href="#">最近の更新</a></li>
                    <li><a href="#">おまかせ表示</a></li>
                </ul>
            </nav>
            <div class="search-bar">
                <input type="text" placeholder="検索">
                <button>検索</button>
            </div>
        </div>
    </header>

    <div id="main-content" class="container">
        <aside id="sidebar">
            <nav class="toc">
                <h2>目次</h2>
                <ul>
                    <li><a href="#section1">1 導入</a></li>
                    <li><a href="#section2">2 歴史</a></li>
                    <li><a href="#section3">3 特徴</a></li>
                    <li><a href="#section4">4 関連項目</a></li>
                </ul>
            </nav>
            <div class="sidebar-links">
                <h3>ツール</h3>
                <ul>
                    <li><a href="#">リンク元</a></li>
                    <li><a href="#">関連ページの更新状況</a></li>
                    <li><a href="#">ファイルをアップロード</a></li>
                </ul>
            </div>
        </aside>

        <article id="article-content">
            <h1>ページのタイトル</h1>
            <p>これはWikipedia風ページのサンプルです。</p>

            <h2 id="section1">1 導入</h2>
            <p>ここに導入に関するテキストが入ります。Wikipediaの記事のように、詳細な情報を提供します。</p>
            <p>Wikipediaは、様々な分野の情報を網羅するオンライン百科事典です。</p>

            <h2 id="section2">2 歴史</h2>
            <p>Wikipediaの歴史に関するテキストです。</p>
            <ul>
                <li>2001年1月15日: Wikipediaがプロジェクトを開始</li>
                <li>...</li>
            </ul>

            <h2 id="section3">3 特徴</h2>
            <p>Wikipediaの主な特徴についての記述です。</p>
            <p>誰でも編集できるオープンなプラットフォームであり、多言語で利用可能です。</p>

            <h2 id="section4">4 関連項目</h2>
            <ul>
                <li><a href="#">関連するトピック1</a></li>
                <li><a href="#">関連するトピック2</a></li>
            </ul>
        </article>
    </div>

    <footer id="footer">
        <div class="container">
            <p>&copy; 2025 Wikipedia風ページ</p>
            <ul>
                <li><a href="#">プライバシーポリシー</a></li>
                <li><a href="#">利用規約</a></li>
            </ul>
        </div>
    </footer>
</body>
</html>

## 📝 最近の更新

```dataviewjs
dv.header(3, "最近更新されたドキュメント");
dv.list(dv.pages("#spec AND #supplier").sort(f => f.file.mtime.ts, "desc").limit(10).file.link);
```

---

## 🔗 関連リンク

- **[[SUPPLIER by RENOSY]]** - プロダクト概要
- **[[Ruby on Rails 探検ガイド]]** - Railsアプリケーションの探検方法

---

*このWikiは継続的に更新されています。新しい情報や改善提案があれば、お気軽にお知らせください。* 