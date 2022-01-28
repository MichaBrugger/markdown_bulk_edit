---
context: null
aliases:
- java, class loader
title: Java, Class Loader
domain:
- ''
---

# Class Loader in Java

A Java program typically consists of several pieces called classes. Each class may have a separate author and each is compiled (translated into byte-code) separately. A class loader (called a linker in other programming languages) automatically connects the classes together. Java classes in the standard Java library are accessed using the Java Applications Programming Interface, commonly referred to as the Java API.[^1]

A source code file contains one or more Java classes. But if there is more than one, only one may be public.[^2]

[^1]: [source::20220102-0522-JavaFundamentals]
