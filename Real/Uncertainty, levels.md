---
tags:
type:
up:
  - Uncertainty
context:
aliases:
source: []
---

# Uncertainty, Levels

Courtney et al. define four different levels of [[Uncertainty|uncertainty]]:[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

Their experience suggests that at least half of all [[Strategy, Problems|strategy problems]] fall into levels 2 or 3, while most of the rest are level 1 problems.
