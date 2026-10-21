# 200. Points and Lines

> [`POLIN`](https://www.codechef.com/problems/POLIN) &middot; difficulty **1296** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Counting distinct coordinates independently |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Given $N$ points of the form $(x_i, y_i)$ on a $2$-D plane.

From each point, you draw $2$ lines one horizontal and one vertical. Now some of the lines may overlap each other, therefore you are required to print the number of **distinct** lines you can see on the plane.

**Note:**
- Two horizontal lines are distinct if they pass through different $y$ coordinates.
- Two vertical lines are distinct if they pass through different $x$ coordinates.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains a single integer $N$, the number of points.
- The next $N$ lines contain two space separated integers $x_i, y_i$, the coordinate of the $i^{th}$ point.

**Output**

For each testcase, output in a single line the number of **distinct** lines that can be seen on the plane.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $0 \leq X_i, Y_i \leq 10^9$
- Sum of $N$ over all test cases is atmost $10^5$.

## Sample

**Sample input**

```
3
4
1 1
1 0
0 1
0 0
5
0 0
0 1
0 2
0 3
0 4
1
10 10
```

**Sample output**

```
4
6
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** There are $2$ horizontal lines passing through $Y = 0$ and $Y = 1$, and $2$  vertical lines passing through $X = 0$ and $X = 1$.

<img src="https://s3.amazonaws.com/codechef_shared/download/Images/DAANISH/graph+(1).png" width="500" height="500">

**Test Case $2$:** There are $5$ horizontal lines passing through $Y = 0, Y = 1, Y = 2, Y = 3$ and $Y = 4$ and $1$ vertical line passing through $X = 0$.

**Test Case $3$:** There is $1$ horizontal line passing through $Y = 10$ and $1$ vertical line passing through $X = 10$.

</details>

## Approach

Each point contributes one vertical line at $x = x_i$ and one horizontal line at $y = y_i$. The statement defines distinctness per axis: two vertical lines coincide exactly when their $x$ values match, and likewise for horizontal and $y$.

So the two families never interfere, and the answer is simply

$$|\{x_1, \ldots, x_N\}| + |\{y_1, \ldots, y_N\}|$$

— two independent distinct-counts, added.

The trap is treating the lines as a single collection and deduplicating across axes. A vertical line at $x = 5$ and a horizontal line at $y = 5$ share a number but are different lines, so they must be counted separately. Keeping two sets rather than one avoids the question entirely.

Sample case 2 shows heavy overlap on one axis: five points all share $x = 0$, collapsing to a single vertical line, while their five distinct $y$ values give five horizontal lines — $6$ in total, not $10$.

Sample case 1 has four points forming a unit square, with two distinct $x$ and two distinct $y$, so $4$ lines. Sample case 3 is a single point contributing one of each.

Coordinates reach $10^9$, so hashing into a Python `set` is the right structure — an array indexed by coordinate is out of the question. With the sum of $N$ at $10^5$, two sets per test case are comfortable.

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
        # Vertical and horizontal lines are counted on separate axes, so a
        # shared numeric value does not merge them.
        xs = set(data[pos:pos + 2 * n:2])
        ys = set(data[pos + 1:pos + 2 * n:2])
        pos += 2 * n
        out.append(str(len(xs) + len(ys)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The two axes are counted independently**, so a shared numeric value does not merge anything: the third row's single point at $(10, 10)$ contributes one vertical and one horizontal line, for $2$.
- **All points on one vertical line** (the second row): one vertical line plus $N$ distinct horizontal ones, giving $6$ for $N = 5$.
- **Duplicate points** would collapse on both axes at once, which the sets handle with no extra logic.
- **Coordinate $0$ is allowed**, so the origin is an ordinary point and the tokens include `0`.
- **Comparing raw byte tokens is safe** here, since the input has no leading zeros or negative numbers and each value therefore has exactly one spelling.
- **The strided slices read the $x$ and $y$ columns in one pass** without materialising a list of points, which matters at $\sum N = 10^5$.

## Dry run

| points | distinct $x$ | distinct $y$ | output |
|---|---|---|---:|
| $(1,1), (1,0), (0,1), (0,0)$ | $\{0, 1\}$ → 2 | $\{0, 1\}$ → 2 | `4` |
| $(0,0) \dots (0,4)$ | $\{0\}$ → 1 | $\{0,1,2,3,4\}$ → 5 | `6` |
| $(10, 10)$ | $\{10\}$ → 1 | $\{10\}$ → 1 | `2` |

---

Same problem grouped by topic: [../docs/sets/POLIN.md](../docs/sets/POLIN.md)
