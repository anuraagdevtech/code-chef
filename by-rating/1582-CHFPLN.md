# 1582 &middot; Chef In Infinite Plane

> CodeChef problem code [`CHFPLN`](https://www.codechef.com/problems/CHFPLN) &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Capacity per value |
| **CodeChef category** | main |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/combinatorics/CHFPLN.md](../docs/combinatorics/CHFPLN.md)

## Question

Chef has an integer sequence $A_1, A_2, \ldots, A_N$. For each index $i$ ($1 \leq i \leq N$), Chef needs to divide $A_i$ into two positive integers $x$ and $y$ (ie. $x, y > 0$) such that $x + y = A_i$, then place this as a point $(x, y)$ in the infinite $2$-dimensional coordinate plane. Help Chef to find the maximum number of distinct points that can be put in the plane, if he optimally splits the values $A_i$. Note that Chef can only perform one split for each index.

**Note:** Please use fast input/output methods for this problem.

**Input**

- The first line contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ integers $A_1, A_2, \ldots, A_N$.

**Output**

For each test case, print a single line containing one integer — the maximum number of distinct points there can be in the infinite plane.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 2 \cdot 10^5$
- $2 \leq A_i \leq 10^5$

## Sample

**Sample input**

```
2
6
2 2 4 4 2 6 
2
16 8
```

**Sample output**

```
4
2
```

<details><summary>Explanation</summary>

**Test Case 1:** Chef can divide $A_1$ as $(1,1)$, $A_2$ as $(1,1)$, $A_3$ as $(1,3)$, $A_4$ as $(2,2)$, $A_5$ as $(1,1)$, $A_6$ as $(2,4)$. Ignoring duplicates, there are $4$ distinct points, which is the maximum possible.

**Test Case 2:** Chef can divide $A_1$ as $(8,8)$, $A_2$ as $(4,4)$.

</details>

## Approach

Splitting $A_i$ into $x + y$ with both parts positive allows $x \in \{1, 2, \ldots, A_i - 1\}$, so a value $v$ offers exactly $v - 1$ distinct points: $(1, v-1)$ through $(v-1, 1)$.

Crucially, points coming from **different values never collide** — a point $(x,y)$ determines its source as $x + y$. So the values partition the problem completely and can be handled independently.

For a value $v$ occurring $c$ times, the number of distinct points obtainable is therefore limited by two things: how many copies there are, and how many distinct splits exist. So

$$\text{answer} = \sum_{v} \min\bigl(c_v,\ v - 1\bigr)$$

Both caps genuinely bind, and the first sample shows each. The value $2$ appears three times but admits only the single split $(1,1)$, so it contributes $1$ — surplus copies are wasted. The value $4$ appears twice and admits three splits, so both copies land distinctly and it contributes $2$. The value $6$ appears once, contributing $1$. Total $4$.

The second sample has two large values appearing once each, so each contributes a single point: $2$.

Note that $v = 2$ is the degenerate case, with only one legal split — a value of $2$ repeated many times still yields just one point, which is the main trap.

A `Counter` gives the multiplicities in one pass, and the sum is immediate. The statement's note about fast I/O matters at $N = 2 \times 10^5$ with $T$ up to $10$.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # Points from different values never collide, so each value is capped
        # independently by its copies and by its v - 1 possible splits.
        out.append(str(sum(min(c, v - 1) for v, c in counts.items())))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
