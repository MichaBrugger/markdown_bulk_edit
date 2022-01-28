---
context: null
aliases:
- java, interfaces
title: Java, Interfaces
domain:
- ''
---

# Java, Interfaces

Every field declared in an interface is automatically static and final. That means that all objects of that class share the same values for that field.

```java
public interface Animal {  
  int age = 1; // static + final
  String name = "Miezi";

  public void poop();
}

public class Cat implements Animal { // it's always named Miezi and age 1
  @Override
  public void poop(){
    // something
  }
}
```
