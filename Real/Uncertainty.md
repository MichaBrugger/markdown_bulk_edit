---
tags:
type:
up:
context:
aliases:
  - uncertainty
source: []
---

# Uncertainty

Even the most uncertain environments usually contain some information.
- often there are [[Trend|trends]]
- some factors could be knowable through analysis

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```
