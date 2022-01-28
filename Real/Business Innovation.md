---
context:
  - Innovation
source: []
tags: 
type:
up:
  - Business
aliases:
---

# Business Innovation

"Business Innovation ist die systematische Planung, Steuerung und Kontrolle von Innovationen in und zwischen Organisationen. Gegenstand der [[Innovation|Innovationen]] sind [[Product|Produkte]] und [[Service|Dienstleistungen]], [[Business, Process|Prozesse]] und [[Business Model|Geschäftsmodelle]]." [^1]

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
