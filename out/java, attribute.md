---
context: null
aliases:
- java, attribute
title: Java, Attribute
domain:
- ''
---

# Java Attributes

In object-oriented programming, the attributes themselves are defined in classes. At the implementation level, attributes are also called instance variables. In this structure, data about the objects are stored with their content - the attribute values. Each object thus represents itself through the totality of its attribute values. This totality of all attribute values is also called the state of an object.

In order to see how to modify or access an attribute in Java check those links.

```java
public class song {
  private int length; // attribute of data type int
  private String title; // etc.
  private String artist;

  public Song (String title, String artist, int length){ // constructor
    this.title = title;
    this.artist = artist;
    this.length = length;
  }
}
```

# Related

- [[Difference between Attribute and Instance Variable in Java
