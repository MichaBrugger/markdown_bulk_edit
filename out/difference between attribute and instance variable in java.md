---
context:
- Java, Attribute
- Java, Non-Static Field
aliases:
- difference between attribute and instance variable in java
title: Difference between Attribute and Instance Variable in Java
domain:
- ''
---

# Difference Between Attribute and Instance Variable in Java

An instance variable is a very specific thing. It is a variable, declared in a class. When you create an instance of a class, you create an object. Those values belong to that particular object, another object of the same class will have its own set of values. Note that `object` and `instance of a class` can be used interchangeably.

An attribute is a non-specific thing used to describe a concept. An object, an instance of a class, can be said to have methods and attributes. The attributes reflect the state of the object, and the methods manipulate that state. Attributes could be those variables themselves, however, public variables are considered bad form. For this reason, methods are offered to expose private values safely. These methods that directly access object variables, getters and setters in Java, can be though of as attributes of the object.
