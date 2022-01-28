---
context: null
aliases:
- java, constructor method
title: Java, Constructor Method
domain:
- ''
---

# Constructor Methods in (Java)

A Java constructor is a special method that is called when an object is instantiated. In other words, when you use the new keyword. The purpose of a Java constructor is to initialise the newly created object (and all the non-static variables) before it is used.

Note that the constructor name **must match the class name**, and it cannot have a return type. All classes have constructors by default: if you do not create a class constructor yourself, Java creates one for you.[^1]Each object can have one or more constructors (even with the same name, as long as the parameters are different).

A full list of the difference between constructors and normal methods can be found here.

# Related

- [[Java, Constructor Parameter

[^1]: [source::20220102-1450-JavaConstructors]
