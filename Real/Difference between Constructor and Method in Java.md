---
tags: Java
up:
context:
  - Java, Constructor Method
  - Java, Method
source: []
type: ['Connect']
aliases:
---

# Difference Between Constructor and Method in Java

Even though the [[Java, Constructor Method|Java constructor]] is technically speaking just a special [[Java, Method|method]], there are key differences: [^1]

| Constructors                                                                       | Methods                                                                                 |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Is a block of code that initialises a newly created object                         | Is a collection of [[Java, Statement\|statements]] which returns a value upon execution |
| Can be used to initialise an object                                                | Consists of Java code to be executed                                                    |
| Invoked implicitly by the system                                                | Is invoked by the programmer                                                            |
| Invoked when an object is created using the [[Java Keywords, New\|new]] keyword | Is invoked through [[Brain/Java, Calling a Method\|method calls]]                             |
| Doesn’t have a [[Java, Return Type\|return type]]                                  | Must have a return type                                                                 |
| Initialises a object that doesn’t exist                                            | Does operations on an already created object                                            |
| Name must be same as the name of the class                                         | [[Java, Naming Conventions\|Name]] can be anything                                                                    |
| A class can have many Constructors but must not have the same parameters           | A class can have many methods but must not have the same parameters                     |
| Cannot be inherited by [[Java, Subclass\|subclasses]]                                                  | Can be inherited by [[Java, Subclass\|subclasses]]                                      |

[^1]: [source::20220110-1436-DifferenceConstructorsMethods]
