---
context:
- Framework
aliases:
- business model navigator
title: Business Model Navigator
domain:
- ''
---

# Business Model Navigator

The Business Model Navigator is a comprehensive business model innovation tool developed at the industries. The Navigator has been developed on the basis of empirical studies of several hundred business models and practical applications in a large number of companies.[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```

[^1]: [source::20220103-1459-BusinessModelNavigatorStrategies]
