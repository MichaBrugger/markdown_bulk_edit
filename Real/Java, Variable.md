---
context:
source: []
tags: 
type:
up:
  - Java, Structure
aliases:
  - variable
  - Java variable
---

# Variables in Java

A [[Java]] variable is a piece of memory that can contain a data value. A variable thus has a [[Java, Data Types|data type]]. Generally speaking, there are four different types of variables in Java:[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```

[^1]: [source::20220102-0655-JavaVariables]
