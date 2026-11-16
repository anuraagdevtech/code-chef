---
topic: Trees
subtopic: Sort child blocks by an exact cross-product comparator
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Each child subtree forms one contiguous block in any DFS sequence. Suppose blocks $A,B$ contain $(o_A,z_A)$ and $(o_B,z_B)$ ones and zeros. Ordering $A$ before $B$ contributes $o_Az_B$ cross inversions, while reversing them contributes $o_Bz_A$. Sort children by this exact comparison to minimise all cross-block contributions.

In reverse tree order, first optimise every child. Start a node's merged block with its own weight, then append children in the sorted order. Add each child's internal inversions and `ones_already_seen * child_zeros`. This exchange-optimal ordering plus independent subtree optimisation gives the global minimum.

## Edge cases

- A one-valued parent contributes an inversion with every zero descendant.
- Pure-one child blocks should come after blocks containing zeros.
- Cross products avoid division by zero and floating-point ratios.
- Use iterative traversal for deep trees.

## Dry run

For root weight 1 with children of weights 0 and 1, put the zero child first. Its zero still forms one unavoidable inversion with the root, so the answer is 1.
