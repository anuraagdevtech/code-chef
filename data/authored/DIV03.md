---
topic: Greedy
subtopic: Spending a budget from the top down
time: $O(1)$ per test case — ten fixed difficulties
space: $O(1)$
---
To make the hardest remaining problem as easy as possible, delete problems from the **top** difficulty downward. Any deletion spent on an easier problem is wasted, since it cannot lower the maximum while harder problems survive.

So walk difficulties $10, 9, \ldots, 1$ with a budget of $K$:

- if the whole tier fits in the budget, erase it and continue;
- otherwise the budget runs out mid-tier, that tier keeps at least one problem, and it is the answer.

The greedy is optimal because the maximum difficulty is determined solely by the hardest surviving tier, and clearing tiers from the top is the only way to reduce it.

The guarantee $K < \sum A_i$ matters: at least one problem always survives, so the scan is certain to find an answer and no empty case arises.

**Empty tiers must be skipped, not treated as answers.** A tier with $A_i = 0$ costs nothing to "clear" and cannot be the maximum. Sample case 4 is exactly this: with $K = 10$ the $10$ problems of difficulty $10$ are erased, difficulties $9$ down to $4$ are already empty, and the answer is the next non-empty tier, $3$.

Sample case 3 has $K = 0$, so nothing is deleted and the answer is just the hardest non-empty tier, $8$. Sample case 5 spends a large budget sweeping down to difficulty $2$, which survives with $9$ of its $10$ problems.

With $A_i$ up to $10^8$ the totals reach $10^9$, fine for Python and just inside 32 bits elsewhere. The fixed ten tiers make each test case constant time, which matters at $T = 2 \times 10^4$.

## Edge cases

- **Empty tiers must be skipped without becoming the answer.** Cases $2$ and $4$ both have runs of zeros between the tier that gets cleared and the tier that survives; without the `continue` on a zero count, the answer would be reported as an empty difficulty.
- **$K = 0$** (case $3$): nothing is removed, and the answer is simply the hardest non-empty tier, $8$.
- **Exactly clearing a tier** (case $4$, where $K = 10$ matches the ten problems at difficulty $10$) moves on to the next non-empty tier, which becomes the answer.
- **Removing from the top down is forced**, because the answer is the *maximum* remaining difficulty: deleting anything easier leaves that maximum untouched and wastes the budget.
- **$K <$ the total is guaranteed**, so at least one problem always survives and the loop always halts at a tier it cannot clear — the `answer = 1` initialiser never actually fires.
- **The ten counts are a fixed-length record**, so each case consumes exactly $11$ tokens; a variable-length read would desynchronise the stream.

## Dry run

Second sample: counts $2, 0, 1, 0, 0, 0, 0, 0, 0, 10$ for difficulties $1$ through $10$, with $K = 12$.

| difficulty | count | action | $K$ left |
|---:|---:|---|---:|
| 10 | 10 | clear it | 2 |
| 9…4 | 0 | skip (empty) | 2 |
| 3 | 1 | clear it | 1 |
| 2 | 0 | skip (empty) | 1 |
| 1 | 2 | **cannot clear** | — |

Output `1`.
