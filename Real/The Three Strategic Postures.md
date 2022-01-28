---
tags:
type:
up:
  - Strategy
context:
  - Uncertainty
aliases:
source: []
---

# The Three Strategic Postures

A posture is not a complete strategy. It clarifies [[Strategy, Intent|strategic intent]] but not the actions required to fulfil that intent. Three types of moves are especially relevant to implementing strategy under conditions of [[Uncertainty|uncertainty]]: big bets, options, and no-regrets moves. These are also called [[The Portfolio of Actions]].[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

![[Pasted image 20220116185525.png]][^1]

[^1]: [source::20220110-0937-StrategyUncertainty]
