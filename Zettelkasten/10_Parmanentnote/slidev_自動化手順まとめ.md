---
タグ: #Slidev #自動化 #Zettelkasten #スライド #Obsidian
---
# ZettelkastenメモをSlidevスライドに反映・起動する手順まとめ

---

## 1. メモの準備

- Zettelkastenディレクトリ内（例：20_LiteratureNoteや30_FeelingNoteなど）にある.mdファイル（メモ）を確認する。
- スライド化したいメモを選定する。

## 2. Slidev用スライド（slides.md）の作成

- 選定したメモの要点や引用、ハイライトを抽出し、Slidev形式（Markdown）でまとめる。
- テーマやタイトル、スライド構成を決める。
- 例：slidev/slides.md に保存

## 3. Slidevの起動方法

1. 必要なパッケージがインストールされていることを確認（`npm install`）
2. slidevディレクトリに移動
   ```
   cd slidev
   ```
3. ローカルサーバーを起動
   ```
   npm run dev
   ```
4. 表示されたURL（例：http://localhost:3030）をブラウザで開く

## 4. 注意点
- slidevコマンドが使えない場合は、`npm run dev`で起動する
- スライドの内容を更新した場合は、サーバーを再起動するか、ブラウザをリロードする

## 5. まとめ
- Zettelkasten内のメモを活用し、効率的にスライド資料を作成・発表できる
- テーマや構成は自由にカスタマイズ可能

---

## 6. LLM（AI）へのプロンプト例

### スライド作成・更新用プロンプト例

#### 1. 新規スライド作成
```
Zettelkasten/20_LiteratureNote/〇〇.md をもとに、slidev用のスライド（テーマはbricks）を作成してください。
要点・引用・ハイライトを反映し、slidev/slides.mdに出力してください。
```

#### 2. 既存スライドへの追記・修正
```
slidev/slides.md の内容に、Zettelkasten/30_FeelingNote/△△.md の要素を追加して、スライドをアップデートしてください。
```

#### 3. スライドの構成やテーマ変更
```
slidev/slides.md のテーマをseriphに変更し、章立てを再構成してください。
```

### サーバー起動用プロンプト例

```
slidev/slides.md をサーバーで起動してください。
```
または
```
slidevディレクトリで npm run dev を実行し、スライドをブラウザで開いてください。
```

---

AIに依頼する際は、
- どのメモを元にするか
- どのテーマや構成にしたいか
- どのファイルに出力するか
- サーバー起動の有無
などを明確に伝えると、より正確な自動化が可能です。

---

## 7. Slidevのインストール方法

### 1. プロジェクトごとにインストール（推奨）
```
npm init slidev@latest
```
対話形式でプロジェクト名やテーマを選択できます。

### 2. 既存プロジェクトでslidevを追加
```
npm install --save-dev @slidev/cli
```

### 3. グローバルインストール（非推奨）
```
npm install -g @slidev/cli
```

---

## 8. 指定できる主なテーマ名

- default
- seriph
- apple-basic
- apple-raw
- shibuya
- sakura
- serif
- simple
- windicss
- fun
- league
- dark
- uncover
- bricks
- peach
- avocad
- panda
- cyberpunk
- navy
- sakura
- seriph
- apple-basic
- apple-raw

※テーマはnpmで追加インストールも可能です。詳細は[Slidev公式テーマギャラリー](https://sli.dev/resources/theme-gallery)参照。

---

## 9. Slidevの主なショートカット

| キー操作                | 機能                         |
|-------------------------|------------------------------|
| → / space               | 次のスライド・アニメーション |
| ← / shift + space       | 前のスライド・アニメーション |
| ↑                       | 前のスライド                 |
| ↓                       | 次のスライド                 |
| p                       | プレゼンターモード           |
| o                       | オーバービューモード         |
| f                       | フルスクリーン               |
| esc                     | フルスクリーン解除           |
| c                       | コメント（ノート）表示       |
| s                       | スライドのソースを開く       |
| g                       | スライドジャンプ             |
| /                       | 検索                        |

---

（この手順メモは自動生成されました） 