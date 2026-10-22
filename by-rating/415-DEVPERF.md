# 415. Devu and Perfume

> [`DEVPERF`](https://www.codechef.com/problems/DEVPERF) &middot; difficulty **1708** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Manhattan 1-centre via rotated coordinates |
| **CodeChef tags** | `Data Structures`, `Arrays`, `2D Arrays` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(nm + n \log m)$ per test case |
| **Space** | $O(nm)$ |

## Question

There is a haunted town called HauntedLand. The structure of HauntedLand can be thought of as a grid of size **n * m**. There is a house in each cell of the grid. Some people have fled from their houses because they were haunted. '.' represents a haunted house whereas '*' represents a house in which people are living.

One day, Devu, the famous perfumer came to town with a perfume whose smell can hypnotize people. Devu can put the perfume in at most one of the houses. This takes Devu one second. Then, the perfume spreads from one house (need not be inhabited by people) to all its adjacent houses in one second, and the cycle continues. Two houses are said to be a adjacent to each other, if they share a corner or an edge, i.e., each house (except those on the boundaries) will have 8 adjacent houses.

You want to save people from Devu's dark perfumery by sending them a message to flee from the town. So, you need to estimate the minimum amount of time Devu needs to hypnotize all the people? Note that if there are no houses inhabited by people, Devu doesn't need to put perfume in any cell.

**Input**

The first line of input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

First line of each test case contains two space separated integers **n, m** denoting the dimensions of the town.

For each of next **n** lines, each line has **m** characters (without any space) denoting a row of houses of the town.

**Output**

For each test case, output a single integer corresponding to the answer of the problem.

**Constraints**

- **1** ≤ **T** ≤ **20**

**Subtask #1:** (40 points)

- **1** ≤ **n, m** ≤ **100**

**Subtask #2:** (60 points)
- **1** ≤ **n, m** ≤ **1000**

## Constraints

- 1 ≤ T ≤ 20

## Sample

**Sample input**

```
2
2 2
*.
..
3 4
.*..
***.
.*..
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

**In the first example**, it will take Devu one second for putting the perfume at the only house. So, the answer is 1.

**In the second example**, He will first put the perfume at the * at cell (1, 1) (assuming 0-based indexing).
Now, it will take Devu 1 secs to put perfume. In the next second, the perfume will spread to all of its adjacent cells, thus making each house haunted.
So, the answer is 2.

</details>

## Approach

Placing the perfume costs one second and it then spreads one cell per second through side-adjacent houses, so the time is $1$ plus the **largest Manhattan distance** from the chosen cell to an inhabited one. With no inhabited houses the answer is $0$.

So this is the Manhattan 1-centre problem. Rotate coordinates:

$$u = r + c, \qquad v = r - c \qquad\Longrightarrow\qquad |r_1-r_2| + |c_1-c_2| = \max\bigl(|u_1-u_2|,\ |v_1-v_2|\bigr)$$

Manhattan distance becomes Chebyshev distance, which decouples the axes. Then the worst inhabited house seen from a cell $p$ depends only on four numbers over the `*` cells:

$$f(p) = \max\bigl(u_p - u_{\min},\ u_{\max} - u_p,\ v_p - v_{\min},\ v_{\max} - v_p\bigr)$$

so one pass over the grid collects $u_{\min}, u_{\max}, v_{\min}, v_{\max}$ and no per-pair work is needed.

Minimising $f$ still has to respect the grid, since not every $(u,v)$ is a real cell. But $f$ is a maximum of linear functions, hence **convex in $c$ for each fixed row**, so a ternary search over the columns finds each row's best cell in $O(\log m)$ — avoiding the $O(nm)$ scan over placements that would otherwise sit on top of reading the grid.

The sample's second case has `*` cells with $u \in [3,5]$ and $v \in [-1,1]$, so the centre $(2,2)$ gives $f = 1$ and the answer is $2$: one second to place, one to reach the four arms of the plus shape. The first case has a single inhabited house, so placing the perfume there gives $f = 0$ and the answer is $1$ — the placement second is always paid.

## Solution

```python
import sys

STAR = 0x2A


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        rows = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Manhattan distance is Chebyshev distance in (r+c, r-c).
        lo_u = lo_v = 1 << 60
        hi_u = hi_v = -(1 << 60)
        for r in range(n):
            row = rows[r]
            for c in range(m):
                if row[c] != STAR:
                    continue
                u, v = r + c, r - c
                lo_u = min(lo_u, u)
                hi_u = max(hi_u, u)
                lo_v = min(lo_v, v)
                hi_v = max(hi_v, v)
        if hi_u < lo_u:
            out.append("0")                 # nobody to hypnotise
            continue

        def worst(r, c):
            u, v = r + c, r - c
            return max(u - lo_u, hi_u - u, v - lo_v, hi_v - v)

        best = 1 << 60
        for r in range(n):
            # worst(r, .) is a max of linear functions, hence convex in c.
            left, right = 0, m - 1
            while right - left > 2:
                a = left + (right - left) // 3
                b = right - (right - left) // 3
                if worst(r, a) <= worst(r, b):
                    right = b
                else:
                    left = a
            for c in range(left, right + 1):
                best = min(best, worst(r, c))
        out.append(str(best + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Manhattan distance becomes Chebyshev distance under the rotation $(u, v) = (r+c,\, r-c)$**, so the worst distance from a cell to every inhabited house is $\max$ of four linear terms over the extremes of $u$ and $v$ — four numbers summarise the whole grid.
- **Only the bounding box in rotated coordinates matters**, not the individual houses, which is what makes the evaluation constant-time per candidate cell.
- **The perfume may go in a haunted house too**, so every cell is a candidate — not just the inhabited ones.
- **No inhabited houses at all** → $0$ seconds, since nothing needs hypnotising; this is checked before any search.
- **The $+1$ is the placement second**, which the statement charges separately from the spreading.
- **The worst-distance function is convex along a row**, being a maximum of linear functions, so a ternary search finds each row's best column — and the final window is swept directly to avoid the usual off-by-one.
- **A single inhabited house** gives $0$ spreading time if the perfume is placed there, for an answer of $1$.

## Dry run

Second sample: a $3 \times 4$ grid with inhabited houses at $(0,1)$, $(1,0)$, $(1,1)$, $(1,2)$, $(2,1)$ (0-based).

| house | $u = r+c$ | $v = r-c$ |
|---|---:|---:|
| $(0,1)$ | 1 | $-1$ |
| $(1,0)$ | 1 | 1 |
| $(1,1)$ | 2 | 0 |
| $(1,2)$ | 3 | $-1$ |
| $(2,1)$ | 3 | 1 |

So $u \in [1,3]$ and $v \in [-1,1]$. Placing the perfume at $(1,1)$ gives $u = 2$, $v = 0$ and a worst distance of $\max(1, 1, 1, 1) = 1$.

Output $1 + 1 = $ `2`.

---

Same problem grouped by topic: [../docs/geometry/DEVPERF.md](../docs/geometry/DEVPERF.md)
