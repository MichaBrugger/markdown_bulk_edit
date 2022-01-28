---
aliases:
tags:
  - 🎱 
type:
up:
 - Java, Interfaces
context:
source:
  - []
---

# Java, Iterable Interface

The Iterable interface is the root interface for all the [[Java, Collection Framework|Java collection]] classes. The Collection interface extends the Iterable interface and therefore all the subclasses of the Collection interface also implement the Iterable interface.[^1]This means also, that a class that implements the Java `Iterable` interface can have its elements iterated.

It contains only one [[Java, Abstract Method|abstract method]]:

```java
Iterator<T> iterator()
```

It returns the iterator over the elements of type `T`.

[^1]: [source::20220112-0959-CollectionsJava]
