---
topic: Number Theory
subtopic: Sieve plus a short search
time: $O(\log H)$ per test case after an $O(V \log\log V)$ sieve
space: $O(V)$ with $V = 10^6$
---
Regular attacks are forced: the first deals $1$, the second $2$, the third $4$, and so on. So $k$ regular attacks deal exactly

$$1 + 2 + 4 + \cdots + 2^{k-1} = 2^k - 1$$

no matter how they are interleaved with the special move, because the special move does not touch the attack power.

That leaves only two decisions: how many regular attacks, and whether to spend the one special move. The damage must total exactly $H$, so for each $k$:

- if $2^k - 1 = H$, the monster dies in $k$ moves with no special;
- otherwise the special must cover the remainder $P = H - (2^k - 1)$, which is legal only if $P$ is **prime** — costing $k+1$ moves.

Since $H \leq 10^6$, $k$ never exceeds about $20$, so scanning $k$ upward and stopping at the first success gives the minimum. Primality is answered in $O(1)$ from a sieve built once.

The constraint $P \leq H$ is automatically satisfied — using the special move **first**, while the monster is at full health, makes it so, and the ordering is free.

Sample $H = 10$: neither $k=0$ ($P=10$, composite) nor $k=1$ ($P=9$) works, but $k=2$ leaves $P = 7$, prime — three moves.

Sample $H = 21$ is the impossible case: $22$ is not a power of two, and every remainder $21, 20, 18, 14, 6$ is composite, so $-1$.

Note $P$ must be at least $2$; a remainder of $1$ is not prime, which is why $k$ values leaving exactly $1$ are rejected.

## Edge cases

- **$k$ regular attacks always deal exactly $2^k - 1$**, since the power doubles each time: $1 + 2 + 4 + \dots + 2^{k-1}$. The order of moves is therefore irrelevant and only the count matters.
- **The special move must cover the whole remainder**, so the remainder has to be prime — the single prime is the only flexibility available.
- **An exact power-of-two-minus-one health needs no special move.** If $2^k - 1 = H$ the answer is $k$, which the equality check catches before the primality test.
- **Some health values are unreachable** (the second row, $H = 21$): every remainder $21 - (2^k - 1)$ is composite for all valid $k$, so the answer is $-1$.
- **The loop bound is $2^k - 1 \leq H$**, which keeps $k$ under about $20$ for $H \leq 10^6$ and guarantees termination.
- **The remainder is always within the sieve** because it is at most $H \leq 10^6$, but the explicit bound check keeps the index safe.
- **Fewer regular attacks are always better**, so the first $k$ that works is optimal — the loop breaks immediately on success.

## Dry run

First sample: $H = 10$.

| $k$ | regular damage $2^k - 1$ | remainder | remainder prime? | total moves |
|---:|---:|---:|:---:|---:|
| 0 | 0 | 10 | no ($2 \cdot 5$) | — |
| 1 | 1 | 9 | no ($3^2$) | — |
| 2 | 3 | **7** | **yes** | $2 + 1 = $ `3` |

Two regular attacks deal $1$ and $2$, then the special move deals the prime $7$.
