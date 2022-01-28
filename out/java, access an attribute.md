---
context: null
aliases:
- java, access an attribute
title: Java, Access an Attribute
domain:
- ''
---

# Java, Access an Attribute

To access an attribute we need to create an object of the class. We can the access the attribute using the (.) dot syntax on the object. The methods that do this are commonly called getter methods.

```java
public class Test {

  public int length = 10; // this is the class attribute

  public static void main(String[] args){
    Test test = new Test();
    test.length = 20; // value of attribute is changed from 10 to 20
  }
}
```
