---
tags: 
type:
up:
  - Java, Structure
context:
aliases:
  - Interfaces
source:
---

# Java, Interfaces

Every field declared in an interface is automatically [[Java Keywords, Static|static]] and [[Java Keywords, Final|final]]. That means that all [[Java, Object|objects]] of that [[Java, Class|class]] share the same values for that field.

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
