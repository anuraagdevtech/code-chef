---
topic: Greedy
subtopic: Pair large values with small weights
time: $O(N)$ per test case
space: $O(N)$
---
Expand the objective. Each $P_j$ is counted once for every triplet containing position $j$, so the sum is

$$\frac{1}{3}\sum_{j=1}^{N} w_j \, P_j, \qquad w_j = \#\{i : i \leq j \leq i+2,\ 1 \leq i \leq N-2\}$$

The weights run $1, 2, 3, 3, \ldots, 3, 2, 1$ — the ends appear in fewer triplets than the middle.

Minimising a weighted sum with a fixed multiset of values is the **rearrangement inequality**: pair the largest values with the smallest weights. So put $N$ and $N-1$ at the two ends, $N-2$ and $N-3$ just inside them, and the remaining values anywhere in the middle, where every weight is $3$.

The intuition is worth keeping: the interior is expensive real estate, charged three times over, so the big numbers belong at the edges.

Sorting the positions by weight ascending and handing out $N, N-1, \ldots, 1$ in that order implements this directly.

**The answer is not unique**, and the problem says so — any optimal permutation is accepted, so this is judged by a special checker rather than by exact match. The two samples even use different-looking arrangements: for $N = 3$ every weight is $1$, so *every* permutation is optimal, while for $N = 4$ the weights are $1,2,2,1$ and the two largest values must take the ends. The permutation produced here is optimal but will generally differ from the sample text, so a naive diff against the expected output will report a mismatch where none exists.

Sorting by weight is $O(N \log N)$; since the weights take only three values the positions can be emitted directly in $O(N)$, which is what matters at $\sum N = 3 \times 10^5$.

## Edge cases

- **The weight of a position is how many triplets cover it**, which runs $1, 2, 3, \ldots, 3, 2, 1$ across the array and is capped at $3$ and at $N - 2$. The whole objective is $\frac{1}{3}\sum_j w_j P_j$, so minimising it is a weighted-sum problem.
- **The rearrangement inequality decides the assignment**: pairing the largest values with the smallest weights minimises the sum, so the permutation is built by sorting positions by weight and filling in descending value.
- **$N = 3$** (the second sample row): every position has weight $1$, so *every* permutation is optimal — the sorted-by-weight order happens to reproduce the sample exactly.
- **$N = 4$**: weights are $1, 2, 2, 1$, so the two ends take $4$ and $3$ and the middle takes $2$ and $1$. This answer is `4 2 1 3` where the sample shows `3 2 1 4`; both sum to $13$ in weighted terms, and the statement allows any optimal permutation.
- **$N - 2$ in the cap matters for small $N$**, since there are only $N - 2$ triplets in total and no position can be covered more often than that.
- **Sum of $N \leq 3 \cdot 10^5$**: the sort by weight is the dominant cost, and the weight array is computed in closed form rather than by counting windows.

## Dry run

$N = 4$: triplets are $(1,2,3)$ and $(2,3,4)$.

| position | covered by | weight | rank by weight | value assigned |
|---:|---|---:|---:|---:|
| 1 | one triplet | 1 | 1st | **4** |
| 2 | both | 2 | 3rd | 2 |
| 3 | both | 2 | 4th | 1 |
| 4 | one triplet | 1 | 2nd | **3** |

Weighted sum $4(1) + 2(2) + 1(2) + 3(1) = 13$, the minimum; the sample's `3 2 1 4` also gives $13$.
