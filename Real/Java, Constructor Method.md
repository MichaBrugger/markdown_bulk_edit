---
context:
source: []
tags: 
type:
up:
  - Java, Method
aliases:
  - constructor
  - constructors
---

# Constructor Methods in (Java)

A Java constructor is a special [[Java, Method|method]] that is [[Brain/Java, Calling a Method|called]] when an [[Java, Object|object is instantiated]]. In other words, when you use the [[Java Keywords, New|new keyword]]. The purpose of a Java constructor is to initialise the newly created object (and all the [[Java, Non-Static Field|non-static variables]]) before it is used.

Note that the constructor name **must match the class name**, and it cannot have a [[Java, Return Type|return type]]. All [[Java, Class|classes]] have constructors by default: if you do not create a class constructor yourself, Java creates one for you.[^1]Each object can have one or more constructors (even with the same name, as long as the parameters are different).

A full list of the [[Difference between Constructor and Method in Java|difference between constructors and normal methods]] can be found here.

# Related

- [[Java, Constructor Parameter]]

[^1]: [source::20220102-1450-JavaConstructors]
