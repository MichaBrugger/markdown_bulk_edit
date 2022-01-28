---
context: null
author:
- Knuth, Donald
- Morris, James H.
- Pratt, Vaughan
aliases:
- algorithm, knuth-morris-pratt
title: Algorithm, Knuth-Morris-Pratt
domain:
- ''
---

# Algorithm, Knuth-Morris-Pratt

In computer science, the Knuth–Morris–Pratt string-searching algorithm searches for occurrences of a “word” W within a main “text string” S by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.[^1]

Worst-case performance: $\theta(m) preprocessing + \theta(n) matching$
Worst-case space complexity: $\theta(m)$
## Notes

Heard about it in Lex Fridmans podcast he held with Donald Knuth.

[^1]: [source::20220104-0727-KnuthMorrisPrattAlgorithm]
