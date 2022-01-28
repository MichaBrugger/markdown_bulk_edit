---
context:
- Binary, Search
- Paradigm, Divide-and-Conquer
aliases:
- connection between binary search and divide-and-conquer
title: Connection between Binary Search and Divide-and-Conquer
domain:
- ''
---

# Connection Between Binary Search and Divide-and-Conquer

Divide and conquer is an approach of breaking down a problem into sub problems and combining the solutions. In binary search, on a sorted array of numbers, we divide (decrease) the array of numbers(search space), conquer the sub problems by recursively looking at the middle point for our target and splitting until we find our target, the base case condition. Note, binary search works on a sorted collection of elements. This means it’s performance is good when the lost is sorted and terrible otherwise. [^1]

[^1]: [source::20220109-0604-DivideConquerBinarySearch]
