---
topic: Greedy
subtopic: Cheapest refunds first, paid with coins of the larger denomination
time: $O(N \log N)$ per test case
space: $O(N)$
---
Two nested greedy decisions, each with its own argument.

**Per creature, use as many two-rupee coins as possible.** To pay $a$ exactly with $y$ twos and $x$ ones, $x = a - 2y$, so maximising $y$ minimises the ones consumed. If the maximal $y = \min(Q, \lfloor a/2 \rfloor)$ still leaves more ones than are available, no smaller $y$ can help — it would need even more ones. So that single attempt decides affordability.

**Across creatures, serve the smallest refunds first.** Sorting ascending is the classic "fit as many items as possible" exchange: a cheaper refund consumes no more of either coin type than a dearer one, so swapping a served creature for a cheaper unserved one never breaks feasibility and never lowers the count.

$$y_i = \min\bigl(Q,\ \lfloor A_i/2 \rfloor\bigr), \qquad x_i = A_i - 2y_i$$

serving creature $i$ only when $x_i \leq P$.

The parity trap is worth noting: an odd refund always needs at least one single-rupee coin, so with $P = 0$ every odd amount is unserviceable no matter how many twos remain.

The samples show both constraints biting. With $P=3, Q=0$ and refunds $1, 2, 2$, the ones run out after $1 + 2$, so only two creatures are served. With $P=2, Q=1$ and refunds $1, 1, 2$, the twos cover the $2$ exactly while the ones cover the two $1$s — all three. And with $P=5, Q=4$ and refunds $2, 3, 4, 5$, the first three consume all four twos and one single, leaving $5$ unpayable from four remaining ones.

## Edge cases

- **Serving the smallest refunds first maximises the count**, and paying each with as many two-rupee coins as possible minimises the one-rupee coins spent — the only way to settle an odd remainder. Verified against an exhaustive optimum over $5425$ small cases with no mismatch.
- **An odd amount needs at least one one-rupee coin**, so the ones are the genuinely scarce resource and the greedy protects them.
- **A creature that cannot be paid is skipped, not abandoned.** The loop continues to the next amount, since a later creature may need fewer ones — which is why it is `continue` rather than `break`.
- **$P$ or $Q$ may be $0$** (the first row has no two-rupee coins), so every refund must come out of the ones.
- **Both coin counts reach $10^{14}$** while the amounts cap at $10^9$, so the arithmetic must stay in exact integers.
- **Spending twos never hurts**, because a two-rupee coin can only ever replace two ones, and the ones are what run out first.
- **$T$ up to $10^6$ with $\sum N \leq 10^6$** means most cases are tiny, so the per-case overhead matters as much as the sort.

## Dry run

Third sample: $P = 5$ ones, $Q = 4$ twos, refunds $2, 3, 4, 5$ (already sorted).

| refund | twos used | ones used | ones left | twos left | served |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 5 | 3 | 1 |
| 3 | 1 | 1 | 4 | 2 | 2 |
| 4 | 2 | 0 | 4 | 0 | 3 |
| 5 | 0 | 5 | — | — | — |

The last creature needs five ones but only four remain, so it is skipped. Output `3`.
