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
