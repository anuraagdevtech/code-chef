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
