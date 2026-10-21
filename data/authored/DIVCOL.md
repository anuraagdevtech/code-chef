---
topic: Number Theory
subtopic: Colouring the divisibility order by prime-factor count
time: $O(N \log \log N)$ per test case
space: $O(N)$
---
**The lower bound.** The chain $1 \mid 2 \mid 4 \mid \cdots \mid 2^k$ lies entirely inside $1 \ldots N$ whenever $2^k \leq N$, and every element of a chain must get a different value. The longest such chain has $\lfloor \log_2 N \rfloor + 1$ elements, so

$$C \geq \lfloor \log_2 N \rfloor + 1$$

**A matching construction.** Let $\Omega(i)$ count the prime factors of $i$ **with multiplicity**, and set

$$A_i = \Omega(i) + 1$$

If $x \mid y$ with $x \neq y$, then $y = x \cdot m$ for some $m > 1$, so $\Omega(y) = \Omega(x) + \Omega(m) > \Omega(x)$ — the values differ, as required. In fact they are strictly ordered along every divisibility chain, which is more than the problem demands.

The largest value used is $\Omega(2^k) + 1 = k + 1$ where $2^k \leq N$, matching the lower bound exactly. So this $C$ is optimal.

$\Omega$ is computed for the whole range with a smallest-prime-factor sieve and the recurrence $\Omega(i) = \Omega(i / \mathrm{spf}(i)) + 1$, seeded by $\Omega(1) = 0$.

For $N = 3$ this gives $C = 2$ and $A = [1, 2, 2]$. The published sample prints $[2, 1, 1]$ — the same colouring with the two values swapped, equally valid — so this is judged by a checker. $N = 1$ gives $C = 1$ and $A = [1]$.

Note it is $\Omega$ (with multiplicity) rather than $\omega$ (distinct primes) that is needed: $\omega(2) = \omega(4) = 1$ would collide on the chain $2 \mid 4$.
