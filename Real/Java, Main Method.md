---
type:
tags:
up:
  - Java, Method
context:
aliases:
  - main method
source: []
---

# Java, Main Method

Every Java application _needs_ to have a main [[Java, Method|method]] with the following [[Java, Signature|signature]]:
```java
public class Main {
  public static void main(String[] args) {
    //something
  }
}
```

The main method is:
- [[Java Keywords, Public|public]] because it's accessed from outside the class.
- [[Java Keywords, Static|static]] because she's called without being instantiated first
- [[Java Keywords, Void|void]] because it doesn't have a [[Java, Return Type|return type]]
- it takes an array of strings as [[Java, Parameter|parameters]]