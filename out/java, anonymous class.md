---
context: null
aliases:
- java, anonymous class
title: Java, Anonymous Class
domain:
- ''
---

# Java, Anonymous Class

An anonymous inner class is a class with no name that is used to instantiate only _one single object_.
There are two way to create an anonymous class.

The first is to create a subclass:
```java
public class AnonymousInnerClass {
  public static void main(String[] args) {

    Animal myAnimal = new Animal(); // normal way
    myAnimal.makeNoise();

    Animal bigfoot = new Animal() { // creating an anonymous subclass of Animal
      public void makeNoise() { // overriding normal method
        System.out.println("Bigfoot noise!")
      } 
    }
    bigfoot.makeNoise();
  }
}

public class Animal {
  public void makeNoise() {
    System.out.println("Noise");
  }
}

// Output:
// Noise
// Bigfoot noise
```

The second is to implement an interface:
```java
public class AnonymousInnerClass {
  public static void main(String[] args) {

    Animal myAnimal = new Animal(); // normal way
    myAnimal.makeNoise();

    // bigfoots type is the anonymous subclass, not Animal
    Animal bigfoot = new Animal() { // creating an anonymous subclass of Animal       
        @Override
        public void makeNoise() { // overriding normal method
        System.out.println("Bigfoot noise!")
      } 
    };
    bigfoot.makeNoise();

    Runnable myAnonymousRunnable = new Runnable() {
  
      @Override
      public void run() {
        System.out.println("I'm an anonymous runnable.")
      }
    };
    myAnonymousRunnable.run();
  }
}

public class Animal {
  public void makeNoise() {
    System.out.println("Noise");
  }
}

// Output:
// Noise
// Bigfoot noise
// I'm an anonymous runnable.
```

This is a great way to implement multi-threading.[^1]

[^1]: [source::20220115-1858-JavaAnonymousInnerClasses]
