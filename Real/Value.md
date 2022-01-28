---
tags:
type: ['moc']
up: ['Terminology']
context:
aliases:
source: []
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

Should this be merged with [[Business Model Dimensions, Value|value dimension of the business model]]? #♻️