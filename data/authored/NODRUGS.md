---
topic: Conditionals & Case Work
subtopic: Monotone objective, so only an endpoint dose matters
time: $O(N)$ per test case
space: $O(1)$
---
The friend's final speed $S_N + uK$ is **monotone in the dose $u$**, so the best dose is always an endpoint of the legal range and there is nothing to search. The dose must stay strictly below $L$ to escape detection, so $u \in \{0, 1, \ldots, L-1\}$ — note the test catches $u \geq L$, which makes the usable maximum $L-1$, the classic off-by-one here.

With $m = \max(S_1, \ldots, S_{N-1})$, winning requires a **strict** maximum, since ties mean nobody wins:

$$S_N + uK > m$$

- $K > 0$: more is better, so take $u = L-1$.
- $K \leq 0$: the drug does not help, so take $u = 0$ and race clean. A negative $K$ is a pure liability.

So the whole problem is one comparison, with $\max(0, (L-1)K)$ as the best boost.

The first two samples are the same race one point apart: with $S_N = 2$, $K = 2$, $L = 2$ the single legal dose gives $4$, which beats a rival's $3$ but not a rival's $4$ — the second case failing precisely because equality is not a win.

The third sample has $K = -10$ and a generous $L = 100$, but every unit *lowers* the speed, so the honest dose of $0$ is optimal, and $9 < 12$ loses anyway.

The degenerate $N = 1$ case leaves the max over rivals empty; the friend is then the sole participant and wins outright, which the code handles by treating the rival maximum as $-\infty$.

## Edge cases

- **The dose is capped at $L - 1$**, because the test catches him at $L$ units *or more* — so the boost is $(L-1)K$ and not $LK$. With $L = 1$ no dose at all is safe, and the boost is zero.
- **A non-positive $K$ makes the drug useless or harmful**, so the best dose is zero. The third row has $K = -10$: any dose only slows him, and the answer rests on his unaided speed.
- **A tie is not a win.** The statement says that when several share the top speed nobody wins, so the comparison is strict — the second row reaches exactly $4$ against a rival's $4$ and answers `No`.
- **Only the fastest rival matters**, so the first $N-1$ speeds collapse to their maximum.
- **$N = 1$**: there are no rivals, so the friend wins outright; the $-\infty$ sentinel handles it without a branch.
- **The objective is linear in the dose**, so only an endpoint can be optimal — either $0$ units or the maximum safe $L - 1$ — which is why no search over doses is needed.

## Dry run

| $N$ | $K$ | $L$ | speeds | best rival | boost | friend's speed | $>$ rival? | output |
|---:|---:|---:|---|---:|---:|---:|:---:|---|
| 4 | 2 | 2 | $2,1,3,2$ | 3 | $1 \times 2 = 2$ | 4 | yes | `Yes` |
| 4 | 2 | 2 | $2,1,4,2$ | 4 | 2 | 4 | **no (tie)** | `No` |
| 3 | $-10$ | 100 | $12,11,9$ | 12 | 0 | 9 | no | `No` |

Row 3 could take up to $99$ units, but every one of them would cost $10$ speed.
