---
context:
- Language
aliases:
- programming language
title: Programming Language
domain:
- ''
---

# Programming Languages

A programming language is a special language used to write computer programs.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
