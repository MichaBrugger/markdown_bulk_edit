---
context: null
aliases:
- the portfolio of actions
title: The Portfolio of Actions
domain:
- ''
---

# The Portfolio of Actions

Three types of moves are especially relevant to implementing strategy under conditions of uncertainty: big bets, options, and no-regrets moves.[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

[^1]: [source::20220110-0937-StrategyUncertainty]
