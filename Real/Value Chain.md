---
tags:
type:
up:
  - Value
context:
  - Business
aliases:
source: []
---

# Value Chain

A description of all the [[Business, Process|processes]] and activities carried out by a business and the [[Resource|resources]] and [[Capability|capabilities]] involved.

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

- [[Value, Creation]]
