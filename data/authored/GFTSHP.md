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
