---
context:
- Java, Constructor Method
- Java, Method
aliases:
- difference between constructor and method in java
title: Difference between Constructor and Method in Java
domain:
- ''
---

# Difference Between Constructor and Method in Java

Even though the Java constructor is technically speaking just a special method, there are key differences: [^1]

| Constructors                                                                       | Methods                                                                                 |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Is a block of code that initialises a newly created object                         | Is a collection of statements which returns a value upon execution |
| Can be used to initialise an object                                                | Consists of Java code to be executed                                                    |
| Invoked implicitly by the system                                                | Is invoked by the programmer                                                            |
| Invoked when an object is created using the new keyword | Is invoked through method calls                             |
| Doesn’t have a return type                                  | Must have a return type                                                                 |
| Initialises a object that doesn’t exist                                            | Does operations on an already created object                                            |
| Name must be same as the name of the class                                         | Name can be anything                                                                    |
| A class can have many Constructors but must not have the same parameters           | A class can have many methods but must not have the same parameters                     |
| Cannot be inherited by subclasses                                                  | Can be inherited by subclasses                                      |

[^1]: [source::20220110-1436-DifferenceConstructorsMethods]
