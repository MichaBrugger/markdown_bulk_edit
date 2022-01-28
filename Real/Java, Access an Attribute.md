---
tags: Java
source: []
type:
up: ['Java, Attribute']
context:
aliases:
---

# Java, Access an Attribute

To access an [[Java, Attribute|attribute]] we need to create an [[Java, Object|object]] of the class. We can the access the attribute using the (.) dot syntax on the object. The methods that do this are commonly called [[Java, Accessor Method|getter methods]].

```java
public class Test {

  public int length = 10; // this is the class attribute

  public static void main(String[] args){
    Test test = new Test();
    test.length = 20; // value of attribute is changed from 10 to 20
  }
}
```
