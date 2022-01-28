---
tags: ['Java']
type:
up: ['Java, Variable']
context:
source: []
aliases:
  - declaring a field
---

# Java, Field Declaration

A [[Java, Non-Static Field|non-static]] or [[Java, Static Field|static field]] is generally declared using the following syntax:[^1]

```java
// The square brackets [ ] around some of the keywords mean that this option is optional. Only type and name are required.

[access_modifier] [static] [final] type name [= initial value] ;
```

- First, an [[Java, Access Modifiers|access modifier]] can be declared for a Java field. The access modifier determines which object classes that can access the [[Java, Non-Static Field|Java field]].
- Second, a [[Java, Data Types|data type]] for the field must be assigned.
- Third, the field can be declared.

[^1]: [source::20220110-1500-JavaFields]
