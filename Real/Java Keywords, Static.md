---
tags:
type:
up:
  - Java, Keywords
context:
  - Java, Non-Access Modifiers
aliases:
  - static
source: []
---

# Java Keywords, Static

[[Java, Static Field|Static fields]] exist independently of any instances created for the class. Only one copy of the static variable exists regardless of the number of instances of the class. [[Java, Static Method|Static methods]] exist independently of any instances created for the class. Both can be accessed using the class name followed by a dot and the name of the variable or method.[^1]

```java
public class InstanceCounter {
   private static int numInstances = 0;

   protected static int getCount() {
      return numInstances;
   }

   private static void addInstance() {
      numInstances++;
   }

   InstanceCounter() {
      InstanceCounter.addInstance();
   }

   public static void main(String[] arguments) {
      System.out.println("Starting with " + InstanceCounter.getCount() + 
        "instances");

      for (int i = 0; i < 500; ++i) {
         new InstanceCounter();
      }
      System.out.println("Created " + InstanceCounter.getCount() + " instances");
   }
}

// Output:
// Started with 0 instances
// Created 500 instances
```

[^1]: [source::20220115-1804-JavaNonAccessModifiers]
