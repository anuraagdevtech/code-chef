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
