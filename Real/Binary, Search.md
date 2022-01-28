---
context:
source: []
tags: 
type:
up:
  - Algorithm, Search
aliases:
  - binary search
---

# Binary, Search

[[Binary]] search is an algorithm that searches in a [[Collection, Sorted|sorted collection]] for a target. It works by comparing the target to the middle element in a collection. If the target is greater than the middle element, the left elements are discarded. If the target is less than the middle element, the right elements are discarded. This [[Recursion|process is repeated]] until the middle element is equal to the target, and if no further splitting can be done. The target does not exist in the list.[^1]

[^1]: [source::20220109-0604-DivideConquerBinarySearch]
