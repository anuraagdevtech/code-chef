---
topic: Prefix Sums
subtopic: Expand the cube of a prefix difference and keep three running power sums
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
With prefix sums $P_0 = 0, P_1, \dots, P_N$, a subarray sum is $P_j - P_i$ for $i < j$, and

$$(P_j - P_i)^3 = P_j^3 - 3 P_j^2 P_i + 3 P_j P_i^2 - P_i^3.$$

Fix $j$ and sum over the $j$ earlier prefixes $i = 0 \dots j - 1$:

$$j \cdot P_j^3 - 3 P_j^2 \, S_1 + 3 P_j \, S_2 - S_3,$$

where $S_1, S_2, S_3$ are the sums of the first, second and third powers of the earlier prefix sums. So one pass suffices: compute the new prefix, add the expression to the answer, then add the powers of the new prefix to the three running sums. $P_0 = 0$ contributes nothing to the sums but is counted in the factor $j$.

## Edge cases

- Everything is reduced modulo $998244353$, including the prefix sums themselves.
- The factor in front of $P_j^3$ is $j$, the number of earlier prefixes including $P_0$.
- Negative intermediate values are fixed by the final reduction.
- A single element gives its cube.

## Dry run

`A = [1, 1]`, prefixes $P_1 = 1$, $P_2 = 2$.

- $j = 1$: $1 \cdot 1 - 0 + 0 - 0 = 1$. Sums become $S_1 = S_2 = S_3 = 1$.
- $j = 2$: $2 \cdot 8 - 3 \cdot 4 \cdot 1 + 3 \cdot 2 \cdot 1 - 1 = 9$.

Total 10 = $1^3 + 1^3 + 2^3$.
