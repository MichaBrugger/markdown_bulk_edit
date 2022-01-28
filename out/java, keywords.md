---
context: null
aliases:
- java, keywords
title: Java, Keywords
domain:
- ''
---

# Java Keywords

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
