---
context:
- Java, Keywords
aliases:
- java, access modifiers
title: Java, Access Modifiers
domain:
- ''
---

# Access Modifiers

Default: The access level of a default modifier is only within the package. It cannot be accessed from outside the package. If you do not specify any access level, it will be the default.
```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.context && page.context.values != null && page.context.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```

!600[^1]

[^1]: [source::20220102-1515-BibliotheksklassenUndKlassenentwurf]
