---
context:
- Java, Non-Access Modifiers
aliases:
- java keywords, final
title: Java Keywords, Final
domain:
- ''
---

# Java Keywords, Final

A _final variable_ can be explicitly initialised only once. A reference variable declared final can never be reassigned to refer to an different object. However, the data within the object can be changed. So, the state of the object can be changed but not the reference. With variables, the _final_ modifier often is used with static to make the constant a class variable.[^1]

```java
public class Test {
   final int value = 10;

   // The following are examples of declaring constants:
   public static final int BOXWIDTH = 6;
   static final String TITLE = "Manager";

   public void changeValue() {
      value = 12;   // will give an error
   }
}
```

A _final method_ cannot be overridden by any subclasses. As mentioned previously, the final modifier prevents a method from being modified in a subclass. The main intention of making a method final would be that the content of the method should not be changed by any outsider.[^1]

```java
public class Test {
   public final void changeName() {
      // body of method
   }
}
```

_Final classes_ are mainly used to prevent the class from being subclassed. If a class is marked as final then no class can inherit any feature from the final class.[^1]

[^1]: [source::20220115-1804-JavaNonAccessModifiers]
