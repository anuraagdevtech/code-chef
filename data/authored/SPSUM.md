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

## Edge cases

- **The two sums are forced by $S$ and $M$.** Their total is $S = N(N+1)/2$ and their difference is $M$, so they must be $(S+M)/2$ and $(S-M)/2$ — there is nothing to search.
- **Parity must match**: if $S + M$ is odd no integer split exists, so the answer is `No` before any gcd is computed.
- **$M$ cannot exceed $S$** (the second row, $N = 1$ with $M = 2$), since the larger share is at most everything.
- **Any target in $[0, S]$ is a reachable subset sum** of $1 \dots N$, which is why only the parity and the gcd need checking and no feasibility search over subsets is needed.
- **The gcd condition is the real test**, and it can fail even when the arithmetic works out — for instance $N = 4$ with $M = 0$ gives $5$ and $5$, whose gcd is $5$.
- **$M$ up to $10^{18}$ and $N$ up to $10^9$** put $S$ near $5 \times 10^{17}$, so exact integers are required throughout.

## Dry run

First sample: $N = 5$, so $S = 15$, and $M = 7$.

| step | value |
|---|---|
| $S + M = 22$ | even ✓ |
| A's share $(S+M)/2$ | 11 |
| B's share $(S-M)/2$ | 4 |
| $\gcd(11, 4)$ | 1 ✓ |

Output `Yes` — for instance A takes $\{5, 4, 2\}$ and B takes $\{1, 3\}$.
