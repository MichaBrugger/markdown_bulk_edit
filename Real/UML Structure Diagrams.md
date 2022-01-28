---
type:
tags: 
up:
  - Unified Modelling Language
context:
aliases:
source:
---

# Structure Diagrams

Structure diagrams represent the static aspects of the system.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
