---
context:
source: []
tags: 
type:
up:
  - Business Model Navigator
aliases:
  - Magic Triangle
---

# Business Model, Dimensions

A business model consists of four components:[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```

![[Pasted image 20220103173102.png]][^2]

[^1]: [source::20220103-1459-BusinessModelNavigatorStrategies]
[^2]: [source::20220102-1704-GeschaftsmodelleEntwickelnVL1]
