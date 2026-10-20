---
topic: Number Theory
subtopic: Splitting a fixed total under a gcd condition
time: $O(\log S)$ per test case
space: $O(1)$
---
The two sums are completely determined. With $S = \frac{N(N+1)}{2}$ the total of $1 \ldots N$, requiring $a + b = S$ and $|a - b| = M$ gives

$$a = \frac{S + M}{2}, \qquad b = \frac{S - M}{2}$$

So three conditions must hold:

1. $M \leq S$, or $b$ would be negative;
2. $S + M$ must be **even**, or the halves are not integers;
3. $\gcd(a, b) = 1$.

Nothing else is needed — in particular, **any** target $a$ in $[0, S]$ is achievable as a subset sum of $1, 2, \ldots, N$, since the values $1 \ldots N$ hit every total in that range. So feasibility of the split never has to be checked separately, and no search is required.

The gcd condition has a neat reading: any common divisor of $a$ and $b$ divides both their sum $S$ and their difference $M$, so the test is closely tied to $\gcd(S, M)$ — but computing $\gcd(a,b)$ directly is simplest and avoids edge cases around $M = 0$.

The problem's note that $\gcd(0, k) = k$ matters when $M = S$: then $b = 0$ and the gcd is $a = S$, which is coprime to nothing unless $S = 1$. The formula handles it without a special case.

Sample case 1: $N = 5$ gives $S = 15$, and $M = 7$ makes $S + M = 22$ even, so $a = 11$ and $b = 4$ with $\gcd = 1$ — `Yes`. Sample case 2 has $S = 1$ against $M = 2$, failing the first condition.

With $N$ up to $10^9$, $S$ reaches about $5 \times 10^{17}$ and $M$ up to $10^{18}$, so this is **64-bit** arithmetic outside Python.
