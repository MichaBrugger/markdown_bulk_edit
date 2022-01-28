---
context:
source: []
tags: 
type:
up:
  - Java, Variable
aliases:
  - instance variable
  - Datenfeld
---

# Non-Static Fields in Java

A non-static field is a variable that belongs to an [[Java, Object Class|object]]. Objects keep their internal [[Java, State|state]] in non-static fields. Non-static fields are also called `instance variables`, because they belong to instances (objects) of a [[Java, Class|class]].[^1]

A Java field is a [[Java, Variable|variable]] inside a [[Java, Class|class]] and is used to store [[Java, Attribute|attributes]].

```java
public class Employee {
  String  name     ;
  String  position ;
  int     salary   ;
  Date    hiredDate;
}
```

# Related

- [[Java, Declaring a Field]]
- [[Difference between Attribute and Instance Variable in Java]]

[^1]: [source::20220102-0655-JavaVariables]
