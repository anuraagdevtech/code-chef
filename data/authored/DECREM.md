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
