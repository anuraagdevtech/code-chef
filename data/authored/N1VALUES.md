---
topic: Constructive
subtopic: Building a sum from a run plus a remainder
time: $O(N)$ per test case
space: $O(N)$
---
We need $N+1$ positive integers summing to $2^N$, with exactly one value repeated and the rest distinct.

Start from the cheapest distinct run, $1, 2, \ldots, N-1$, which uses $N-1$ of the slots and contributes $\frac{N(N-1)}{2}$. Two slots remain. Fill one by **repeating $N-1$** — that supplies the required duplicate — and let the last slot absorb everything left over:

$$L = 2^N - \frac{N(N-1)}{2} - (N-1)$$

The result, sorted, is $1, 2, \ldots, N-2,\ N-1,\ N-1,\ L$.

This works because $2^N$ grows exponentially while the run grows quadratically, so $L$ is comfortably larger than $N-1$ for every $N \geq 2$ — which keeps it distinct from the rest and keeps the list non-decreasing without re-sorting. At $N = 5$, for instance, $L = 32 - 10 - 4 = 18$.

$N = 1$ needs its own answer: two values summing to $2$, and since exactly one value must repeat, the only option is `1 1`.

The construction reproduces both samples exactly — $N = 3$ gives `1 2 2 3` and $N = 4$ gives `1 2 3 3 7` — though **any valid answer is accepted**, so this is judged by a checker rather than by text.

$N$ reaches $60$, so $2^N$ is about $1.15 \times 10^{18}$ — inside a signed 64-bit range, but only just, and worth noting for a C implementation.
