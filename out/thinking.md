---
context: null
aliases:
- thinking
title: Thinking
domain:
- ''
---

# Thinking

This could probably be split into multiple 'schools of thought'.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```
