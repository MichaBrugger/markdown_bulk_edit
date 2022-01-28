---
tags:
  - 🚧 
type:
up:
  - Java, Interfaces
context:
aliases:
  - Java serialization
source:
---

# Java, Serializable Interface

Serialization is the conversion of the [[Java, State|state]] of an [[Java, Object|object]] into a byte stream; deserialization does the opposite. Classes that are eligible for serialization need to implement a special marker interface, Serializable.[^1]

Important: [[Java Keywords, Static]] fields belong to a class (and not the object), so they are not going to be serialized.

![[Pasted image 20220112153855.png]][^2]
![[Pasted image 20220112153912.png]]

[^1]: [source::20220112-1434-IntroductionJavaSerialization]
[^2]: [source::20220102-1521-Vererbung]
