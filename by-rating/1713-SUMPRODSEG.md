# 1713 &middot; Sum Product Segments

> CodeChef problem code [`SUMPRODSEG`](https://www.codechef.com/problems/SUMPRODSEG) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Every family shares a pivot, so the pair must be mixed |
| **CodeChef tags** | `Number Theory`, `Mathematics`, `Integer Factorisation` |
| **CodeChef category** | easy |
| **Time** | $O(\sqrt{Y})$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/SUMPRODSEG.md](../docs/number-theory/SUMPRODSEG.md)

## Question

A *segment* is a range of **non-negative** integers $L, L + 1, L + 2, \ldots, R$, denoted $[L, R]$ where $L \leq R$.

Chef has a set $S$ consisting of **all** segments $[L, R]$ such that either $L + R = X$ or $L\cdot R = Y$.

For example, if $X = 5$ and $Y = 6$, then Chef's set is $S = \{[0, 5], [1, 4], [1, 6], [2, 3]\}$.

Given the integers $X$ and $Y$, can you help Chef find two non-intersecting segments from his set $S$? If it is not possible to find two such non-intersecting segments, print $-1$. If there are multiple possible answers, you may output **any** of them.

**Note:** Two segments are said to be non-intersecting if they have no number in common. For example,
- $[1, 4]$ and $[10, 42]$ are non-intersecting
- $[1, 4]$ and $[3, 10]$ are intersecting since they have $3$ and $4$ in common.
- $[1, 4]$ and $[4, 6]$ are intersecting since they have $4$ in common.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space separated integers $X$ and $Y$.

**Output**

- If there are non-intersecting segments, then output two lines:
    - In the first line, output two space-separated integers $L_1, R_1$ denoting the first segment.
    - In the second line, output two space-separated integers $L_2, R_2$ denoting the second segment.
- If there are no such segments, print $-1$ on a single line.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq X, Y \leq 10^{12}$

## Sample

**Sample input**

```
3
4 24
1 1
3 30
```

**Sample output**

```
1 3
4 6
-1
5 6
0 3
```

<details><summary>Explanation</summary>

**Test case $1$:** $1+3 = 4$ and $4 \cdot 6 = 24$, so $[1, 3]$ and $[4, 6]$ are both valid segments. Clearly, they also don't intersect.

**Test case $2$:** When $X = Y = 1$, we have $S = \{[0, 1], [1, 1]\}$. The only two segments intersect with each other, so there is no answer.

</details>

## Approach

Two structural facts collapse the search.

**All sum-segments overlap.** A segment $[L, X-L]$ with $L \leq X-L$ straddles $X/2$, so every one of them contains both $\lfloor X/2 \rfloor$ and $\lceil X/2 \rceil$.

**All product-segments overlap.** A segment $[L, Y/L]$ with $L \leq Y/L$ straddles $\sqrt{Y}$, so every one contains $\lfloor \sqrt{Y} \rfloor$.

So a disjoint pair must take **one from each family**, and within each family we should take the segment best placed to get out of the other's way — which in both cases is the most balanced one. Let the sum-segment be $[\lfloor X/2 \rfloor, \lceil X/2 \rceil]$, the shortest one available, and consider the balanced factor pair $[\ell, Y/\ell]$ where $\ell$ is the **largest divisor of $Y$ at most $\sqrt{Y}$**. Two ways to separate them:

- product-segment entirely to the right: $\ell > \lceil X/2 \rceil$;
- product-segment entirely to the left: $Y/\ell < \lfloor X/2 \rfloor$.

If neither holds, no pair exists and the answer is $-1$: pushing the product-segment further right only shrinks $\ell$, and further left only grows $Y/\ell$, while widening the sum-segment only makes matters worse.

Enumerating divisors to $\sqrt{Y} = 10^6$ handles $Y \leq 10^{12}$.

The samples: $X{=}4, Y{=}24$ gives the sum-segment $[2,2]$ and the balanced pair $[4,6]$, which clears it on the right — the sample's `1 3` plus `4 6` is an equally valid answer. $X{=}3, Y{=}30$ gives $[1,2]$ and $[5,6]$. And $X{=}Y{=}1$ has only $[0,1]$ and $[1,1]$, which share the point $1$, so $-1$.

## Solution (Python)

```python
import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        lo, hi = x // 2, x - x // 2       # the shortest sum-segment
        # The most balanced factor pair is the one best able to clear it.
        small = 1
        for d in range(1, isqrt(y) + 1):
            if y % d == 0:
                small = d
        large = y // small
        if small > hi:
            out.append(f"{lo} {hi}")
            out.append(f"{small} {large}")
        elif large < lo:
            out.append(f"{small} {large}")
            out.append(f"{lo} {hi}")
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\sqrt{Y})$ per test case
- **Space:** $O(1)$
