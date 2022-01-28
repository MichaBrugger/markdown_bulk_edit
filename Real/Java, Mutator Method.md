---
context:
source: []
tags: 
type:
up:
  - Java, Method
aliases:
  - setter
---

# Mutator Method

Methods that are used to mutate or change the value of an [[Java, Non-Static Field|instance variable]] are called setter methods.[^1] Setter methods change the values of one or more data fields through assignment.

```java
public void geldEinwerfen(int betrag) {
  bisherGezahlt = bisherGezahlt + betrag; // bisherGezahlt is mutated
}
```
