---
context: null
aliases:
- java, mutator method
title: Java, Mutator Method
domain:
- ''
---

# Mutator Method

Methods that are used to mutate or change the value of an instance variable are called setter methods.[^1] Setter methods change the values of one or more data fields through assignment.

```java
public void geldEinwerfen(int betrag) {
  bisherGezahlt = bisherGezahlt + betrag; // bisherGezahlt is mutated
}
```
