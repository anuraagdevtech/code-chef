# 446. One Dimensional Kingdoms

> [`ONEKING`](https://www.codechef.com/problems/ONEKING) &middot; difficulty **1743** &middot; time limit **3s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Stabbing intervals at earliest right endpoints |
| **CodeChef tags** | `Algorithms`, `Greedy`, `Sorting` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

**N** one dimensional kingdoms are represented as intervals of the form **[a_i , b_i]** on the real line.
A kingdom of the form **[L, R]** can be destroyed completely by placing a bomb at a point **x** on the real line if **L
≤ x ≤ R**.

Your task is to determine minimum number of bombs required to destroy all the one dimensional kingdoms.

**Input**

-
First line of the input contains **T** denoting number of test cases.

-
For each test case, first line contains **N** denoting the number of one dimensional kingdoms.

-
For each next **N** lines, each line contains two space separated integers **a_i** and **b_i**.

**Output**

For each test case , output an integer denoting the minimum  number of bombs required.

**Constraints**

Subtask 1 (20 points) : **1 ≤ T ≤ 100 , 1 ≤ N ≤ 100 , 0 ≤ a_i ≤ b_i ≤500 **

Subtask 2 (30 points) : **1 ≤ T ≤ 100 , 1 ≤ N ≤ 1000 , 0 ≤ a_i ≤ b_i ≤ 1000  **

Subtask 3 (50 points) : **1 ≤ T ≤ 20 , 1 ≤ N ≤ 10^5, 0 ≤ a_i ≤ b_i ≤ 2000**

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $0 \leq a_i \leq b_i \leq 2000$
- (subtask 3 lowers $T$ to $20$ while raising $N$ to $10^5$)

## Sample

**Sample input**

```
1
3
1 3
2 5
6 9
```

**Sample output**

```
2
```

<details><summary>Explanation</summary>

There are three kingdoms [1,3] ,[2,5] and [6,9]. You will need at least 2 bombs
to destroy the kingdoms. In one of the possible solutions, you can place two bombs at x = 2 and x = 6 .

</details>

## Approach

A bomb at $x$ destroys every kingdom whose interval contains $x$, so this is the classic **interval point cover** (or stabbing) problem: pick the fewest points so that every interval holds at least one.

Sort the kingdoms by **right endpoint** and sweep. Whenever the current kingdom is not already hit by the last bomb placed, drop a new bomb at that kingdom's right endpoint:

$$\text{place at } b_i \iff a_i > x_{\text{last}}$$

Choosing the right endpoint is what makes the greedy optimal. Some bomb must hit this interval, and among all positions that do, $b_i$ is the furthest right — so it covers a superset of the later intervals that any other valid choice would. Formally, exchanging an optimal solution's bomb for $b_i$ keeps it feasible, and induction finishes the argument.

Sorting by right endpoint rather than left is essential; sorting by left endpoint and bombing greedily can be arbitrarily bad, since a wide interval early on would let the sweep place bombs that cover nothing useful later.

In the sample, $[1,3]$, $[2,5]$ and $[6,9]$ sort as given. A bomb at $3$ destroys the first two kingdoms — note it covers $[2,5]$ even though $5 > 3$, which is exactly the reach the greedy buys. The third kingdom starts beyond $3$, so a second bomb at $9$ finishes the job: $2$ bombs.

Note equal right endpoints need no tie-break, since any of them accepts the same bomb.

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
        spans = []
        for _ in range(n):
            spans.append((int(data[pos + 1]), int(data[pos])))   # (right, left)
            pos += 2
        spans.sort()
        bombs = 0
        placed = -1
        for right, left in spans:
            # Bombing the right endpoint reaches as far forward as possible.
            if left > placed:
                bombs += 1
                placed = right
        out.append(str(bombs))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/ONEKING.md](../docs/greedy/ONEKING.md)
