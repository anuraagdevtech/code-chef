---
topic: Number Theory
subtopic: Sieve counting distinct prime factors
time: $O(V \log\log V)$ once, then $O(m - n)$ per query
space: $O(V)$ with $V = 10^6$
---
The energy for the step from level $k$ to $k+1$ is $\omega(k)$, the number of **distinct** prime factors of $k$. Travelling from $n$ to $m$ means taking the steps at $n, n+1, \ldots, m-1$, so the total is

$$\sum_{k=n}^{m-1} \omega(k)$$

Note the upper limit: the step *out of* level $m$ is never taken, so $\omega(m)$ is excluded. The statement's phrase about $n$ and $m$ being inclusive refers to the levels visited, not the steps paid for — and the sample settles it. From $3$ to $7$ the costs are $\omega(3), \omega(4), \omega(5), \omega(6) = 1, 1, 1, 2$, totalling $5$. Including $\omega(7)$ would give $6$.

Computing $\omega$ for every value up to $10^6$ is a **modified sieve**: start an array of zeros and, for each $p$ from $2$ upward, if $\omega[p]$ is still $0$ then $p$ is prime, so add $1$ to every multiple of $p$. Each number ends up counting exactly its distinct prime divisors. That is $O(V \log\log V)$ overall — the same shape as Eratosthenes, but incrementing instead of marking.

Note $\omega(1) = 0$, since $1$ has no prime factors; the sieve gives this for free by never touching index $1$.

A prefix-sum array over $\omega$ would make each query $O(1)$, which would matter for many queries — but $T \leq 2$ here, so a direct sum over the range is plenty. Building the sieve once, outside the test-case loop, is the part that actually matters.
