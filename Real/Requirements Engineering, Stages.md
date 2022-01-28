---
tags: 
type:
up:
  - Requirements Engineering
context:
source: []
aliases:
---

# Requirements Engineering, Stages

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
})

dv.list(pages.file.link)
```

## Notes

This seems to be more or less identical with the [[Software Development, Life Cycle|software development life cycle]]. #♻️
