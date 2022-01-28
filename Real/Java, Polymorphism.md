---
type:
tags:
  - 🚧 
up:
  - Java, Terminology
context:
  - Java, Inheritance
aliases:
source:
  - []
---

# Java, Polymorphism

[[Java, Inheritance|Inheritance]] is a powerful feature in Java. Inheritance lets one [[Java, Class|class]] acquire the properties and attributes of another class. Polymorphism in java allows us to use these inherited properties to perform different tasks. Thus, allowing us to achieve the same action in many different ways.[^1]

Languages that do not support polymorphism cannot be referred to as [[Object Oriented Programming|Object Oriented Programming]]. But instead, they are known as Object Based Languages.

```java
// Die Signatur dieser Methode ist identisch mit der Methode toString aus der Superklasse Angebot. Daher überschreibt (Polymorphie) die Methode aus der Superklasse. Die ursprüngliche Methode aus der Klasse Angebot wird jedoch genutzt um diese zu erweitern. Der Aufruf der ursprünglichen Methode erfolgt durch super.toString(). An die Rückgabe werden die fehlenden Attribute angehängt

public String toString(){
  return super.toString()+ " Hersteller: " + hersteller + " Gewicht: " + gewicht;
  }
}
```

[^1]: [source::20220112-1457-JavaAufDeutsch]
