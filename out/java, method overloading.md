---
context:
- Java, Polymorphism
- Java, Overloading
aliases:
- java, method overloading
title: Java, Method Overloading
domain:
- ''
---

# Java, Method Overloading

Method overloading is defined as a process that can create multiple methods of the same name in the same class, and all the methods work in different ways. Method overloading occurs when there is more than one method of the same name in the class.[^1]

```java
class Shapes {
  public void area() {
    System.out.println("Find area ");
  }
public void area(int r) {
    System.out.println("Circle area = "+3.14*r*r);
  }
 
public void area(double b, double h) {
    System.out.println("Triangle area="+0.5*b*h);
  }
public void area(int l, int b) {
    System.out.println("Rectangle area="+l*b);
  }
 
 
}
 
class Main {
  public static void main(String[] args) {
    Shapes myShape = new Shapes();  // Create a Shapes object
     
    myShape.area();
    myShape.area(5);
    myShape.area(6.0,1.2);
    myShape.area(6,2);
     
  }
}

// Output
// Find area  
// Circle area = 78.5  
// Triangle area=3.60  
// Rectangle area=12
```

[^1]: [source::20220112-1520-PolymorphismJavaIntroduction]
