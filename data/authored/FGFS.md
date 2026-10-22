---
topic: Greedy
subtopic: Independent activity selection per compartment
time: $O(N \log N)$ per test case
space: $O(N)$
---
Each customer insists on one compartment, so the compartments never interact: the problem **decomposes** into $K$ independent instances, and only the compartments that actually appear matter — which is what makes $K$ up to $10^9$ harmless.

Within a compartment, a customer occupies the half-open interval $[s_i, f_i)$, and two customers are compatible when their intervals do not overlap. Maximising the count is the classic **activity-selection** problem, solved by sorting on finishing time and taking each interval whose start is at or after the last accepted finish:

$$\text{accept } i \iff s_i \geq f_{\text{last}}$$

The exchange argument: among any optimal solution's intervals, replacing the first by the globally earliest-finishing one keeps it feasible, since that one ends no later and so blocks no more of the future. Induction does the rest.

Half-open intervals are the detail to get right — a customer leaving at $f$ frees the compartment *at* $f$, so the comparison is $\geq$, not $>$. The second sample turns on it: in compartment $2$, the customer $[100,200)$ is followed by $[200,300)$, which fits exactly, while $[150,500)$ would collide.

Grouping by compartment with a dictionary and sorting each group gives $O(N \log N)$ overall. Note $N$ may be $0$, in which case the answer is $0$ and no groups exist.

The first sample has three customers in three different compartments, so all three dine. The second has one in compartment $1$ and three in compartment $2$, of which two are compatible — total $3$.

## Edge cases

- **The compartments are completely independent**, since a customer insists on exactly one of them — so the problem splits into $K$ separate activity-selection instances.
- **Earliest finishing time first is the classic optimum** for each compartment, and sorting the tuples as $(f, s)$ makes that the natural order.
- **The intervals are half-open $[s, f)$**, so a customer may start exactly when the previous one leaves — which is why the test is `s >= free_at` rather than a strict inequality. The second sample row relies on it.
- **$K$ is read but never used**: only the compartments that actually appear matter, so a dictionary beats an array of size $K$ at $K \leq 10^9$.
- **$N$ may be $0$**, giving an answer of $0$ with no intervals to read.
- **A customer who finds the compartment busy simply leaves**, which is why rejecting one is free — the chef may disallow customers at will.
- **$s_i < f_i$ is guaranteed**, so no zero-length visit needs special thought.

## Dry run

Second sample: $N = 4$ customers.

| compartment | intervals (sorted by finish) | accepted |
|---:|---|---:|
| 1 | $[10, 100)$ | 1 |
| 2 | $[100, 200)$, $[200, 300)$, $[150, 500)$ | 2 |

In compartment $2$, the first two chain exactly at time $200$; the third starts at $150$, which is already busy. Total `3`.
