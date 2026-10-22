---
topic: Number Theory
subtopic: Reducing a nested modulo to a divisibility test
time: $O(N \cdot d)$ per test case after an $O(M)$ sieve
space: $O(M)$
---
Fix $a < b$. Then $M \bmod a < a < b$, so the outer modulo on the left does nothing:

$$(M \bmod a) \bmod b = M \bmod a$$

Writing $M = qb + r$ with $q = \lfloor M/b \rfloor$ and $r = M \bmod b$, the right-hand side is $r \bmod a$, and the condition becomes

$$(qb + r) \equiv r \pmod a \quad\Longleftrightarrow\quad qb \equiv 0 \pmod a$$

So the whole nested-modulo equation collapses to a **divisibility test**:

$$a \;\Big|\; b \left\lfloor \frac{M}{b} \right\rfloor \;=\; M - (M \bmod b)$$

Two immediate consequences. Whenever $a \mid b$ the condition holds automatically, so every such pair counts — including all pairs with $a = 1$. And when $b > M$ the quotient is $0$, making the product $0$, which every $a$ divides — so all $b - 1$ partners qualify.

Otherwise the count for a given $b$ is the number of divisors of $V_b = b\lfloor M/b\rfloor$ that fall below $b$, found by factorising $V_b$ through a smallest-prime-factor sieve and enumerating its divisors.

Sample $N = 3, M = 5$ gives $2$: the pairs with $a = 1$ both qualify, while $(2,3)$ has $V = 3$, which $2$ does not divide. Raising $M$ to $6$ makes $V = 6$ for that pair, so all three count.

The honest caveat: with $\sum N = 10^6$ this is near the edge in Python even though the algorithm is right — the sieve and divisor enumeration are what a C++ submission would breeze through.

## Edge cases

- **The nested modulo collapses.** With $a < b$ we have $M \bmod a < a < b$, so the left side is just $M \bmod a$; and the condition becomes $M \bmod a = (M \bmod b) \bmod a$, i.e. $a \mid \bigl(M - (M \bmod b)\bigr) = a \mid b \lfloor M/b \rfloor$.
- **So for each $b$ the answer is the number of its partners below it that divide $b \lfloor M/b \rfloor$** — a divisor count, not a search over pairs.
- **$b > M$ makes the product zero**, and every $a$ divides $0$, so all $b-1$ partners qualify. Without that branch the divisor routine would be handed $0$ and loop forever.
- **$a < b$ is strict**, so the divisors counted are those strictly below $b$.
- **The divisors are generated from the smallest-prime-factor sieve**, built once across all test cases to the largest $M$ — re-factorising per pair would be far too slow.
- **$a = 1$ always qualifies**, since $1$ divides everything, so every $b \geq 2$ contributes at least one pair.
- **Sum of $N \leq 10^6$** with $M \leq 5 \cdot 10^5$, so the sieve dominates the memory and the per-$b$ divisor work stays small.

## Dry run

Second sample: $N = 3$, $M = 6$.

| $b$ | $\lfloor M/b \rfloor$ | $b \lfloor M/b \rfloor$ | divisors below $b$ | pairs |
|---:|---:|---:|---|---:|
| 2 | 3 | 6 | $\{1\}$ | 1 |
| 3 | 2 | 6 | $\{1, 2\}$ | 2 |

Output `3`. Checking $(2,3)$ directly: $((6 \bmod 2) \bmod 3) = 0$ and $((6 \bmod 3) \bmod 2) = 0$ ✓
