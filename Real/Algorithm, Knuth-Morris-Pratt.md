---
tags: 
type:
up:
  - Algorithm, Search
context:
author:
  - Knuth, Donald
  - Morris, James H.
  - Pratt, Vaughan
source: []
aliases:
  - KPM algorithm
---

# Algorithm, Knuth-Morris-Pratt

In [[computer science|computer science]], the Knuth–Morris–Pratt [[Algorithm, String Search|string-searching algorithm]] searches for occurrences of a “word” W within a main “text string” S by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.[^1]

Worst-case [[Time Complexity|performance]]: $\theta(m) preprocessing + \theta(n) matching$
Worst-case [[Space Complexity|space complexity]]: $\theta(m)$
## Notes

Heard about it in [[20220104-0729-ProgrammingAlgorithmsHardProblems|Lex Fridmans podcast he held with Donald Knuth]].

[^1]: [source::20220104-0727-KnuthMorrisPrattAlgorithm]
