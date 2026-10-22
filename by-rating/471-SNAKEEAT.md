[&larr; 470. ChefTown Parade](470-CHEFTOWN.md) &middot; [Index](README.md) &middot; [472. Chef and Good Subsequences &rarr;](472-GDSUB.md)

# 471. Snake Eating

> [`SNAKEEAT`](https://www.codechef.com/problems/SNAKEEAT) &middot; difficulty **1940** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Feasibility check with prefix sums |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((N + Q) \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

The Chef has acquired a vicious bunch of snakes, and these snakes are ever hungry and end up eating each other. In particular, each snake i has a length **L_i**, whose initial value is given to you. A snake can eat any other snake which is not longer than itself. That is, snake i can eat snake j (i ≠ j), if **L_i** ≥ **L_j**. And when a snake eats another snake, its length increases by 1. That is, **L_i** increases by 1. A snake can eat multiple other snakes.

The Chef doesn't care about snakes eating each other. All he wants is to have as many snakes as possible, which are at least some particular lengths long. You are given **Q** values: **K_1, K_2, .., K_Q**. Treat each of them independently and output the answer for each. That is, for each **K_i**, assume that you start out from the beginning with all the snakes alive and the lengths as the initial values given in the input, and find out the maximum number of snakes you can get whose length is at least **K_i**.

**Input**

- The first line contains an integer **T**, which is the number of testcases. The description of each testcase follows.

- The first line of each testcase contains two integers: **N** and **Q**, which denote the number of snakes initially, and the number of queries, respectively.

- The second line contains **N** space separated integers: **L_1, L_2, .., L_N**, the initial lengths of the snakes.

- The i-th of the next **Q** lines contains a single integer, **K_i**.

**Output**

- For each testcase, output **Q** lines, the i-th of which should have a single integer: The maximum number of snakes the Chef can get which are of length at least **K_i**.

**Constraints**

- 1 ≤ **T** ≤ 5

- 1 ≤ **N, Q** ≤ 10^5

- 1 ≤ **L_i** ≤ 10^9

- 1 ≤ **K_i** ≤ 10^9

**Explanation**

## Constraints

- 1 ≤ T ≤ 5
- 1 ≤ N, Q ≤ 10^5
- 1 ≤ L_i ≤ 10^9
- 1 ≤ K_i ≤ 10^9

## Sample

**Sample input**

```
2
5 2
21 9 5 8 10
10
15
5 1
1 2 3 4 5
100
```

**Sample output**

```
3
1
0
```

<details><summary>Explanation</summary>

In the first testcase, first query, the second snake (length 9) can eat the fourth snake (length 8), and hence make its length 10. Now, there are four snakes left, and their lengths are {21, 10, 5, 10}. So, we have three snakes with length ? 10: Two snakes of length 10 and one snake of length 21. This is the best you can do.

In the second query, no matter what happens, you cannot get more than one snake of length ? 15.

In the second testcase, no matter what happens, you cannot get any snake of length ? 100. Hence the answer is 0.

</details>

## Approach

Suppose we aim to end with $m$ snakes of length at least $K$. Two greedy choices are forced.

**Keep the $m$ longest.** They start closest to the target, so any other choice needs at least as much feeding.

**Feed them the $N - m$ shortest.** Each snake eaten adds exactly $1$ to its eater, so the sacrifices are interchangeable — only their *count* matters.

So after sorting, the kept snakes are the suffix $L[N-m \ldots N-1]$, and the total feeding needed is the sum of their shortfalls:

$$\text{deficit}(m) = \sum_{i=N-m}^{N-1} \max(0,\ K - L_i)$$

which must not exceed the $N - m$ available meals.

As $m$ grows the deficit rises while the supply falls, so feasibility is **monotone** — binary search on $m$ answers each query in $O(\log N)$.

The deficit itself is computed in $O(\log N)$ rather than $O(m)$: binary search for the first index whose length already reaches $K$, then take a prefix-sum slice of everything below it. Without that, the queries would be $O(NQ)$ overall.

The eating rule $L_i \geq L_j$ is automatically respected, since every kept snake is at least as long as every sacrificed one.

Sample case 1 with $K = 10$ keeps $[9,10,21]$: only the $9$ falls short, by $1$, and two meals are available — so $3$ snakes. Pushing to $m = 4$ would need $3$ meals with only $1$ left. At $K = 15$ even $m = 2$ needs $5$ meals against $3$, so the answer drops to $1$.

Sample case 2 asks for length $100$ from snakes topping out at $5$, needing $95$ meals from four — so $0$.

## Solution

```python
import sys
from bisect import bisect_left


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        lengths = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        prefix = [0] * (n + 1)
        for i, v in enumerate(lengths):
            prefix[i + 1] = prefix[i] + v
        for i in range(q):
            k = int(data[pos + i])
            # First index already long enough; everything before it is short.
            short_end = bisect_left(lengths, k)

            def feasible(m):
                lo = n - m
                hi = min(short_end, n)          # kept snakes below k
                if lo >= hi:
                    return True
                need = k * (hi - lo) - (prefix[hi] - prefix[lo])
                return need <= n - m

            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if feasible(mid):
                    lo = mid
                else:
                    hi = mid - 1
            out.append(str(lo))
        pos += q
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Keeping the longest snakes is optimal**, so for a target count $m$ the survivors are the top $m$ after sorting — and everything else becomes food.
- **The feasibility check is a prefix sum.** Among the survivors, those still below $K$ need $K - L_i$ feeds each, and the total must not exceed the $n - m$ snakes available as food.
- **The predicate is monotone in $m$** — fewer survivors means more food and less demand — so the answer is binary searched.
- **Survivors already at or above $K$ need nothing**, which is why the demand is summed only over the prefix below $K$, found by one `bisect_left`.
- **An unreachable $K$ gives $0$.** The second sample asks for length $100$ from snakes of length at most $5$; even one survivor would need $95$ feeds against four available, so no snake qualifies.
- **A feed gives exactly $+1$**, so the demand is linear in the shortfall and no scheduling subtlety arises.
- **$L_i$ and $K$ reach $10^9$ with $n$ at $10^5$**, so the demand can reach $10^{14}$ — past 32-bit.

## Dry run

First query of the first sample: lengths sorted to $5, 8, 9, 10, 21$ with $K = 10$.

| survivors $m$ | kept snakes | those below $10$ | feeds needed | food available | feasible? |
|---:|---|---|---:|---:|:---:|
| 3 | $9, 10, 21$ | just the $9$ | 1 | 2 | yes |
| 4 | $8, 9, 10, 21$ | $8$ and $9$ | $2 + 1 = 3$ | 1 | no |

So `3` snakes can reach length $10$.

---

Same problem grouped by topic: [../docs/binary-search/SNAKEEAT.md](../docs/binary-search/SNAKEEAT.md)
