---
topic: Dynamic Programming
subtopic: Every part needs all values below the global MEX - count partitions with a prefix-sum DP
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If every part has MEX $m$, then every part contains $0, \dots, m - 1$ and none contains $m$; so the whole array contains $0, \dots, m - 1$ and not $m$, which means $m$ is the MEX of the whole array. Conversely a part has that MEX as soon as it contains all of $0, \dots, m - 1$, because $m$ does not occur anywhere.

If $m = 0$ there is no requirement at all and every one of the $2^{N-1}$ ways to cut the array is valid.

Otherwise let `ways[i]` be the number of valid partitions of the first $i$ elements. The last part $(j, i]$ is valid exactly when it contains every required value, i.e. when $j$ is at most the smallest among the last occurrences (up to $i$) of the values $0 \dots m - 1$. Call that position $\ell_i$ (0-based index); then

$$\text{ways}[i] = \sum_{j \le \ell_i} \text{ways}[j],$$

a prefix sum of the DP values, and 0 while some required value has not appeared yet. The minimum of the last occurrences changes as the scan proceeds; it is kept in a heap of (last occurrence, value) pairs with outdated entries discarded lazily.

## Edge cases

- MEX 0 (no zero in the array): the answer is $2^{N-1}$.
- A prefix that lacks some required value cannot be a complete part: `ways` is 0 there.
- Values at or above the MEX are irrelevant.
- Everything is modulo $10^9 + 7$.

## Dry run

`A = [1, 0, 0, 1, 0, 1]`, MEX 2, required values 0 and 1. `prefix` starts as `[1]` (the empty prefix).

| i | value | last(0), last(1) | limit | ways | prefix |
|---:|---:|---|---:|---:|---|
| 1 | 1 | -, 1 | - | 0 | 1 |
| 2 | 0 | 2, 1 | 1 | 1 | 2 |
| 3 | 0 | 3, 1 | 1 | 1 | 3 |
| 4 | 1 | 3, 4 | 3 | 2 | 5 |
| 5 | 0 | 5, 4 | 4 | 3 | 8 |
| 6 | 1 | 5, 6 | 5 | 5 | 13 |

(Positions are 1-based here; "limit" is the latest allowed start of the last part, and `ways` is the prefix total just before it.) Answer 5.
