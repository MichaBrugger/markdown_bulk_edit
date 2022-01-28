---
tags:
type:
up:
context:
  - UML, Aggregation
  - UML, Composition
aliases:
source: []
---

# Difference Between UML Aggregation and UML Composition

A [[UML, Composition]] is used when:
- attempting to represent real-world whole-part relationships, e.g. an engine is a part of a car
- the container is destroyed, the contents are also destroyed, e.g. a university and its departments

A [[UML, Aggregation]] is used when:
- Car model engine E01 is part of a car model C01, as the engine, E01, maybe also part of a different car model
- When the container is destroyed, the contents are usually not destroyed, e.g. a professor has students; when the professor dies the students do not die along with him

Thus the aggregation relationship is often 'catalogue' containment to distinguish it from composition's 'physical' containment.
