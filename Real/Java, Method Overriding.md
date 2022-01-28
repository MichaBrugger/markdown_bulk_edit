---
type:
tags: 
up:
  - Java, Method
context:
  - Java, Overriding
  - Java, Polymorphism
aliases:
  - method overriding
source:
  - []
---

# Java, Method Overriding

Method overriding is defined as a process when the [[Java, Subclass|subclass]] has the same method as declared in the parent class.[^1]

```java
class Vehicle{  
  //defining a method  
  void run(){System.out.println("Vehicle is moving");}  
}  
//Creating a child class  
class Car2 extends Vehicle{  
  //defining the same method as in the parent class  
  void run(){System.out.println("car is running safely");}  
  
  public static void main(String args[]){  
  Car2 obj = new Car2();//creating object  
  obj.run();//calling method  
  }  
}
// Output
// Car is running safely
```

[^1]: [source::20220112-1520-PolymorphismJavaIntroduction]
