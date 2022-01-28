---
tags:
type:
up:
context:
  - Java, Interfaces
  - Java, Abstract Class
aliases:
source: []
---

# Difference Between Interface and Abstract Class in Java

Both [[Java, Abstract Class|abstract classes]] and [[Java, Interfaces|interfaces]] 'force' the classes that either [[Java, Inheritance|extend]] or implement it, to implement the methods defined in them. Unlike in an abstract class, we don't need the [[Java Keywords, Abstract|abstract]] keyword for interfaces, because every [[Java, Abstract Method|method]] in an interface is assumed to be abstract.

The key differences are however, that a [[Java, Class|class]] _can implement as many interfaces as they want_, but can only extend one class (one can also do both at the same time). Another key difference is, that _any fields declared in an interface are [[Java Keywords, Static|static]] and [[Java Keywords, Final|final]]_.[^1]

---
Create an interface when you have a lot of unrelated classes that should all be able to do a certain thing, even though they might be very different besides that.

Abstract classes should be used, when you have a lot of closely related class that have the same functionality and the same types of fields.

[^1]: [source::20220115-1655-AbstractClassesMethodsJava]
