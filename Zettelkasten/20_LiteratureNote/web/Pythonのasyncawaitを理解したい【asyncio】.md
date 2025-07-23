---
title: "Pythonのasync/awaitを理解したい【asyncio】"
source: "https://zenn.dev/iharuoru/articles/45dedf1a1b8352"
author:
  - "[[Zenn]]"
published: 2024-09-23
created: 2025-07-23
description:
tags:
  - "web-info"
---
---
title: "Pythonのasync/awaitを理解したい【asyncio】"
aliases: []
url: "https://zenn.dev/iharuoru/articles/45dedf1a1b8352"
source: ""
author: ""
date: ""
tags: [📥/webclip, ⚪️/toread]
status: "to-read"
---

## 🚀 要約
- 

## 💡 学び・考察
- 

## ❓ 疑問点
- 

## 🔗 関連
- [[ ]]

---

### 元記事のハイライト
> 

### 元記事の全文
26

5[tech](https://zenn.dev/tech-or-idea)

## 用語

概念を理解するために、非同期処理で何が起きているかを把握します。

- **イベントループ** ：タスクをスケジュールする
- **タスク** ：コルーチンを実行し、実行結果などを管理する
- **コルーチン** ：実行や一時停止ができる処理

私たちはやりたいことをコルーチンで書いてタスクにしてイベントループに入れるだけで、イベントループがうまいこと処理してくれる、というイメージです。

ここでいううまいこととは、CPUを使わないのに何秒もかかるタスクがあるときに、代わりに別のタスクにCPUを使わせる、といった具合です。

これらのことをするために、Pythonの標準ライブラリである `asyncio` を使用します。

## コルーチンを作成する（async）

コルーチンを作成するのは簡単で、 `def` の前に `async` をつけるとコルーチン関数ができます。

```python
# 通常の関数(同期関数)
def main():
    print('hello world')

# コルーチン関数(非同期関数)
async def async_main():
    print('hello async world')
```

通常の関数は以下の通りで、実行するとすぐに結果が返ってきます。

```python
>>> main()
hello world
```

コルーチン関数は実行すると、 **コルーチンオブジェクト** を返すようになります。

```python
>>> async_main()
<coroutine object main at 0x123456789>
```

コルーチンを実行するには `asyncio.run` をします。

```python
>>> asyncio.run(async_main())
hello async world
```

## コルーチンの完了を待つ（await）

コルーチンは一時停止ができる処理と書きました。何か別の処理が完了するまで待つ時には `await` を使います。  
1秒かかる `hello` というコルーチンを `main` で行うとします。その際、 `hello` が完了するまで待つために `await` をつけます。

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def main():
    await hello() # helloの完了を待つ
```

これを実行すると以下のようになります。

```
>>> asyncio.run(main())
I say,
hello
```

一方で、awaitをつけないと単に **コルーチンオブジェクト** を生成しているだけなので何も起きません。

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def main():
    hello() # awaitがない
```

これを実行すると `hello` が待たれていないというエラーが出ます。

```
>>> asyncio.run(main())
RuntimeWarning: coroutine 'hello' was never awaited
```

最初にコルーチンはタスクとして実行されると書きました。実はコルーチンを `await` すると、内部的にタスクが作成されコルーチンが実行されます。

なお、 `await` は一時停止をすることが目的なので `async` の中でしか書けません。  
一方で、 `asyncio.run` は同期関数からコルーチンを実行することが目的なので `async` の中では書けません。

## タスクを作成する

コルーチンは明示的にタスクを作成して実行することもできます。  
`asyncio.create_task` を使うと、 **コルーチンオブジェクト** を **タスクオブジェクト** にして実行できます。

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def main():
    await asyncio.create_task(hello()) # helloタスクの完了を待つ
```

これを実行すると以下のようにコルーチンを `await` した時と同じ結果になります。

```python
>>> asyncio.run(main())
I say,
hello
```

一方で、 `await` しなかった場合の挙動は少し異なります。

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def main():
    asyncio.create_task(hello())
```

```python
>>> asyncio.run(main())
I say,
```

`asyncio.create_task` では、タスクの **実行** も行われます。  
そのため、 `print('I say,')` は実行されていますが `main` は `hello` の完了を待たないため `print('hello')` は実行されません。

---

## 複数のコルーチンを制御する

ここまででコルーチンとタスクを紹介しましたが、違いはどこに現れるのでしょうか。

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def goodbye():
    print('you say,')
    await asyncio.sleep(2) # 2秒かかる
    print('goodbye')

async def main():
    await goodbye()
    await hello()
```

これを実行すると3秒かかり以下のようになります。

```
>>> asyncio.run(main())
you say,
goodbye
I say,
hello
```

`goodbye` の完了を待ってから `hello` の実行をしているためです。

`asyncio.create_task` を使った場合

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def goodbye():
    print('you say,')
    await asyncio.sleep(2) # 2秒かかる
    print('goodbye')

async def main():
    goodbye_task = asyncio.create_task(goodbye())
    hello_task = asyncio.create_task(hello())
    await goodbye_task
    await hello_task
```

これを実行すると2秒かかり以下のようになります。

```
>>> asyncio.run(main())
you say,
I say,
hello
goodbye
```

`hello` と `goodbye` はともに実行されており、実行された順に `print('you say,')` と `print('I say,')` が実行されます。  
`print('goodbye')` は2秒後に実行されるので、先に `print('hello')` が実行されます。

`asyncio.gather` を使うことで、複数のコルーチンを並行に実行することができます。  
コルーチンもタスクも使用することができます。

```python
async def hello():
    print('I say,')
    await asyncio.sleep(1) # 1秒かかる
    print('hello')

async def goodbye():
    print('you say,')
    await asyncio.sleep(2) # 2秒かかる
    print('goodbye')

async def main():
    await asyncio.gather(goodbye(), hello(), hello()) # タスクも同様
```

これを実行すると2秒かかり以下のようになります。

```
>>> asyncio.run(main())
you say,
I say,
I say,
hello
hello
goodbye
```

## 参考

26

5

26

5