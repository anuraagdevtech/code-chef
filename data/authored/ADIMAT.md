---
topic: Combinatorics
subtopic: Burnside over row cycle types with a cycle-index DP for the columns
time: $O(p(n) \cdot m^2)$, $n = \min(N, M)$, $m = \max(N, M)$ and $p$ the partition function
space: $O(n + m)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Matrices are identified under the group $S_N \times S_M$ of row and column permutations, so by Burnside's lemma the answer is the average number of matrices fixed by a pair (row permutation, column permutation).

A pair fixes a matrix when the matrix is constant on every orbit of cells. A row cycle of length $a$ and a column cycle of length $b$ together split their $a \cdot b$ cells into $\gcd(a, b)$ orbits, so the pair fixes $2^{\sum \gcd(a_i, b_j)}$ matrices.

Take $N \le M$ (swap otherwise). Enumerate the cycle type of the row permutation - a partition of $N$ - with weight $1 / \prod (\text{length}^{count} \cdot count!)$, which is the fraction of permutations with that type. For a fixed row type a column cycle of length $j$ contributes the factor $c_j = 2^{\sum_i \gcd(a_i, j)}$, and the average over all column permutations is the cycle index evaluated at these values:

$$Z_0 = 1, \qquad Z_k = \frac{1}{k} \sum_{j=1}^{k} c_j \, Z_{k-j}.$$

Summing weight times $Z_M$ over all partitions gives the answer.

## Edge cases

- With a single row only the number of ones matters: the answer is $M + 1$.
- The recursion enumerates partitions, so the smaller dimension must be the one that is partitioned.
- All divisions are modular inverses, computed once up to $M$.
- The input is a single line with both dimensions.

## Dry run

`2 x 2`. Row types: two fixed points (weight $1/2$) and one 2-cycle (weight $1/2$).

- Two fixed rows: $c_1 = 2^{1+1} = 4$, $c_2 = 2^{1+1} = 4$. $Z_1 = 4$, $Z_2 = (c_1 Z_1 + c_2 Z_0) / 2 = (16 + 4) / 2 = 10$.
- One 2-cycle: $c_1 = 2^{1} = 2$, $c_2 = 2^{2} = 4$. $Z_1 = 2$, $Z_2 = (4 + 4) / 2 = 4$.

Answer $(10 + 4) / 2 = 7$.
