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

## Edge cases

- **$\Omega(i) + 1$ is a valid colouring**, because $x \mid y$ with $x \neq y$ forces $\Omega(y) > \Omega(x)$ — the quotient contributes at least one more prime factor — so the colours of a divisor pair always differ.
- **It is also optimal.** The chain $1 \mid 2 \mid 4 \mid \dots \mid 2^k \leq N$ has $k+1$ members all pairwise divisible, so $C \geq k+1$; and $\Omega(i) \leq \log_2 i \leq k$ gives $C \leq k+1$.
- **So $C = \lfloor \log_2 N \rfloor + 1$**, computed here as $\Omega$ of the highest power of two not exceeding $N$, plus one.
- **$N = 1$** gives $C = 1$: a single element with no divisor pair to worry about.
- **$\Omega$ counts multiplicity, not distinct primes.** $\Omega(4) = 2$ while $\omega(4) = 1$, and using the distinct count would give $4$ and $2$ the same colour despite $2 \mid 4$.
- **The smallest-prime-factor sieve gives $\Omega$ in one pass** via $\Omega(v) = \Omega(v / \mathrm{spf}(v)) + 1$, which is why the sieve stores spf rather than just primality.
- **This colouring differs from the sample's** at $N = 3$ (`1 2 2` against `2 1 1`), and both use $C = 2$ validly, so a special judge checks the divisor pairs.

## Dry run

$N = 3$: the highest power of two is $2$, so $C = \Omega(2) + 1 = 2$.

| $i$ | factorisation | $\Omega(i)$ | colour |
|---:|---|---:|---:|
| 1 | — | 0 | 1 |
| 2 | $2$ | 1 | 2 |
| 3 | $3$ | 1 | 2 |

Divisor pairs: $1 \mid 2$ (colours $1 \neq 2$ ✓) and $1 \mid 3$ ($1 \neq 2$ ✓). The pair $2, 3$ has no divisibility, so sharing colour $2$ is fine.
