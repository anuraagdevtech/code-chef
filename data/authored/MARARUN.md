---
topic: Conditionals & Case Work
subtopic: Largest achievable tier
time: $O(1)$ per test case
space: $O(1)$
---
Over $D$ days at $d$ km per day, Chef can cover at most $D \cdot d$ kilometres. Since prizes satisfy $A < B < C$, longer categories always pay more, so Chef should enter the **longest category he can finish**:

- $D \cdot d \geq 42$ → prize $C$
- $D \cdot d \geq 21$ → prize $B$
- $D \cdot d \geq 10$ → prize $A$
- otherwise → $0$

Testing from the longest distance downward means each branch may assume the longer ones failed, so only a lower bound is needed per tier.

The guarantee $A < B < C$ is what licenses the greedy. Without it — if a shorter race paid more — Chef would have to compare prizes rather than distances, and the ladder would need to check all affordable tiers and take the maximum prize.

The rule that one person cannot enter multiple categories is what keeps this a single choice rather than a packing problem; otherwise Chef might split his distance across several races.

Sample case 3 is the discriminating one: $10 \times 3 = 30$ km clears $21$ but falls short of $42$, so the answer is $B = 2$ rather than $C$. Sample case 1 covers just $1$ km and wins nothing, which is why the explicit $0$ branch is needed — the constraints allow $D \cdot d$ as low as $1$.

The maximum reach is $D \cdot d \leq 10 \times 5 = 50$, so the $42$ km tier is attainable but only just.

## Edge cases

- **Below every threshold** (a total of $1$ km): no prize at all, so $0$ — a case the ladder needs an explicit final branch for.
- **Exactly on a threshold** ($10$, $21$ or $42$): qualifies for that tier, so the comparisons are non-strict. The second sample row sits exactly on $10$.
- **The longest race he can finish is always the best**, because $A < B < C$ is guaranteed — so there is no need to compare prize values, only distances.
- **Largest total** ($D = 10$ days at $d = 5$ km, so $50$): clears $42$ and takes $C$.
- The bands must be tested from the top down; ascending tests with the first match winning would hand out the smallest prize instead of the largest.

## Dry run

| $D$ | $d$ | total | tier reached | prize | output |
|---:|---:|---:|---|---:|---|
| 1 | 1 | 1 | none | 0 | `0` |
| 10 | 1 | 10 | $\geq 10$ | $A = 1$ | `1` |
| 10 | 3 | 30 | $\geq 21$ | $B = 2$ | `2` |

Row 2 lands exactly on the first threshold.
