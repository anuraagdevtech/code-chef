---
topic: Basic Math
subtopic: Count each grid adjacency exactly once
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For every pair of neighbouring cells, exactly one is coloured later. Their adjacency contributes one point precisely when that later cell is coloured. Thus every grid edge contributes exactly once, regardless of the order.

There are $N(M-1)$ horizontal edges and $M(N-1)$ vertical edges. Their sum is the score for every play order and therefore also the maximum.

## Edge cases

- A one-cell board scores zero.
- Diagonal neighbours do not count.
- No search over colouring orders is necessary.

## Dry run

A two-by-two grid has two horizontal and two vertical adjacencies, so its score is four.
