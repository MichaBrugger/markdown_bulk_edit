---
alias: ['A-B testing']
tags: 🚧 
up: ['Java']
type: ['Method']
source: []
---

A/B-Testing is often used to see what impact a specific feature has on the [[User, |user]]. This is often used by [[Corporation, Digital|tech companies]] for [[Product, Digital|digital goods]].[^1]

In the context of [[Digitization, Internal Focus|user focused digitization]] it unfortunately typically doesn't work since we would have to compare full products or services and not specific features.

[^1]: [source::20220102-1802-BusinessInnovationDigitalEconomy]
```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```