
```dataviewjs
dv.table(
  ["file", "status"],
  dv.pages()
    .map(p => [
        dv.fileLink(p.file.path, false, p.file.frontmatter.title),
        p.file.frontmatter.status
    ])
)
```



