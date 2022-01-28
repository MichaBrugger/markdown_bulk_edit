---
context:
  - Java, Keywords
source:
tags: 
type:
up:
  - Java, Modifiers
aliases:
  - access modifier
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

![[Pasted image 20220112114423.png|600]][^1]

[^1]: [source::20220102-1515-BibliotheksklassenUndKlassenentwurf]
