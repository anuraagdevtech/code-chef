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

## Edge cases

- **Distinct primes, not total factors.** $4 = 2^2$ counts as $1$, and so do $8$ and $16$ — which is why the sieve adds one per *prime* over its multiples, never once per prime power.
- **The answer can be $0$** (the fourth row): the smallest number with three distinct prime factors is $30$, so a range ending at $20$ has none.
- **$A \geq 2$ is guaranteed**, so `row[a - 1]` never reaches a negative index.
- **$0$ and $1$ have no prime factors**, so they sit at $\omega = 0$ and are never counted for $K \geq 1$.
- **A prime is detected by $\omega(p)$ still being $0$** when the outer loop reaches it — the pass doubles as both sieve and counter.
- **$K \leq 5$** means only five prefix rows are needed, so the $5 \times 10^5$ table is affordable where a per-query scan at $T = 10^4$ would not be.
- **Both endpoints are inclusive**, which the prefix difference `row[b] - row[a-1]` handles directly.

## Dry run

| range | $K$ | numbers and their distinct prime counts | matches |
|---|---:|---|---:|
| $2 \dots 5$ | 1 | $2{:}1$, $3{:}1$, $4{:}1$, $5{:}1$ | `4` |
| $4 \dots 10$ | 2 | $6{:}2$, $10{:}2$ (others $1$ or more) | `2` |
| $14 \dots 15$ | 2 | $14 = 2 \cdot 7$, $15 = 3 \cdot 5$ | `2` |
| $2 \dots 20$ | 3 | none reach three distinct primes | `0` |

Note $4$, $8$ and $16$ all have $\omega = 1$, which is what the first row relies on.
