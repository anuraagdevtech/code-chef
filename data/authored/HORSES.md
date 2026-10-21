---
topic: Sorting
subtopic: Minimum adjacent difference after sorting
time: $O(N \log N)$ per test case
space: $O(N)$
---
The closest pair of values in a set must be **adjacent once sorted**. If two values $x < y$ had anything between them, that in-between value would be closer to each of them than they are to each other — so the minimum difference can only occur between neighbours.

That observation turns an $O(N^2)$ comparison of all pairs into a sort plus a single linear scan:

$$\min_{1 \leq i < N} \bigl(S_{i+1} - S_i\bigr)$$

on the sorted array. At $N = 5000$ the quadratic version is about $12$ million comparisons and would likely pass, but the sorted scan is both faster and the idea that generalises.

After sorting, the differences are automatically non-negative, so no absolute value is needed — a small simplification that only holds *because* the array is sorted.

Sample: $[4, 9, 1, 32, 13]$ sorts to $[1, 4, 9, 13, 32]$ with gaps $3, 5, 4, 19$, so the answer is $3$, from the pair $(1, 4)$ that sits far apart in the original input.

Duplicates, if present, would give a difference of $0$, which the scan reports correctly with no special case.

Values reach $10^9$, so a difference fits comfortably in 32 bits — but a C solution computing anything cumulative would want care. The guarantee $N \geq 2$ means at least one pair exists.

## Edge cases

- **The closest pair is always adjacent once sorted.** For $i < j < k$ in sorted order, $a_k - a_i \geq a_k - a_j$, so any non-adjacent pair is beaten by a pair nested inside it — which is why only $N-1$ differences need examining instead of all $\binom{N}{2}$.
- **Duplicate skills give $0$**, the smallest possible answer, and need no special handling.
- **$N \geq 2$ is guaranteed**, so there is always at least one pair and `min` never sees an empty sequence.
- **The best pair need not be at either end.** In the sample the winning difference of $3$ comes from $1$ and $4$ at the low end, but the array also has a run $9, 13$ with difference $4$ — all adjacent gaps must be compared, not just the first or last.
- **Values up to $10^9$**: differences stay well inside the integer range.

## Dry run

Values $4, 9, 1, 32, 13$, sorted to $1, 4, 9, 13, 32$.

| pair | difference |
|---|---:|
| $1, 4$ | **3** |
| $4, 9$ | 5 |
| $9, 13$ | 4 |
| $13, 32$ | 19 |

Output `3`.
