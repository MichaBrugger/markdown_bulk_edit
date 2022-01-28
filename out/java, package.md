---
context: null
aliases:
- java, package
title: Java, Package
domain:
- ''
---

# Java, Package

Packages are the Java equivalent of a library.

```java
import java.util.ArrayList; //util = package; ArrayList = library class
public class Notizbuch {

  private ArrayList<String> notizen; // ArrayList<String> = generic class

  public Notizbuch() {
    notizen = new ArrayList<String>(); 
  }

}
```
