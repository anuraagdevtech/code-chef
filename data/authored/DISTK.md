---
topic: Constructive
subtopic: A distinct prefix, one calibrated repeat and a constant tail
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Count good subarrays by their right end: position $i$ contributes the length of the longest all-distinct subarray ending there, which is at least 1. So every array has at least $N$ good subarrays, and we must distribute $K - N$ extra units.

Start with the distinct values $1, 2, \dots, L$: position $j$ contributes $j$, i.e. $j - 1$ extra. Extend the prefix greedily while the remaining extra is at least the cost of the next position. When it stops, the remainder $r$ satisfies $0 \le r < L$.

The next element is chosen to contribute exactly $r + 1$: repeat the value that sits $r + 1$ places from the end of the prefix, i.e. index $L - r$ (1-based). The longest distinct subarray ending at the new position then has exactly $r + 1$ elements. Fill the rest of the array with that same value; each of those positions contributes exactly 1.

## Edge cases

- $K = N$: the array is constant.
- $K = \binom{N+1}{2}$: the whole array is the distinct prefix.
- When the prefix reaches length $N$ there is nothing to append.
- Any valid array is accepted, so the judge needs a checker rather than a text comparison.

## Dry run

`N = 5, K = 7`, so 2 extra units.

Prefix: length 1 costs nothing; extending to length 2 costs 1 (extra left: 1); extending to length 3 would cost 2, too much. $L = 2$, $r = 1$.

Append the value $r + 1 = 2$ places from the end of `[1, 2]`, which is 1, then pad with 1s: `1 2 1 1 1`.

Contributions by right end: `1 2 2 1 1`, total 7.
