---
topic: Number Theory
subtopic: Sieve of distinct prime factors plus prefix counts
time: $O(V \log \log V + 5V)$ precomputation, $O(1)$ per query
space: $O(5V)$
---
With $T$ up to $10^4$ and ranges up to $10^5$, factorising per query would be wasteful — and entirely avoidable, since the universe of numbers is fixed. Everything is precomputed once.

First, a sieve variant that counts **distinct** prime factors for every $n \leq 10^5$. Walk $p$ upward; if $\omega[p]$ is still $0$ then no smaller prime divides $p$, so $p$ is prime, and we add one to $\omega[m]$ for every multiple $m$ of $p$:

$$\omega[n] = \#\{p \text{ prime} : p \mid n\}$$

Counting multiples rather than factorising means each prime touches $V/p$ entries, for $O(V \log \log V)$ total. Note multiplicity is ignored by construction — $4 = 2^2$ is visited only by $p = 2$, so $\omega[4] = 1$ and $4$ is a $1$-prime.

Second, because $K \leq 5$, build five prefix-count arrays $\mathrm{pre}_k[n] = \#\{x \leq n : \omega[x] = k\}$. Each query is then a subtraction:

$$\mathrm{pre}_K[B] - \mathrm{pre}_K[A-1]$$

The samples exercise the edges. For $K = 1$ on $[2,5]$ all four of $2, 3, 4, 5$ qualify — $4$ included, which is the multiplicity trap. For $K = 2$ on $[4,10]$ only $6$ and $10$ qualify. And $K = 3$ on $[2,20]$ gives $0$, since the smallest number with three distinct primes is $2 \cdot 3 \cdot 5 = 30$. In general the smallest $K$-prime is the product of the first $K$ primes, so $K = 5$ needs $n \geq 2310$.
