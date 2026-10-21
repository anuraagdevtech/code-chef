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

## Edge cases

- **Only the bus count needs searching.** Once it is fixed, the leftover people must all go by car, so the car count is forced at $\lceil \text{rest}/4 \rceil$ — one variable, not two.
- **The last bus may run under-filled.** The third row puts $100$ of $105$ people on one bus and the other five in two cars, which beats both all-car and two-bus options.
- **More than $\lceil N/100 \rceil$ buses can never help**, which bounds the loop at eleven iterations; `max(0, …)` keeps the remainder non-negative at that last step.
- **Cars round up too**: nine people need three cars, not two and a quarter.
- **Either mode can win outright** — the first row takes no buses at all, the second takes no cars.
- **$N, X, Y \leq 1000$** keeps every candidate cost small, so the brute force is comfortably within budget at $T = 1000$.

## Dry run

Third sample: $N = 105$, bus cost $X = 80$, car cost $Y = 10$.

| buses | carried by bus | rest | cars $\lceil \text{rest}/4 \rceil$ | cost |
|---:|---:|---:|---:|---:|
| 0 | 0 | 105 | 27 | 270 |
| 1 | 100 | 5 | 2 | **100** |
| 2 | 200 | 0 | 0 | 160 |

Output `100`.
