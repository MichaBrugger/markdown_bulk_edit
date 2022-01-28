---
context:
- Java, Class
- Java, Inner Class
aliases:
- difference between inner and outer class in java
title: Difference between Inner and Outer Class in Java
domain:
- ''
---

# Difference Between Inner and Outer Class in Java

Unlike a regular class, an inner class can be private or protected.

```java
class OuterClass {
  int x = 10;

  private class InnerClass {
    int y = 5;
  }
}

public class Main {
  public static void main(String[] args) {
    OuterClass myOuter = new OuterClass();
    OuterClass.InnerClass myInner = myOuter.new InnerClass();
    System.out.println(myInner.y + myOuter.x);
  }
}
```
