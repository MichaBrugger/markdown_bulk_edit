---
context: null
aliases:
- uml interaction diagrams
title: UML Interaction Diagrams
domain:
- ''
---

# Interaction Diagrams

Both diagram types are used to describe the behaviour within a use-case in more detail and they both don't offer a formal description. They describe how a group of objects interact with each other, e.g. amount of objects involved, exchange of messages, etc.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
