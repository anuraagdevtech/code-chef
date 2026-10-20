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
