[&larr; 633. Mexy Array](633-MEXYARR.md) &middot; [Index](README.md) &middot; [635. Valid String &rarr;](635-VSTRING.md)

# 634. Pyramid Traversal

> [`PYRAMIDMOVES`](https://www.codechef.com/problems/PYRAMIDMOVES) &middot; difficulty **2194** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Convert labels to (row, column) and choose which steps go right |
| **CodeChef tags** | `Mathematics`, `Combinatorics`, `Algorithms`, `Basic Math`, `Permutations & Combinations`, `Observation` |
| **Complexity class** | Constant time $O(1)$ (one-off precomputation) |
| **Time** | $O(\sqrt{V})$ precomputation and $O(1)$ per query, $V$ the largest label |
| **Space** | $O(\sqrt{V})$ |

## Question

You are given a pyramid of the following form with an infinite number of rows:
    $$1$$
   $$2\ 3$$
  $$4\ 5\  6$$
 $$7\ 8\ 9\ 10$$
$$...........$$

From a cell, you can move to either the bottom-left cell or the bottom-right cell directly in contact with the current one (For example, you can make the following moves: $1 \rightarrow 2, 1 \rightarrow 3, 6 \rightarrow 9, 6 \rightarrow 10$, while you **cannot** make moves $2\to 6$ or $2\rightarrow 7$).

You are given a starting cell $s$ and an ending cell $e$. Starting at cell $s$, find the number of ways to reach cell $e$. This number can be large, so print the answer modulo $10^9 + 7$.

Two ways are said to be different if there exists at least one cell which was visited in one of the ways but not the other one.

**Input**

- The first line of input contains a single integer $T$, the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $s$ and $e$, denoting the starting and the ending cell respectively.

**Output**

For each test case, output a single line containing one integer: the number of ways to go from $s$ to $e$ modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq s, e\leq 10^9$

**Subtasks**

**Subtask 1(100 points):** Original constraints

## Sample

**Sample input**

```
3
2 7
1 5
5 3
```

**Sample output**

```
1
2
0
```

<details><summary>Explanation</summary>

In the first test case, there exists only $1$ way to move from $2$ to $7$, which is:
- $2 \rightarrow 4 \rightarrow 7$

In the second test case, there exist $2$ ways to move from $1$ to $5$, which are:
- $1 \rightarrow 2 \rightarrow 5$
- $1 \rightarrow 3 \rightarrow 5$

In the third test case, it is not possible to move from $5$ to $3$.

</details>

## Approach

Row $r$ of the pyramid ends with the triangular number $r(r+1)/2$, so the row of a label $x$ is the smallest $r$ with $r(r+1)/2 \ge x$, found from an integer square root with a one-step correction, and its column is $x - r(r-1)/2$.

Every move goes down one row; the bottom-left move keeps the column and the bottom-right move increases it by one. To get from $(r_1, c_1)$ to $(r_2, c_2)$ we need exactly $d = r_2 - r_1$ moves, of which exactly $k = c_2 - c_1$ go right. This is possible only for $0 \le k \le d$, and then any choice of which moves go right is a valid path:

$$\text{ways} = \binom{d}{k}.$$

Labels up to $10^9$ lie in rows below 45000, so factorials up to 50000 are enough.

## Solution

```python
import sys
from math import isqrt


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    cases = [(next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 10 ** 9 + 7
    LIMIT = 50000
    fact = [1] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (LIMIT + 1)
    inv_fact[LIMIT] = pow(fact[LIMIT], -1, MOD)
    for i in range(LIMIT, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def cell(x):
        r = (isqrt(8 * x - 7) + 1) // 2
        if r * (r + 1) // 2 < x:
            r += 1
        return (r, x - r * (r - 1) // 2)
    for start, end in cases:
        r, c = cell(start)
        u, v = cell(end)
        down = u - r
        right = v - c
        out.append(str(fact[down] * inv_fact[right] % MOD * inv_fact[down - right] % MOD) if 0 <= right <= down else '0')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- The end above the start, or too far left or right: 0.
- $s = e$: one way, the empty path.
- The float-free row computation uses `isqrt` and fixes the off-by-one explicitly.
- The pyramid never restricts a path between two valid cells - columns stay within their rows automatically.

## Dry run

- `1 -> 5`: cells $(1, 1)$ and $(3, 2)$, so $d = 2$, $k = 1$: $\binom{2}{1} = 2$.
- `2 -> 7`: cells $(2, 1)$ and $(4, 1)$, $d = 2$, $k = 0$: 1.
- `5 -> 3`: the end is above the start: 0.

---

Same problem grouped by topic: [../docs/combinatorics/PYRAMIDMOVES.md](../docs/combinatorics/PYRAMIDMOVES.md)
