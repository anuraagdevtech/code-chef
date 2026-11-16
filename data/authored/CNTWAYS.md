---
topic: Combinatorics
subtopic: Lattice paths split at the unique step that passes below the cut-out corner
time: $O(\max(N + M) + \sum N)$
space: $O(\max(N + M))$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The turtle walks from the top-left to the bottom-right corner of an $N \times M$ rectangle from which an $A \times B$ rectangle has been cut out of the top-right corner. It may walk along the boundary of the cut but not through its interior.

Every valid path goes down from height $B - 1$ to height $B$ exactly once, and it must do so at a horizontal position $x \le N - A$, i.e. to the left of the cut (or along its left edge). Classifying paths by that position $x$ counts each path once:

$$\text{answer} = \sum_{x=0}^{N-A} \binom{x + B - 1}{x} \cdot \binom{(N - x) + (M - B)}{N - x}.$$

The first factor counts the ways to reach $(x, B-1)$, the second the ways to finish from $(x, B)$, where nothing is in the way any more. Binomials come from factorial tables.

## Edge cases

- Walking along the edge of the cut is allowed, which is why $x = N - A$ is included.
- The sum of $N$ over the test cases bounds the total work of the loops.
- Factorials are needed up to $N + M$.
- All arithmetic is modulo $10^9 + 7$.

## Dry run

`N = 2, M = 2, A = 1, B = 1`. The sum runs over $x = 0, 1$:

- $x = 0$: $\binom{0}{0} \cdot \binom{2 + 1}{2} = 3$
- $x = 1$: $\binom{1}{1} \cdot \binom{1 + 1}{1} = 2$

Answer 5 - the 6 unrestricted paths minus the one that runs through the removed corner.
