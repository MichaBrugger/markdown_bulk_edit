---
tags:
type:
up:
  - Unified Modelling Language
context:
  - Notation
aliases:
source: []
---

# UML Relations Notation

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
Inheritance and implementation are _class-level_ relationships, all others are _instance-level_.

![|400](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Uml_classes_en.svg/1920px-Uml_classes_en.svg.png)
