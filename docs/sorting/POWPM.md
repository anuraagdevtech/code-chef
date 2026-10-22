[&larr; 405. Concat Sort](CONCATSORT.md) &middot; [Index](../../README.md) &middot; [469. Pokemon Battles &rarr;](PBATTLE.md)

# 421. Powered Parameters

> CodeChef problem code [`POWPM`](https://www.codechef.com/problems/POWPM) &middot; difficulty **1673** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Bounding the exponent, then counting by integer root |
| **Time** | $O(N \log N + 30 \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array $A$ containing $N$ integers.
Count the number of **ordered pairs** $(i, j)$ such that:
- $1 \leq i, j \leq N$, and
- $A_i^j \leq A_j$
That is, $A_i$ raised to the power $j$ doesn't exceed $A_j$.

Note that we're counting ordered pairs, meaning the pair $(1, 2)$ is *different* from the pair $(2, 1)$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**

For each test case, output on a new line the number of ordered pairs $(i, j)$ that satisfy the given condition.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
3
2 3 4
4
2 7 2 3
5
1000 100 1 10 1
```

**Sample output**

```
1
4
14
```

<details><summary>Explanation</summary>

**Test case $1$:** The only valid pair is $(1, 1)$, since $A_i^j = 2^1 \leq 2 = A_j$.
$(1, 3)$ is an invalid pair for example, since $A_i^j = 2^3 = 8 \gt 4 = A_j$. The same can be verified for all the other pairs.

**Test case $2$:** The valid pairs are $(1, 1), (1, 2), (3, 1), (3, 2)$.

**Test case $3$:** The valid pairs are:
$(1, 1),$
$(2, 1),$
$(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),$
$(4, 1), (4, 2),$
$(5, 1), (5, 2), (5, 3), (5, 4), (5, 5).$

</details>

## Approach

Two observations shrink the $N^2$ pair space to almost nothing.

**Ones are free.** If $A_i = 1$ then $A_i^j = 1 \leq A_j$ for every $j$, since all values are positive. So each index holding a $1$ contributes $N$ pairs outright.

**Otherwise the exponent is tiny.** If $A_i \geq 2$ then $A_i^j \geq 2^j$, and the condition forces $2^j \leq A_j \leq 10^9$, so $j \leq 29$. Only the first $30$ indices can ever be the second element of a pair — the rest of the array is irrelevant as a $j$.

For each such $j$, the condition $A_i^j \leq A_j$ with $A_i \geq 2$ is just $A_i \leq \lfloor A_j^{1/j} \rfloor$. So sort a copy of $A$ once and answer each $j$ with a binary search:

$$\text{answer} = c_1 \cdot N + \sum_{j=1}^{\min(N,30)} \Bigl(\#\{\,i : 2 \leq A_i \leq \lfloor A_j^{1/j} \rfloor\,\}\Bigr)$$

where $c_1$ is the number of ones. Compute the root with an integer routine and correct it by stepping, since `a ** (1/j)` in floating point is off by one near exact powers and would silently miscount.

The third sample is the one that shows both parts. $A = [1000, 100, 1, 10, 1]$ has two ones, contributing $2 \cdot 5 = 10$ pairs. Then $j = 1$ admits $A_i \leq 1000$, i.e. all three non-one values, and $j = 2$ admits $A_i \leq \lfloor\sqrt{100}\rfloor = 10$, i.e. just the $10$. Total $10 + 3 + 1 = 14$.

Note $(i,j)$ with $i = j$ is allowed, which is where $j = 1$ picking up $A_1$ itself comes from in the first sample.

## Solution (Python)

```python
import sys
from bisect import bisect_right


def iroot(a: int, j: int) -> int:
    """Largest r with r**j <= a."""
    if j == 1:
        return a
    r = int(round(a ** (1.0 / j)))
    while r > 1 and r ** j > a:
        r -= 1
    while (r + 1) ** j <= a:
        r += 1
    return r


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        ordered = sorted(a)
        ones = bisect_right(ordered, 1)
        total = ones * n                  # A_i = 1 pairs with every j
        # A_i >= 2 forces 2^j <= 10^9, so only j <= 29 can ever work.
        for j in range(1, min(n, 30) + 1):
            limit = iroot(a[j - 1], j)
            if limit >= 2:
                total += bisect_right(ordered, limit) - ones
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N + 30 \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **$A_i = 1$ pairs with every $j$**, since $1^j = 1 \leq A_j$ for all $A_j \geq 1$ — contributing $(\text{count of ones}) \times N$ before any root is taken.
- **For $A_i \geq 2$ only $j \leq 29$ can work**, because $2^j \leq A_j \leq 10^9$ bounds the exponent — which is what keeps the loop at $30$ iterations instead of $N$.
- **The exponent is the *index* $j$, not a value**, so the bound comes from the position; `a[j - 1]` reads $A_j$ from the original array while the sorted copy serves the counting.
- **The integer root must be exact.** `round(a ** (1.0/j))` can land one off for large $a$, so it is corrected by stepping down while $r^j > a$ and up while $(r+1)^j \leq a$.
- **A limit below $2$ means no $A_i \geq 2$ qualifies**, which the `if limit >= 2` guard skips — otherwise the ones would be double-counted.
- **Ordered pairs are counted**, so $(1,2)$ and $(2,1)$ are distinct and $i = j$ is allowed.
- **Sum of $N \leq 2 \cdot 10^5$**: one sort plus $30$ binary searches per case.

## Dry run

Third sample: $A = 1000, 100, 1, 10, 1$, sorted to $1, 1, 10, 100, 1000$ with two ones.

| contribution | count |
|---|---:|
| ones paired with every $j$ ($2 \times 5$) | 10 |
| $j = 1$: $A_i \leq \sqrt[1]{1000} = 1000$, excluding ones | 3 |
| $j = 2$: $A_i \leq \sqrt{100} = 10$, excluding ones | 1 |
| $j = 3, 4, 5$: limits are $1$, so nothing | 0 |

Total `14`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#392 of 486): [../../by-rating/392-POWPM.md](../../by-rating/392-POWPM.md)
