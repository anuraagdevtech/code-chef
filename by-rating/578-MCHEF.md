[&larr; 577. K Distinct Array](577-DISTK.md) &middot; [Index](README.md) &middot; [579. Prime Factor Division &rarr;](579-PRIMEFACDIV.md)

# 578. MasterChef

> [`MCHEF`](https://www.codechef.com/problems/MCHEF) &middot; difficulty **2016** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Interval-minimum sweep and pruned removal knapsack |
| **Complexity class** | Interval sweep and budget DP $O((N+M) \log M + KB)$ |
| **Time** | $O((N+M)\log M+N\log K+KB)$ per test case with $B\le\min(N,\sum_{c=1}^{200}\lfloor K/c\rfloor)$ |
| **Space** | $O(N+M+K+B)$ |

## Question

Chef loves to prepare delicious dishes. He has prepared **N** dishes numbered from **1** to **N** for this year's MasterChef contest. He has presented all the **N** dishes to a panel of judges. Judging panel consists of **M** judges numbered from **1** to **M**. Rating for each dish was decided by voting from all the judges. Rating for the dishes has been given by a **1**-indexed array **A** where **A_i** denotes rating of the **i^th** dish.

Some dishes prepared by chef are extraordinary delicious, but unfortunately, some are not. Chef has been given a chance to improve the total rating of his dishes. By total rating of dishes, we mean the sum of the ratings of his dishes. Each of the **M** judges has administrative power to remove some (zero or more) dishes from a specified range. The **i^th** judge takes **C_i** rupees for removing each dish of Chef's choice from the dishes numbered from **L_i** to **R_i** (both inclusive). Once a dish is removed by any of the **M** judges it will not be considered for calculating total rating of the dishes. Chef has spent a large portion of his money preparing mouth watering dishes and has only **K** rupees left for now. Now chef is worried about maximizing total rating of his dishes by dropping some of the **N** dishes.

Please Help chef by finding the maximum total rating he can achieve such that the total expenditure does not exceed his budget of **K** rupees.

** Input **

- First line of input contains a single integer **T** denoting the number of test cases.

- First line of each test case contains three space separated integers **N**, **K** and **M** denoting the number of dishes prepared by chef, chef's budget, and number of judges in judging panel respectively.

- Next line of each test case contains **N** space separated integers where **i^th** integer denotes the rating received by the **i^th** dish.

- Next **M** lines of each test case contain three space separated integers each: **L**, **R** and **C**, where the integers in the **i^th** line denotes the value of **L_i**, **R_i** and **C_i** respectively.

**Output **

For each test case, print a single integer in a line corresponding to the answer.

** Constraints **

-  **1 ≤ T ≤ 10^5**

-  **1 ≤ N,M ≤ 10^5**

-  **1 ≤ K ≤ 500 **

-  **1 ≤ L_i ≤ R_i ≤ N**

-  **1 ≤ C_i ≤ 200**

-  **-10^9 ≤ A_i ≤ 10^9**

-  Sum of **N** and **M** over all test cases does not exceed **5*10^5**

** Subtasks : **

- **Subtask 1 :** Sum of all **N**'s across the test cases in a file does not exceed **5000**. Sum of all **M**'s is also at most **5000**. **(33 points)**.

- **Subtask 2 :** Sum of all **N**'s across the test cases in a file does not exceed **5*10^5**. Sum of all **M**'s is also at most **5*10^5**. **( 67 points )**.

## Constraints

-  1 ≤ T ≤ 10^5
-  1 ≤ N,M ≤ 10^5
-  1 ≤ K ≤ 500
-  1 ≤ L_i ≤ R_i ≤ N
-  1 ≤ C_i ≤ 200
-  -10^9 ≤ A_i ≤ 10^9
-  Sum of N and M over all test cases does not exceed 5*10^5

## Sample

**Sample input**

```
1
5 10 5
10 -2 -5 7 -10
1 1 5
2 4 10
4 4 12
3 4 10
1 5 15
```

**Sample output**

```
5
```

<details><summary>Explanation</summary>

- Chef can drop dish numbered 3^rd with rating -5 by paying 10 rupees to the 4^th judge, and get the maximum possible total rating of 5.

</details>

## Approach

Removing a nonnegative-rated dish cannot help. For each negative dish, find the cheapest judge covering its index: sort interval starts and maintain a heap ordered by removal price, lazily discarding intervals whose right endpoint has passed.

A removable negative dish becomes a 0-1 item with cost equal to that cheapest price and gain equal to the negated rating. For any cost $c$, at most $K//c$ such dishes can be removed. Keep only that many largest gains with a min-heap; every discarded gain is dominated by enough equally priced better dishes. Run ordinary descending-capacity knapsack over the retained items and add its best gain to the original total rating.

## Solution

```python
import sys
from heapq import heappush,heappop,heapreplace


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,budget,m = (int(next(tokens)) for _ in range(3))
        a = [int(next(tokens)) for _ in range(n)]
        intervals = []
        for _ in range(m):
            left,right,cost = (int(next(tokens)) for _ in range(3))
            intervals.append((left-1,right-1,cost))
        intervals.sort()
        active = []
        groups = {}
        index = 0
        for i,value in enumerate(a):
            while index < m and intervals[index][0] <= i:
                _,right,cost = intervals[index]
                heappush(active,(cost,right))
                index += 1
            while active and active[0][1] < i:
                heappop(active)
            if value >= 0 or not active:
                continue
            cost = active[0][0]
            if cost > budget:
                continue
            group = groups.setdefault(cost,[])
            gain = -value
            if len(group) < budget//cost:
                heappush(group,gain)
            elif gain > group[0]:
                heapreplace(group,gain)
        dp = [0]*(budget+1)
        for cost,group in groups.items():
            for gain in group:
                for capacity in range(budget,cost-1,-1):
                    dp[capacity] = max(dp[capacity],dp[capacity-cost]+gain)
        out.append(str(sum(a)+dp[budget]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- An uncovered negative dish cannot be removed.
- Never pay to remove a positive or zero rating.
- Overlapping judges use their minimum price.
- Equal-cost pruning preserves the optimum.

## Dry run

The sample begins with total zero. Budget ten can remove the dish rated minus five for ten rupees, giving final rating five; the minus-ten dish costs fifteen and is unaffordable.

---

Same problem grouped by topic: [../docs/dynamic-programming/MCHEF.md](../docs/dynamic-programming/MCHEF.md)
