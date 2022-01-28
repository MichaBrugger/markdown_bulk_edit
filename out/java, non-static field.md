---
context: null
aliases:
- java, non-static field
title: Java, Non-Static Field
domain:
- ''
---

# Non-Static Fields in Java

A non-static field is a variable that belongs to an object. Objects keep their internal state in non-static fields. Non-static fields are also called `instance variables`, because they belong to instances (objects) of a class.[^1]

A Java field is a variable inside a class and is used to store attributes.

```java
public class Employee {
  String  name     ;
  String  position ;
  int     salary   ;
  Date    hiredDate;
}
```

# Related

- [[Java, Declaring a Field
- [[Difference between Attribute and Instance Variable in Java

[^1]: [source::20220102-0655-JavaVariables]
