---
tags:
  - 🌱 
  - 🚧 
up:
context:
  - Java, Attribute
  - Java, Non-Static Field
source: []
type:
aliases:
---

# Difference Between Attribute and Instance Variable in Java

An [[Java, Non-Static Field|instance variable]] is a very specific thing. It is a [[Java, Non-Static Field|variable]], declared in a [[Java, Class|class]]. When you create an instance of a class, you create an [[Java, Object|object]]. Those values belong to that particular object, another object of the same class will have its own set of values. Note that `object` and `instance of a class` can be used interchangeably.

An attribute is a non-specific thing used to describe a [[Concept|concept]]. An object, an instance of a class, can be said to have [[Java, Method|methods]] and [[Java, Attribute|attributes]]. The attributes reflect the [[Java, State|state]] of the object, and the methods manipulate that state. Attributes could be those variables themselves, however, [[Java, Public Variables|public variables]] are considered bad form. For this reason, methods are offered to expose private values safely. These methods that directly access object variables, [[Java, Accessor Method|getters]] and [[Java, Mutator Method|setters]] in Java, can be though of as attributes of the object.
