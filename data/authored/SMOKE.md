---
topic: Brute Force
subtopic: Searching one variable over a small range
time: $O(N/100)$ per test case — at most 11 iterations
space: $O(1)$
---
Two vehicle types with different capacities and different costs, so the cheaper **per person** is not always the right choice — the last vehicle is usually part-empty, and that waste can flip the comparison.

Since $N \leq 1000$, at most $\lceil N/100 \rceil \leq 10$ buses are ever useful. So fix the bus count $b$ from $0$ upward, carry the rest by car, and take the best:

$$\min_{0 \leq b \leq \lceil N/100 \rceil} \left( bX + \left\lceil \frac{\max(0,\ N - 100b)}{4} \right\rceil Y \right)$$

Eleven evaluations settle it, with no case analysis about which vehicle is better value.

The samples show all three regimes. Case 1 ($N=9$) uses cars only: three cars at $8$ beat one bus at $40$. Case 2 ($N=15$) uses a bus only: one bus at $20$ beats four cars at $20$ each. Case 3 ($N=105$) **mixes**: one bus plus two cars costs $80 + 20 = 100$, beating both two buses ($160$) and twenty-seven cars ($270$).

That mixed case is the reason to search rather than reason. A greedy "fill buses first, then cars" happens to be right here, but "pick whichever is cheaper per seat" is not — cars are cheaper per seat in case 3 ($2.5$ against $0.8$ per person for the bus), yet the answer still uses a bus.

The clamp at zero matters for the last bus, which may carry fewer than $100$ people; without it the car count would go negative.
