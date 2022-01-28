---
context:
- Innovation
aliases:
- business innovation
title: Business Innovation
domain:
- ''
---

# Business Innovation

"Business Innovation ist die systematische Planung, Steuerung und Kontrolle von Innovationen in und zwischen Organisationen. Gegenstand der Innovationen sind Produkte und Dienstleistungen, Prozesse und Geschäftsmodelle." [^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.value != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

[^1]: [source::20220110-0914-StGallerBusinessInnovationModell]
