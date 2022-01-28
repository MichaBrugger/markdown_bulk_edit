---
alias:
- Java, Structure
title: Java, Structure
domain:
- ''
aliases:
- java, structure
---

# Structure

!750

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```