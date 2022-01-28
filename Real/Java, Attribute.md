---
context:
type:
tags: Java 
up: ['Java, Object']
aliases:
  - attribute
  - Java attribute
source: []
---

# Java Attributes

In object-oriented programming, the attributes themselves are defined in classes. At the implementation level, attributes are also called [[Java, Non-Static Field|instance variables]]. In this structure, data about the objects are stored with their content - the attribute values. Each [[Java, Object|object]] thus represents itself through the totality of its attribute values. This totality of all attribute values is also called the [[Java, State|state]] of an object.

In order to see how to [[Java, Modify an Attribute|modify]] or [[Java, Access an Attribute|access an attribute in Java]] check those links.

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

- [[Difference between Attribute and Instance Variable in Java]]
