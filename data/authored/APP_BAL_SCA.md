---
topic: Number Theory
subtopic: Halving only reaches the odd part
time: $O(\log M)$ per test case
space: $O(1)$
---
The balance offers exactly three moves: halve a known weight when both halves are integers, duplicate a known weight, and add known weights together. None of them can produce a finer division than repeated halving, so the **smallest** weight reachable from $M$ is

$$q = \frac{M}{2^{\nu_2(M)}}$$

the odd part of $M$, obtained by halving as long as the result stays an integer. Everything reachable is a sum of pieces of size $q$ or multiples of it, so every achievable weight is a multiple of $q$. And duplication is capped by the stock on hand, so nothing above $M$ is reachable.

Conversely every multiple of $q$ up to $M$ *is* reachable: halve $M$ all the way down to $2^{\nu_2(M)}$ pieces of size $q$, then combine as many as needed. So

$$\text{answer} = \text{YES} \iff N \leq M \text{ and } q \mid N$$

The point is that the balance can only bisect, never trisect — which is why an odd $M$ is completely rigid: $q = M$, and the only reachable weight is $M$ itself.

The samples show all three failure-free and failure cases. $M = 2, N = 1$: one halving gives $1$. $M = N = 1$: nothing to do. $M = 5, N = 1$: $5$ is odd, so $q = 5$ and only $5$ is reachable — `NO`. And $M = 4, N = 9$ asks for more apples than exist.

With $M$ up to $10^{18}$ the halving loop runs at most $60$ times, so $T = 2 \times 10^5$ is comfortable.

## Edge cases

- **A balance with no weights can only bisect**, so from $M$ the reachable amounts are sums of $M/2^j$ pieces — that is, $M p / 2^j$ for integers $p, j$.
- **So $N$ is reachable iff the odd part of $M$ divides $N$**, since the powers of two can always be supplied by halving far enough while the odd factor can never be split.
- **$N$ must also not exceed $M$**, which is the other half of the test — the fourth row has $N = 9$ against $M = 4$ and fails on size alone.
- **The third row fails on the odd part**: $M = 5$ is already odd, so every reachable amount is a multiple of $5$ and $N = 1$ is out of reach.
- **$M$ a power of two makes the odd part $1$**, so every $N \leq M$ works — the first row, where $2$ halves into $1$ and $1$.
- **$M = N$ always works** with no weighing at all.
- **$M, N$ up to $10^{18}$**: the odd part is found by at most $60$ halvings, and the arithmetic stays exact.

## Dry run

| $M$ | odd part of $M$ | $N$ | $N \leq M$? | odd part divides $N$? | output |
|---:|---:|---:|:---:|:---:|---|
| 2 | 1 | 1 | yes | yes | `YES` |
| 1 | 1 | 1 | yes | yes | `YES` |
| 5 | 5 | 1 | yes | **no** | `NO` |
| 4 | 1 | 9 | **no** | yes | `NO` |

For the first row: balance $2$ kg into two piles of $1$ kg each.
