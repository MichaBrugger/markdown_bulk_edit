---
context:
- Java, Inheritance
aliases:
- java, abstract class
title: Java, Abstract Class
domain:
- ''
---

# Java, Abstract Class

An abstract class in java is a class that can't be instantiated. Its purpose is to serve as a superclass for other classes.[^1]

An example for the use-case of an abstract class would be the creation of an animal class. While it makes sense to extend the animal class with, for example, a cat subclass, it would never make sense to make actual instance of the animal class.[^2]

```java
public abstract class Animal{
  int age; // class attributes, shared among subclasses
  String name;

  public animal(){ // technically doesn't need constructor
    // something
  }
}

public class Cat extends Animal{
  
  public cat(String name, int age){
    this.name = name;
    this.age = age;
  }  
}
```

[^1]: [source::20220112-1457-JavaAufDeutsch]
[^2]: [source::20220115-1655-AbstractClassesMethodsJava]