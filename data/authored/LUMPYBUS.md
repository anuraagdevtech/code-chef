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
