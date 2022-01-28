---
context: null
aliases:
- value
title: Value
domain:
- ''
---

# Value

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

## Notes

Should this be merged with value dimension of the business model? #♻️
