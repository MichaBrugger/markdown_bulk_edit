---
context:
source: []
tags: 
type:
up:
  - Programming Language
aliases:
  - high-level programming language
---

# High Level Programming Languages

Unfortunately, [[Hardware|computer hardware]] does not understand high-level languages. Therefore, all high-level languages must be translated into a low-level language using a [[Compiler]].

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file) ||
  page.context && page.context.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
