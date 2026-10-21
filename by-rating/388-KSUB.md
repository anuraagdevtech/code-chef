# 388. K-Subarrays

> [`KSUB`](https://www.codechef.com/problems/KSUB) &middot; difficulty **1663** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Earliest cut maximises the number of GCD-$G$ pieces |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Algorithms`, `Basic Math`, `GCD`, `Greedy` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log A)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an array $A$ of $N$ **positive** integers. Let $G$ be the [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor) of all the numbers in the array $A$.

You have to find if there exist $K$ **non-empty**, **non-intersecting** subarrays of $A$ for which the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of the gcd of those $K$ subarrays equals $G$.

Formally, let $g_1, g_2, \ldots, g_K$ be the gcd of those $K$ chosen subarrays, then, $\frac{(g_1 + g_2 + .... + g_K)}{K} = G$ should follow.

If there exist $K$ such subarrays, output `YES`, otherwise output `NO`.

Note: Two subarrays are non-intersecting if there exists no index $i$, such that, $A_i$ is present in both the subarrays.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers — the number of integers in the array $A$ and the integer $K$, respectively.
    - The next line contains $N$ space-separated positive integers $A_1, A_2, \ldots, A_N$, the elements of the array $A$.

**Output**

For each test case, if there exist $K$ such subarrays, output `YES`, otherwise output `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot {10}^5$
- $1 \leq K \leq N$
- $1 \leq A_i \leq 2 \cdot {10}^5$
- The sum of $N$ over all test cases won't exceed $4 \cdot {10}^5$.

## Sample

**Sample input**

```
4
6 4
2 2 3 3 2 2
1 1
1
5 3
1 2 3 4 5
4 3
6 12 18 24
```

**Sample output**

```
NO
YES
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** It is impossible to find $4$ non-empty, non-intersecting subarrays which satisfy the given condition.

**Test case $2$:** There is only one element in the array. Here, $G = 1$ and, for the subarray $[1]$, $g = 1$. Thus, it is possible to satisfy the conditions.

**Test case $3$:** Here, $G = gcd(1,2,3,4,5) = 1$. We can choose $3$ non-empty, non-intersecting subarrays $\{[1], [2,3], [4,5]\}$ where $gcd(1) = 1$, $gcd(2,3) = 1$, and $gcd(4,5) = 1$. Thus, the arithmetic mean = $\frac{(1 + 1 + 1)}{3} = 1$. Hence, we can have $3$ such subarrays.

**Test case $4$:** It is impossible to find $3$ non-empty, non-intersecting subarrays which satisfy the given condition.

</details>

## Approach

$G$ divides every element, so the GCD of **any** subarray is a multiple of $G$ and hence at least $G$. An average of values each $\geq G$ equals $G$ only if they are *all* exactly $G$. So the arithmetic-mean condition is not an averaging problem at all — it demands

$$g_1 = g_2 = \cdots = g_K = G$$

and the question becomes: can we find $K$ disjoint subarrays each with GCD exactly $G$? Equivalently, is the maximum number of such disjoint subarrays at least $K$?

That maximum comes from a greedy sweep: run a running GCD from left to right and **cut as soon as it reaches $G$**, then reset. Cutting at the earliest possible point is optimal because a GCD only shrinks as a subarray grows, so any solution's first piece can be shortened to the greedy's first piece without affecting the rest — the classic exchange argument for interval packing.

Leftover elements at the end are simply discarded; the subarrays need not cover the array.

The samples separate the two outcomes. $[1,2,3,4,5]$ has $G = 1$ and the greedy cuts at $[1]$, $[2,3]$, $[4,5]$ — three pieces, enough for $K = 3$. But $[2,2,3,3,2,2]$ also has $G = 1$ and yields only two pieces, $[2,2,3]$ and $[3,2]$, falling short of $K = 4$: the twos cannot reach GCD $1$ on their own.

The last sample shows the same with a larger $G$: $[6,12,18,24]$ has $G = 6$, and only $[6]$ and $[12,18]$ qualify before the trailing $24$ is stranded, so $K = 3$ is impossible.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        vals = [int(x) for x in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        whole = 0
        for v in vals:
            whole = gcd(whole, v)
        pieces = 0
        run = 0
        for v in vals:
            run = gcd(run, v)
            if run == whole:      # cut at the earliest chance and reset
                pieces += 1
                run = 0
        out.append("YES" if pieces >= k else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/KSUB.md](../docs/greedy/KSUB.md)
