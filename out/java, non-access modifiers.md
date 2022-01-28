---
context: null
aliases:
- java, non-access modifiers
title: Java, Non-Access Modifiers
domain:
- ''
---

# Java, Non-Access Modifiers

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.context && page.context.values != null && page.context.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```

There is also _synchronised_ and _volatile_ modifiers, which are used for threads.[^1]

[^1]: [source::20220115-1804-JavaNonAccessModifiers]
