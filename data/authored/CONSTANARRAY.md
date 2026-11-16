---
topic: Constructive
subtopic: Blocks of M distinct values keep all frequencies within one of each other
time: $O(N + M)$ expected per test case
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The condition says that after every prefix, $A_i$ must be one of the most frequent values of $B_1 \dots B_i$.

Build $B$ in consecutive blocks of $M$ positions, each block being a permutation of $1 \dots M$. Then after any prefix every value has occurred either $q$ or $q + 1$ times, where $q$ is the number of completed blocks, and the values with $q + 1$ occurrences are exactly those already placed in the current block.

So at position $i$ it is enough to make sure that $A_i$ has been placed in the current block: if $A_i$ is still unused in this block, place it now; otherwise it was placed earlier in the block and any unused value can go here. Either way $A_i$ has frequency $q + 1$, the maximum.

Two sets track which values are still available in the current block; when the block is full they are reset.

## Edge cases

- $M = 1$: the array is all ones.
- The last block may be incomplete, which is fine.
- When $A_i$ was already used in the block, the filler value is arbitrary.
- Many arrays are valid, so the output is validated by a checker.

## Dry run

`N = 3, M = 2, A = [1, 1, 1]`.

- position 1: 1 is unused in the block - place 1.
- position 2: 1 is already used - place the other value, 2. The block `1 2` is complete; both values have frequency 1.
- position 3: new block, place 1. Frequencies: 1 twice, 2 once.

Output `1 2 1`.
