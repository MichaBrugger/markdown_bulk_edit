---
type:
tags: 
up:
context:
  - Java, Class
  - Java, Inner Class
aliases:
source: []
---

# Difference Between Inner and Outer Class in Java

Unlike a regular class, an inner class can be [[Java Keywords, Private|private]] or [[Java Keywords, Protected|protected]].

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
