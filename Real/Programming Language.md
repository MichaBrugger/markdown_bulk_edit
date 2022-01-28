---
source: []
tags:
type:
  - moc
up:
  - Programming
context:
  - Language
aliases:
---

# Programming Languages

A programming language is a special language used to write computer [[Program|programs]].

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
