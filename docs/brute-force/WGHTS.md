# 56. Weights

> CodeChef problem code [`WGHTS`](https://www.codechef.com/problems/WGHTS) &middot; difficulty **697** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Enumerating every non-empty subset |
| **Time** | $O(2^k)$ per test case with $k = 3$, so $O(1)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is playing with weights. He has an object weighing $W$ units. He also has three weights each of $X, Y,$ and $Z$ units respectively. Help him determine whether he can measure the **exact** weight of the object with one or more of these weights.

If it is possible to measure the weight of object with one or more of these weights, print `YES`, otherwise print `NO`.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line containing a four positive integers $W, X, Y,$ and $Z$.

**Output**

For each test case, output on a new line `YES` if it is possible to measure the weight of object with one or more of these weights, otherwise print `NO`.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yes`, `YES`, `Yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq W, X, Y, Z \leq 10^5$

## Sample

**Sample input**

```
4
5 2 1 6
7 9 7 2
20 8 10 12
20 10 11 12
```

**Sample output**

```
NO
YES
YES
NO
```

<details><summary>Explanation</summary>

**Test Case $1$:** It is not possible to measure $5$ units using any combination of given weights.

**Test Case $2$:** Chef can use the second weight of $7$ units to measure the object exactly.

**Test Case $3$:** Chef can use combination of first and third weights to measure $8+12=20$ units.

**Test Case $4$:** Chef cannot measure $20$ units of weight using any combination of given weights.

</details>

## Approach

Chef may use **one or more** of the three weights, so the reachable totals are the sums of the non-empty subsets of $\{X, Y, Z\}$. With three weights there are $2^3 - 1 = 7$ of them:

$$X,\quad Y,\quad Z,\quad X+Y,\quad X+Z,\quad Y+Z,\quad X+Y+Z$$

Seven candidates is small enough to list outright, and because the set is fixed the cost is constant per test case.

The phrase "one or more" is what excludes the empty subset — a weight of $0$ is not measurable, and since $W \geq 1$ it could never match anyway. It also means every single weight counts on its own, which sample case 2 relies on: $W = 7$ matches the weight $7$ directly, with the others unused.

Rather than hard-coding seven expressions, the code uses `itertools.combinations` over sizes $1$ to $3$. That is the same seven sums, written in a form that would extend unchanged to more weights — and it is the honest way to express "any subset" so the reader sees the structure rather than a list of special cases.

It is worth noting what the problem does *not* ask. In classic balance-scale puzzles, weights may be placed on either pan, which allows **differences** such as $Y - X$ and turns this into a different question. Here weights only add. Sample case 4 confirms it: $20$ is unreachable from $\{10, 11, 12\}$ by addition, even though $10 + 12 - 11 = 11$ and other signed combinations exist.

For a larger weight set this approach would become $O(2^k)$ and a subset-sum DP would take over; at $k = 3$ enumeration is exactly right.

## Solution (Python)

```python
import sys
from itertools import combinations


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        w, x, y, z = map(int, data[1 + 4 * i:5 + 4 * i])
        weights = (x, y, z)
        # Every non-empty subset; weights only add, they never subtract.
        ok = any(sum(c) == w
                 for r in (1, 2, 3)
                 for c in combinations(weights, r))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(2^k)$ per test case with $k = 3$, so $O(1)$
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
