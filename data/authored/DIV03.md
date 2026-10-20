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
