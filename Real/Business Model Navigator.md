---
context:
  - Framework
source: []
tags: 
type:
up:
  - Business Model Innovation
aliases:
---

# Business Model Navigator

The Business Model Navigator is a comprehensive [[Business Model Innovation|business model innovation]] tool developed at the [[University of St.Gallen]]. At the core of the Navigator methodology is creative imitation of existing business models in different [[Industry|industries]]. The Navigator has been developed on the basis of empirical studies of several hundred business models and practical applications in a large number of companies.[^1]

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
