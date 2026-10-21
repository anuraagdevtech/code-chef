# 454. Find an integer

> CodeChef problem code [`SUMDIV2`](https://www.codechef.com/problems/SUMDIV2) &middot; difficulty **1714** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Simultaneous congruences solved by inspection |
| **Time** | $O(\log \min(X,Y))$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has two nephews who love integers $X$ and $Y$. An integer $N$ is *awesome* if the following conditions hold:
- $1 \leq N \leq 10^{18}$
- $(N+Y)$ is divisible by $X$.
- $(N+X)$ is divisible by $Y$.

Find **any** awesome integer $N$. We can prove that under the given constraints, an answer always exists.

Note that you do **not** have to minimize the answer.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input.
    - The first line of each test case contains two space-separated integers $X$ and $Y$ — favourite numbers of Chef's nephews.

**Output**

For each test case, output an awesome integer. If there are several answers, you may print any of them.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X, Y \leq 10^9$

## Sample

**Sample input**

```
3
18 42
1 1
100 200
```

**Sample output**

```
192
5
500
```

<details><summary>Explanation</summary>

**Test Case 1:** In this case, $N = 192$ is an awesome integer because:
- $1 \le 192 \le 10^{18}$
- $192 + 18 = 210$ is divisible by $42$
- $192 + 42 = 234$ is divisible by $18$

**Test Case 2:** We can output any positive integer $N$ such that $(1 \le N \le 10^{18})$ because $N + 1$ is divisible by $1$ for all such $N$.

</details>

## Approach

The two divisibility conditions are congruences:

$$N \equiv -Y \pmod X, \qquad N \equiv -X \pmod Y$$

One solution can be read off directly: $N = XY - X - Y$. Reducing mod $X$, both $XY$ and $X$ vanish and $-Y$ remains; reducing mod $Y$, both $XY$ and $Y$ vanish and $-X$ remains. So the conditions are consistent and the solution set is the full arithmetic progression

$$XY - X - Y + t \cdot \mathrm{lcm}(X, Y)$$

since adding the LCM preserves both congruences.

That progression is what fixes the two range problems. $XY - X - Y$ can be non-positive — it is $-1$ for $X = Y = 1$ and $0$ for $X = Y = 2$ — so reduce it modulo $L = \mathrm{lcm}(X,Y)$ into $[0, L)$ and, if the result is $0$, step up to $L$ itself. The answer is then the smallest positive solution, which is at most $L \leq XY \leq 10^{18}$ and so always in range.

Computing the LCM as $X/\gcd(X,Y) \cdot Y$ keeps the intermediate value from exceeding the bound.

Any answer is accepted. For $X = 18, Y = 42$ the LCM is $126$ and $XY - X - Y = 696$ reduces to $66$: indeed $66 + 42 = 108 = 6 \cdot 18$ and $66 + 18 = 84 = 2 \cdot 42$. The sample's $192$ is $66 + 126$, the next term of the same progression. For $X = Y = 1$ the reduction gives $0$, so we print $1$.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        lcm = x // gcd(x, y) * y
        # XY - X - Y solves both congruences; shift it into (0, lcm].
        n = (x * y - x - y) % lcm
        out.append(str(n if n else lcm))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log \min(X,Y))$ per test case
- **Space:** $O(1)$
