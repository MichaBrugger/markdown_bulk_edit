---
up:
  - Business Strategy
context:
source: []
tags: 
type:
aliases:
---

# Blue Ocean Strategy

The Blue Ocean Strategy is about [[Market, New|creating]] and capturing [[Market, Uncontested|uncontested]] market space and thereby making [[Competition|competition]] irrelevant. It is based on the view, that market boundaries and industry structure are not a given and can be reconstructed by the players. Companies pursue both [[Differentiation]] and [[Cost Leadership]] to open up new markets (instead of playing in highly competitive [[Red Ocean|red oceans]]) and create new demand (this [[Difference between Blue Ocean Strategy and Stuck in the Middle|doesn't really align with Porter's Stuck in the Middle concept]]).

The logic behind the creation of a blue ocean is somewhat counter-intuitive, since it's neither about technology innovation, nor about creating complete new markets or industries from scratch. The core strategy evolves around [[Value, Creation|increasing the value]] for the customer, [[Cost, Reduction|reducing cost]] and not being 'comparable' to the competition.[^1]

```dataviewjs
const file = dv.current().file.name
const pages = dv.pages().where(page => {
  if (page.up && page.up.values != null && page.up.values.includes(file)) {
    return page
  }
}).sort(k => k.file.name, 'asc')

dv.list(pages.file.link)
```

[^1]: [source::20220110-0811-BlueOceanStrategy]
