# 481. Missing a Point

> [`PTMSSNG`](https://www.codechef.com/problems/PTMSSNG) &middot; difficulty **unrated** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | XOR cancels everything that appears twice |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has $N$ axis-parallel rectangles in a 2D Cartesian coordinate system. These rectangles may intersect, but it is guaranteed that all their $4N$ vertices are pairwise distinct.

Unfortunately, Chef lost one vertex, and up until now, none of his fixes have worked (although putting an image of a point on a milk carton might not have been the greatest idea after all...). Therefore, he gave you the task of finding it! You are given the remaining $4N-1$ points and you should find the missing one.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- Then, $4N-1$ lines follow. Each of these lines contains two space-separated integers $x$ and $y$ denoting a vertex $(x, y)$ of some rectangle.

**Output**
For each test case, print a single line containing two space-separated integers $X$ and $Y$ ― the coordinates of the missing point. It can be proved that the missing point can be determined uniquely.

**Constraints**
- $T \le 100$
- $1 \le N \le 2 \cdot 10^5$
- $|x|, |y| \le 10^9$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

**Subtasks**
**Subtask #1 (20 points):**
- $T = 5$
- $N \le 20$

**Subtask #2 (30 points):** $|x|, |y| \le 10^5$

**Subtask #3 (50 points):** original constraints

## Constraints

- $T \le 100$
- $1 \le N \le 2 \cdot 10^5$
- $|x|, |y| \le 10^9$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
1
2
1 1
1 2
4 6
2 1
9 6
9 3
4 3
```

**Sample output**

```
2 2
```

<details><summary>Explanation</summary>

The original set of points are:
![fig1](https://i.imgur.com/7oHoe86.png =333x211)

Upon adding the missing point $(2, 2)$, $N = 2$ rectangles can be formed:
![fig1](https://i.imgur.com/N8ceCw0.png =333x211)

</details>

## Approach

An axis-parallel rectangle with corners at $x \in \{x_1, x_2\}$ and $y \in \{y_1, y_2\}$ contributes each of its two $x$-values **exactly twice** among its four vertices, and likewise each $y$-value.

So across all $N$ rectangles, every $x$-coordinate occurs an **even** number of times, and the same holds for $y$. Removing one vertex breaks that parity for exactly one $x$ and one $y$ — the missing ones.

XOR is the perfect detector: $v \oplus v = 0$, so every value occurring an even number of times cancels out entirely, leaving only the odd one out.

$$X = \bigoplus_i x_i, \qquad Y = \bigoplus_i y_i$$

over the $4N-1$ given vertices.

Note the $x$ and $y$ folds are **independent** — the missing point's coordinates need not come from the same input vertex, and the parity argument applies to each axis separately.

The guarantee that all $4N$ vertices are **pairwise distinct** is what makes the rectangles unambiguous, but the XOR argument does not actually depend on it: it only needs each coordinate value to appear an even number of times, which the rectangle structure guarantees regardless.

Coordinates may be **negative**, down to $-10^9$. Python's XOR on negative integers follows two's-complement semantics over arbitrary precision, and $v \oplus v = 0$ still holds, so no offsetting is needed — though a fixed-width language would want care.

In the sample the $x$ values fold to $2$ and the $y$ values to $2$, giving the missing vertex $(2,2)$ — which completes the rectangle with corners $1$ and $2$ on both axes.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        # Each coordinate appears twice per rectangle, so XOR leaves the
        # one whose partner is missing. The two axes fold independently.
        x = y = 0
        for i in range(4 * n - 1):
            x ^= int(data[pos + 2 * i])
            y ^= int(data[pos + 2 * i + 1])
        pos += 2 * (4 * n - 1)
        out.append(f"{x} {y}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/bit-manipulation/PTMSSNG.md](../docs/bit-manipulation/PTMSSNG.md)
