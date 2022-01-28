---
context:
- Java, Inheritance
- Java Keywords, Abstract
aliases:
- java, abstract method
title: Java, Abstract Method
domain:
- ''
---

# Java, Abstract Method

When creating an abstract method, we don't specify a body for it, all we have to do is declare it.[^1] However, as soon as one method within a class is abstract, the whole class is abstract.[^2]

```java
public abstract class Animal {
  int age;
  String name;

  public abstract void makeNoise(); //no curly braces needed

  // we can still have non-abstract methods that child classes can access
  // but they don't need to implement it themselves

  public void printName() {
    System.out.println("My name is: " + this.name); 
  }
}
```

Having defined an abstract method, we now need to implement the abstract method in every child of that class.

```java
public class Cat extends Animal{ // child class of Animal
  public cat(String name, int age){
    this.name = name;
    this.age = age;
  }

  @Override
  public void makeNoise(){
    // something
  }
}
```

If we were to instantiate a cat object in our main method and let it make noise, it would look like this:
```java
public class Main {
  public static void main(String[] args) {
    Cat myCat = new Cat("Miezi", 12);
    myCat.makeNoise();
  }
}
```

[^1]: [source::20220115-1655-AbstractClassesMethodsJava]
[^2]: [source::20220112-1457-JavaAufDeutsch]
