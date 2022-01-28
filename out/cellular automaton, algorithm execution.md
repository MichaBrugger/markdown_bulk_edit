---
context:
- Algorithm
aliases:
- cellular automaton, algorithm execution
title: Cellular Automaton, Algorithm Execution
domain:
- ''
---

# How Does a Computer Execute a [[Cellular Automaton?

The algorithm starts iterating over every single tile to determine what it should be. It does it not in parallel but successively. Due to it's successive nature, it's crucially important that the calculated value (e.g. black or white) is stored in a separate grid and not written into the original one, else the whole algorithm doesn't work.