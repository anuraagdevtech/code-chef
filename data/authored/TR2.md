---
topic: Trees
subtopic: Merge root-path tries and count supporting maps
time: $O(\sum N_i+M)$ per test case
space: $O(\sum N_i+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Each root-to-node path is a control string over `L` and `R`. Merge all maps into a common binary trie, counting how many maps contain each trie node. A map contains each root path at most once, so visiting its vertices increments exactly those support counts.

For every trie node of depth $d$ and count $c$, update the longest string supported by exactly that node count. A suffix maximum over counts then converts this to the longest string supported by at least $k$ maps for every $k$.

## Edge cases

- The capital is vertex one in every map.
- Input edges need not be in parent-first order; traverse after reading the map.
- An empty control string is always valid and has length zero.

## Dry run

In sample one, path `RL` exists in the first two maps, while only one-step paths are common to all three. The answers are `2 2 1`.
