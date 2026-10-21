---
topic: Prefix Sums
subtopic: Prefix sums with a single discount
time: $O(N \log N)$ per test case
space: $O(N)$
---
Two greedy choices, then a scan.

**For a fixed count $m$, buy the $m$ cheapest items.** Any other selection of $m$ items costs at least as much, so sorting ascending and taking a prefix is optimal.

**Apply the coupon to the most expensive item bought.** The coupon turns a cost $X$ into $\lceil X/2 \rceil$, saving $\lfloor X/2 \rfloor$ — an increasing function of $X$. So within the chosen prefix the saving is maximised on its largest element, which after sorting is the last one.

So the cost of buying the $m$ cheapest is

$$\text{prefix}(m) - \left\lfloor \frac{A_{m-1}}{2} \right\rfloor$$

and the answer is the largest $m$ whose cost fits in $K$. A single sweep over $m$ with a running prefix sum does it in $O(N)$ after the sort.

Note the cost is **not monotonic in a way that permits binary search without care** — but it is, in fact, non-decreasing in $m$ here, since adding an item adds at least $\lceil A/2 \rceil \geq 0$. The linear scan sidesteps the question entirely and is fast enough.

Sample case 3 is the one that exercises the discount placement: with $K = 10$ and prices $[4,6,7]$, buying two costs $4 + 6 = 10$ less $\lfloor 6/2 \rfloor = 3$, so $7$ — affordable. Buying all three costs $17 - 3 = 14$, too much. The answer is $2$.

The rounding is **up** for what Chef pays, so the saving is the floor. Writing the saving as `a // 2` keeps it exact; computing `ceil(x/2)` through floats would be the fragile route at $A_i$ up to $10^9$.

## Edge cases

- **The coupon belongs on the dearest item in the chosen set**, which after sorting is the one just added — so the discount is $\lfloor a_{m-1}/2 \rfloor$ and not $\lfloor a_0/2 \rfloor$. Halving the cheapest item instead fails the third sample row.
- **The discount floors**, so an odd price loses the half: a price of $5$ saves only $2$, which is exactly what the first row turns on ($5 - 2 = 3 \leq 4$).
- **Buying the cheapest items first maximises the count**, so sorting comes before anything else.
- **The early `break` is sound** because the discounted cost is non-decreasing in $m$: adding item $m$ raises it by $\lceil a_m/2 \rceil + \lfloor a_{m-1}/2 \rfloor \geq 0$, so once the budget is exceeded it stays exceeded.
- **$K = 0$**: nothing is affordable, since $A_i \geq 1$ leaves every discounted price at $1$ or more, so the answer is $0$.
- **The coupon is optional but never harmful**, so it is always spent — there is no case where declining it buys more.

## Dry run

Third sample: $K = 10$, prices $6, 7, 4$ sorted to $4, 6, 7$.

| $m$ | items | raw prefix | coupon on dearest | cost | $\leq 10$? | best |
|---:|---|---:|---:|---:|:---:|---:|
| 1 | $4$ | 4 | $-2$ | 2 | yes | 1 |
| 2 | $4, 6$ | 10 | $-3$ | 7 | yes | 2 |
| 3 | $4, 6, 7$ | 17 | $-3$ | 14 | **no** | 2 |

Output `2`.
