# 211. Gift Shop and Coupon

> CodeChef problem code [`GFTSHP`](https://www.codechef.com/problems/GFTSHP) &middot; difficulty **1364** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Prefix sums with a single discount |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef wants to impress Chefina by giving her the maximum number of gifts possible.

Chef is in a gift shop having $N$ items where the cost of the $i^{th}$ item is equal to $A_{i}$.
Chef has $K$ amount of money and a $50 \%$ off discount coupon that he can use for **at most one** of the items he buys.

If the cost of an item is equal to $X$, then, after applying the coupon on that item, Chef only has to pay ${\bf \left\lceil \frac{X}{2} \right\rceil}$ (rounded up to the nearest integer) amount for that item.

Help Chef find the **maximum number** of items he can buy with $K$ amount of money and a $50 \%$ discount coupon given that he can use the coupon on **at most one** item.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The next line contains $N$ space-separated integers, where the $i^{th}$ integer $A_{i}$ denotes the cost of the $i^{th}$ item.

**Output**

For each test case, print a single line containing one integer ― the **maximum number** of items Chef can buy.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_{i} \leq 10^9$
- $0 \leq K \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2\cdot10^5$.

## Sample

**Sample input**

```
3
1 4
5
3 15
4 4 5
3 10
6 7 4
```

**Sample output**

```
1
3
2
```

<details><summary>Explanation</summary>

**Test case $1$:** After applying the discount, Chef can buy the only available item at ${\left\lceil \frac{5}{2} \right\rceil} = 3$.

**Test case $2$:** Chef can buy all three items even without using the coupon.

**Test case $3$:** After applying coupon on the third item, Chef can buy the second and the third item at $7 + {\left\lceil \frac{4}{2} \right\rceil} = $ $ 7 + 2 = 9$.
It is not possible for Chef to buy more than two items.

</details>

## Approach

Two greedy choices, then a scan.

**For a fixed count $m$, buy the $m$ cheapest items.** Any other selection of $m$ items costs at least as much, so sorting ascending and taking a prefix is optimal.

**Apply the coupon to the most expensive item bought.** The coupon turns a cost $X$ into $\lceil X/2 \rceil$, saving $\lfloor X/2 \rfloor$ — an increasing function of $X$. So within the chosen prefix the saving is maximised on its largest element, which after sorting is the last one.

So the cost of buying the $m$ cheapest is

$$\text{prefix}(m) - \left\lfloor \frac{A_{m-1}}{2} \right\rfloor$$

and the answer is the largest $m$ whose cost fits in $K$. A single sweep over $m$ with a running prefix sum does it in $O(N)$ after the sort.

Note the cost is **not monotonic in a way that permits binary search without care** — but it is, in fact, non-decreasing in $m$ here, since adding an item adds at least $\lceil A/2 \rceil \geq 0$. The linear scan sidesteps the question entirely and is fast enough.

Sample case 3 is the one that exercises the discount placement: with $K = 10$ and prices $[4,6,7]$, buying two costs $4 + 6 = 10$ less $\lfloor 6/2 \rfloor = 3$, so $7$ — affordable. Buying all three costs $17 - 3 = 14$, too much. The answer is $2$.

The rounding is **up** for what Chef pays, so the saving is the floor. Writing the saving as `a // 2` keeps it exact; computing `ceil(x/2)` through floats would be the fragile route at $A_i$ up to $10^9$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        best = 0
        prefix = 0
        for m in range(1, n + 1):
            prefix += a[m - 1]
            # The coupon saves floor(x / 2), so spend it on the dearest item
            # in the prefix - which, sorted, is the one just added.
            if prefix - a[m - 1] // 2 <= k:
                best = m
            else:
                break
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

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

---

Same problem in rating order (#219 of 486): [../../by-rating/219-GFTSHP.md](../../by-rating/219-GFTSHP.md)
