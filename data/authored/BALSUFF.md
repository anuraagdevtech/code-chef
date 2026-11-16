---
topic: Greedy
subtopic: Build left to right, keeping the remaining multiset balanced
time: $O(26 \cdot N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
After a prefix has been written, what remains is exactly a suffix of the final string. So the string is good when, at every moment of the construction, the remaining counts of all characters of $C$ - including characters whose remaining count has dropped to 0 - differ by at most $K$.

The whole string is a suffix too, so if the initial counts are not within $K$ of each other the answer is $-1$.

Otherwise build greedily: at each step take the smallest character whose removal keeps the remaining multiset balanced. Removing one copy of $x$ only lowers the count of $x$, so the only thing that can break is the gap between the current maximum and the new count of $x$: the move is legal exactly when $\max - (\text{cnt}_x - 1) \le K$.

A legal move always exists - removing a character with the maximum count is always fine - so the greedy never gets stuck, and since any legal choice can be completed, taking the smallest legal character at each step gives the lexicographically smallest good string.

## Edge cases

- A single distinct character: the string itself.
- $K \ge$ the largest count: every arrangement is good, so the answer is the sorted string.
- Characters that have run out still count with frequency 0.
- The alphabet has at most 26 letters, so scanning it at every step is cheap.

## Dry run

`S = abcbcac`, `K = 2`. Counts `a:2 b:2 c:3`.

| step | remaining before | choice | reason |
|---:|---|---|---|
| 1 | 2 2 3 | a | $3 - 1 = 2 \le 2$ |
| 2 | 1 2 3 | b | `a` would give $3 - 0 = 3$; `b` gives $3 - 1 = 2$ |
| 3 | 1 1 3 | c | `a` and `b` would give 3; `c` gives $3 - 2 = 1$ |
| 4 | 1 1 2 | a | $2 - 0 = 2$ |
| 5 | 0 1 2 | b | $2 - 0 = 2$ |
| 6 | 0 0 2 | c | |
| 7 | 0 0 1 | c | |

Answer `abcabcc`.
