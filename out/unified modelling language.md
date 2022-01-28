---
context:
- Software Engineering
aliases:
- unified modelling language
title: Unified Modelling Language
domain:
- ''
---

# Unified Modelling Language

UML is a form of [[Object Oriented Modelling and offers different kinds of diagrams to model static system structures and dynamic runtime behaviour.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
