---
topic: Arrays
subtopic: Positions of the largest values must form one contiguous block
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
What remains must be a permutation of $1 \dots m$ for some $m \ge 1$, so the removed elements are exactly the values $m+1, \dots, N$. Removing them is one operation precisely when they occupy a contiguous block of positions.

Add the values $N, N-1, \dots$ one at a time while tracking the smallest and largest position seen. The values $v \dots N$ form a contiguous block exactly when (largest $-$ smallest $+ 1$) equals how many there are, $N - v + 1$. The best score is the largest such count; removing only the value $N$ is always possible, so the answer is at least 1.

## Edge cases

- At least one element must stay, so the scan stops at value 2.
- A sorted permutation lets everything but the 1 go: answer $N - 1$.
- The value $N$ alone is always a valid block.
- Larger candidate sets are checked later in the scan, so the last success is the maximum.

## Dry run

`A = [3, 1, 4, 6, 5, 2]` (positions 1-6: value 6 at 4, 5 at 5, 4 at 3, 3 at 1, 2 at 6).

| values removed | positions span | count | block? |
|---|---|---:|---|
| 6 | 4-4 | 1 | yes |
| 5, 6 | 4-5 | 2 | yes |
| 4, 5, 6 | 3-5 | 3 | yes |
| 3..6 | 1-5 | 4 | no |
| 2..6 | 1-6 | 5 | no |

Answer 3.
