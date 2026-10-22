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

## Edge cases

- **The three conditions force the shape $p \cdot q$ with $p < q$ the two smallest primes at least $X$.** No factor below $X$ means every prime factor is $\geq X$; not prime means at least two factors; not a perfect square rules out $p^2$.
- **$p^2$ is the trap.** It is the smallest composite with all factors $\geq p$, and it is excluded precisely because it is a square — which is why the next prime is needed.
- **$p \cdot q$ beats $p^3$**, since Bertrand's postulate gives $q < 2p \leq p^2$ for $p \geq 2$, so no cube can undercut it.
- **$X = 1$ and $X = 2$ give the same answer**, $6$: the smallest prime at least $1$ is still $2$. Note $4$ is rejected as a square.
- **The answer may exceed 32 bits**, as the statement warns: near $X = 10^9$ the product is about $10^{18}$.
- **Primality must be tested, not sieved.** At $X = 10^9$ a sieve is out of the question, so Miller–Rabin with the first twelve prime bases is used — deterministic well past $10^{18}$.
- **$T \leq 5$** keeps the prime-gap walk cheap; gaps near $10^9$ are only a few hundred.

## Dry run

| $X$ | smallest prime $\geq X$ | next prime | $Y$ |
|---:|---:|---:|---:|
| 1 | 2 | 3 | `6` |
| 2 | 2 | 3 | `6` |
| 3 | 3 | 5 | `15` |

For $X = 3$: $9 = 3^2$ is a square, $3 \cdot 5 = 15$ is composite, non-square, and its only factors are $1, 3, 5, 15$ — none below $3$.
