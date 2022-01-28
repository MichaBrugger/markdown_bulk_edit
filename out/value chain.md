---
context:
- Business
aliases:
- value chain
title: Value Chain
domain:
- ''
---

# Value Chain

A description of all the processes and activities carried out by a business and the resources and capabilities involved.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

# Related

- [[Value, Creation
