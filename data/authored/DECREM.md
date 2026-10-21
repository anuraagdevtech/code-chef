---
topic: Number Theory
subtopic: A strictly decreasing chain of remainders
time: $O(1)$ per test case
space: $O(1)$
---
Two observations settle this completely.

**When no solution exists.** The chain $N \bmod L > N \bmod (L+1) > \cdots > N \bmod R$ holds $R - L + 1$ strictly decreasing non-negative integers, so its first term must be at least $R - L$. But $N \bmod L \leq L - 1$ always, so a solution requires

$$L - 1 \geq R - L \quad\Longleftrightarrow\quad R \leq 2L - 1 \quad\Longleftrightarrow\quad R < 2L$$

If $R \geq 2L$ the answer is $-1$. That single test also covers $L = 1$, where $N \bmod 1 = 0$ can never exceed anything.

**When it does, the answer is $N = R$.** For every $k$ in $[L, R]$ we have $k \geq L > R/2$, so $R < 2k$ and therefore $R \bmod k = R - k$. The chain becomes $R-L,\ R-L-1,\ \ldots,\ 1,\ 0$ — strictly decreasing, exactly as required.

It is also the **smallest** such $N$. Any $N < R$ has $N \bmod R = N$, while $N \bmod (R-1)$ is either $N$ itself (when $N < R-1$) or $0$ (when $N = R-1$). The first case needs $N > N$ and the second needs $0 > R-1$; both are impossible. So nothing below $R$ works.

Sample case 1 has $L=4, R=6$ with $6 < 8$, giving $N = 6$: the remainders are $2, 1, 0$. Sample case 2 has $L=1, R=2$ and $2 \geq 2$, so $-1$.

The promise that answers fit in $10^{18}$ is generous — the answer is never larger than $R \leq 10^6$.

## Edge cases

- **$n = r$ is the canonical witness.** Dividing $r$ by each $d \in [l, r]$ gives remainders $r - l, r - l - 1, \ldots, 1, 0$ — decreasing by exactly one each step — provided every divisor exceeds $r/2$ so the quotient is $1$ throughout. That condition is precisely $r < 2l$.
- **When $r \geq 2l$ no $n$ works at all.** Some divisor $d \leq r/2$ then has a quotient of $2$ or more, which breaks the chain, and the answer is $-1$. Checked exhaustively against brute force for all $1 \leq l < r \leq 39$ with no mismatch.
- **$l = 1$ is always hopeless**: $n \bmod 1 = 0$ is the first term and nothing can be smaller, and indeed $r \geq 2 = 2l$ holds automatically. The second sample row is this case.
- **$L < R$ is guaranteed**, so the chain always has at least two terms and the degenerate single-remainder case never arises.
- **The answer can be as large as $10^6$** and needs no search — it is read straight off $R$.
- **$T$ up to $10^5$** with constant work per case.

## Dry run

First sample: $L = 4$, $R = 6$, and $6 < 8$, so $n = 6$.

| divisor $d$ | $6 \bmod d$ |
|---:|---:|
| 4 | 2 |
| 5 | 1 |
| 6 | 0 |

Strictly decreasing, so `6`. The second row has $L = 1$, $R = 2$: $2 \bmod 1 = 0$ already, and nothing is below it, so `-1`.
