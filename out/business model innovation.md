---
context:
- Das St.Galler Business-Innovation Modell
aliases:
- business model innovation
title: Business Model Innovation
domain:
- ''
---

# Business Model Innovation

For a true business model innovation to be affected, at least two of the four business model dimensions (who-what-how-value) have to be reconfigured. Successful business model innovation ‘creates value and captures value’ for a company.

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```
