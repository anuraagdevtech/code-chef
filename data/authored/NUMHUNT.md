---
topic: Number Theory
subtopic: Product of the two smallest admissible primes
time: $O(g \log^3 X)$ per test case, where $g$ is the local prime gap
space: $O(1)$
---
Translate each condition into the factorisation of $Y$:

- "no factor other than $1$ below $X$" means **every prime factor of $Y$ is at least $X$**;
- "not prime" means $Y$ has at least two prime factors counted with multiplicity;
- "not a perfect square" rules out $Y = p^2$, the smallest two-factor option.

So $Y = pq$ with $p \neq q$ both prime and both $\geq X$, and the minimum is obtained by taking $p$ as the smallest prime $\geq X$ and $q$ as the next prime after it. Nothing smaller can work: $p^2$ is excluded as a square, and any product of three or more admissible primes is at least $p^3 > pq$ (since $q < p^2$ by Bertrand's postulate).

At $X \leq 10^9$ the candidates are far too large to sieve, so test individual numbers with a deterministic **Miller–Rabin** over the bases $2, 3, 5, \ldots, 37$, which is exact below $3 \times 10^{24}$. Prime gaps near $10^9$ are only a few hundred, so a handful of tests per query suffices and $T \leq 5$ makes this trivial.

The samples show the small cases and the square trap. $X = 1$ and $X = 2$ both give $2 \cdot 3 = 6$ — note $4 = 2^2$ is rejected as a square, which is why the answer is not $4$. $X = 3$ skips $4$ (factor $2 < 3$) and $9 = 3^2$ (square), landing on $3 \cdot 5 = 15$.

The statement's warning about 32-bit overflow is the product: near $X = 10^9$ the answer is about $10^{18}$.
