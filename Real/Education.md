---
tags:
type:
up:
  - Terminology
context:
aliases:
source: []
---

# Education

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.values != null && page.up.values.includes(file) ||
  page.context && page.context.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
