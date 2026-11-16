---
topic: Trees
subtopic: Repeatedly move the larger heap label to its parent
time: $O(\log\max(i,j))$ per query
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The parent of a heap-labelled vertex $v$ is $\lfloor v/2\rfloor$. While the labels differ, move the larger label to its parent and count one edge. The larger label cannot be a strict ancestor of the smaller one, so this move stays on the path toward their lowest common ancestor. When the labels meet, all required upward edges from both endpoints have been counted.

## Edge cases

- Equal endpoints have distance zero.
- Root label one has no parent to traverse.
- The leading count is the number of queries.

## Dry run

For labels 4 and 3, move `4->2`, `3->1`, and `2->1`. They meet after three edges.
