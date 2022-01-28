---
source:
tags: 
type:
up:
  - Java, Terminology
context:
aliases:
---

# Java, Overloading

A [[Java, Class|Java class]] can have more than one [[Java, Constructor|constructor]] or contain more than one [[Java, Method|method]] with the same name, as long as both of them define a clearly distinguishable set of [[Java, Parameter|parameters]].[^1]

Overloading is used [[Java, Method Overloading|to perform polymorphism]] in Java.

```java
public class Test{

  Object.method(parameter); // external
  method(parameter) // internal
} 


```


[^1]: [source::20220102-1511-Objektinteraktion]
