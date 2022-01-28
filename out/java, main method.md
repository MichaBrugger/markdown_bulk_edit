---
context: null
aliases:
- java, main method
title: Java, Main Method
domain:
- ''
---

# Java, Main Method

Every Java application _needs_ to have a main method with the following signature:
```java
public class Main {
  public static void main(String[] args) {
    //something
  }
}
```

The main method is:
- public because it's accessed from outside the class.
- static because she's called without being instantiated first
- void because it doesn't have a return type
- it takes an array of strings as parameters