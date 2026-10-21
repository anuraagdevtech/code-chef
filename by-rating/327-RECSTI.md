# 327. Sticks and Rectangles

> [`RECSTI`](https://www.codechef.com/problems/RECSTI) &middot; difficulty **1555** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Pairing by length, then pairing the pairs |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + \max L)$ per test case |
| **Space** | $O(\max L)$ |

## Question

MoEngage has a bundle of $N$ sticks. The $i^{th}$ stick has a length $L_i$ meters.

Find the **minimum** number of sticks (of any length) you need to add to the bundle such that you can construct some [rectangles](https://en.wikipedia.org/wiki/Rectangle) where **each** stick of the bundle belongs to **exactly one** rectangle and **each** side of a rectangle should be formed with **exactly one** stick.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, denoting the number of given sticks.
- The second line of each test case contains $N$ space-separated integers $L_1, L_2, \dots, L_N$, denoting the length of the sticks.

**Output**

For each test case, output in a single line, the minimum number of sticks you need to add to the bundle to satisfy the given conditions.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq L_i \leq 100$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
4
1
1
2
2 5
4
2 2 3 3
7
1 3 5 7 1 7 5
```

**Sample output**

```
3
2
0
1
```

<details><summary>Explanation</summary>

**Test case $1$:** One possible way is to add $3$ sticks with lengths $1, 2,$ and $2$. Now, it is possible to construct a rectangle with one pair of opposite sides having a length of $1$ and another pair of opposite sides having a length of $2$.

**Test case $2$:** The optimal way is to add $2$ sticks with lengths $2$ and $5$. Now, it is possible to construct a rectangle with one pair of opposite sides having a length of $2$ and another pair of opposite sides having a length of $5$.

**Test case $3$:** There is no need to add more sticks to the bundle as it is possible to construct a rectangle using the given sticks.

</details>

## Approach

A rectangle is two sticks of one length and two of another (equal lengths give a square), so the construction has **two levels**: sticks pair up by equal length, and pairs group up in twos to form rectangles. Both levels are forced, so the minimum additions follow by counting.

At the first level, a length occurring $c$ times gives $\lfloor c/2 \rfloor$ complete pairs and, when $c$ is odd, one orphan. Each orphan needs exactly one new stick of its own length, so

$$\text{additions}_1 = \#\{\text{lengths with odd count}\}, \qquad \text{pairs} = \sum_\ell \left\lceil \frac{c_\ell}{2} \right\rceil$$

At the second level, every rectangle consumes two pairs. If the pair count is odd, one pair is left over and needs a partner — a brand-new pair of two identical sticks, so $+2$. There is no cheaper fix: a single extra stick cannot form a pair on its own once every length already has an even count.

$$\text{answer} = \#\{\text{odd counts}\} + 2 \cdot (\text{pairs} \bmod 2)$$

The samples walk through the cases. A lone stick needs $1$ to make its pair and $2$ more for a second pair, giving $3$ — the worst case for $N = 1$. Two sticks of different lengths need one partner each, and the resulting two pairs already form a rectangle, so $2$. `2 2 3 3` is already a rectangle, so $0$. And `1 3 5 7 1 7 5` has a single odd count (the lone $3$), after which there are four pairs — an even number — so just $1$.

Note it is the number of *pairs* whose parity matters, not the number of sticks: in the last sample $7$ sticks become $8$, and $8/4 = 2$ rectangles fall out without further help.

## Solution

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
        counts = Counter(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        added = sum(c & 1 for c in counts.values())      # orphan per odd length
        pairs = sum((c + 1) // 2 for c in counts.values())
        # A leftover pair needs a whole new pair to square off with.
        out.append(str(added + 2 * (pairs & 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/RECSTI.md](../docs/greedy/RECSTI.md)
