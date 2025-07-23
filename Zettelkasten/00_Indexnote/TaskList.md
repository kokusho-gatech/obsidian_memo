---
tags:
  - タスク管理
  - インデックスノート
  - dataview
---

#  未完了タスク
```dataview
TASK  
WHERE !completed and file.text != ""
group by file.link

```


```
```






