---
topic: Greedy
subtopic: Every original boundary is paid once, in its cheaper direction
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Look at the boundary between the original neighbours $i$ and $i+1$. At the end only one ingredient survives, so at some moment the two sides of this boundary must be merged: an ingredient from the left block removes its right neighbour, paying its $R$, or an ingredient from the right block removes its left neighbour, paying its $L$. Each removal settles exactly one original boundary, so there are $N - 1$ payments, one per boundary.

The cheapest payment that can ever be attributed to boundary $i$ is $\min(R_i, L_{i+1})$ when the two original neighbours are still adjacent, and this can be arranged for all boundaries simultaneously by choosing a suitable order of removals. Hence the answer is

$$\sum_{i=1}^{N-1} \min(R_i, L_{i+1}).$$

## Edge cases

- $N = 1$: nothing to remove, cost 0.
- Costs go up to $10^9$ per removal, so the total needs 64 bits.
- $L_1$ and $R_N$ are never used.
- The order of removals is not asked for - only the total.

## Dry run

`L = [2, 1, 3, 2]`, `R = [4, 2, 4, 3]`.

- boundary 1|2: $\min(R_1, L_2) = \min(4, 1) = 1$
- boundary 2|3: $\min(R_2, L_3) = \min(2, 3) = 2$
- boundary 3|4: $\min(R_3, L_4) = \min(4, 2) = 2$

Answer 5.
