---
source: []
tags: ['Java']
type:
up: ['Java, Attribute']
context:
aliases:
---

# Java, Modify an Attribute

In order to modify an [[Java, Attribute|attribute]] in Java, we can simply override it. Methods that do that are commonly referred to as [[Java, Mutator Method|setter methods]].

```java
public class Test {

  public int length = 10; // this is the class attribute

  public static void main(String[] args){
    Test test = new Test();
    test.length = 20; // value of attribute is changed from 10 to 20
  }
}
```