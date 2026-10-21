# 1460 &middot; Polygon Relationship

> CodeChef problem code [`POLYREL`](https://www.codechef.com/problems/POLYREL) &middot; time limit **1.5s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Halving the vertex count down to a triangle |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Geometry`, `Greedy` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case, all of it input reading |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/geometry/POLYREL.md](../docs/geometry/POLYREL.md)

## Question

You are given a strictly convex polygon with $N$ vertices (numbered $1$ through $N$). For each valid $i$, the coordinates of the $i$-th vertex are $(X_i, Y_i)$. You may perform the following operation any number of times (including zero):
- Consider a *parent polygon*. Initially, this is the polygon you are given.
- Draw one of its *child polygons* ― a simple non-degenerate polygon such that each of its sides is a chord of the parent polygon (it cannot be a side of the parent polygon). The operation cannot be performed if the parent polygon does not have any child polygons.
- The child polygon which you drew becomes the new parent polygon.

Your goal is to draw as many sides of polygons in total as possible (including the polygon given at the start). Find this maximum total number of sides.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $X_i$ and $Y_i$.

### Output
Print a single line containing one integer ― the maximum possible number of sides of polygons.

### Constraints
- $1 \le T \le 1,000$
- $3 \le N \le 10^5$
- $|X_i|, |Y_i| \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^6$

## Constraints

- $1 \le T \le 1,000$
- $3 \le N \le 10^5$
- $|X_i|, |Y_i| \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^6$

## Sample

**Sample input**

```
2
4
-100 1
0 2
0 0
100 1
7
-4 0
-3 -2
-3 2
0 -4
2 -3
2 3
3 2
```

**Sample output**

```
4
10
```

<details><summary>Explanation</summary>

**Example case 1:** It is not possible to draw a child polygon.

**Example case 2:** We can draw a child polygon once, e.g. with vertices $(-3, -2)$, $(-3, 2)$ and $(3, 2)$. Even though there are several other ways to draw a child polygon, it can only be a triangle, so the total number of sides cannot exceed $7+3 = 10$.

</details>

## Approach

The coordinates are **irrelevant** — the answer depends only on $N$. That is the whole insight, and strict convexity is what licenses it: any set of vertices in convex position forms a simple non-degenerate polygon in their cyclic order, so a candidate child is feasible purely combinatorially.

A child's sides are chords of the parent, so its vertices are parent vertices and consecutive chosen vertices are **non-adjacent** in the parent. Choosing $k$ vertices cyclically from $N$ with every gap at least $2$ needs $N \geq 2k$, so

$$k \leq \left\lfloor \frac{N}{2} \right\rfloor$$

and that bound is attained by taking every second vertex. A polygon also needs $k \geq 3$, which is where the chain stops.

Since larger children can only help — more sides now, and a weakly larger budget for the next step — the greedy "always halve" is optimal, and the answer is

$$N + \left\lfloor \frac{N}{2} \right\rfloor + \left\lfloor \frac{N}{4} \right\rfloor + \cdots$$

truncated at the last term that is still at least $3$. The chain is $O(\log N)$ long.

The two samples sit on either side of the cutoff. A quadrilateral has $\lfloor 4/2 \rfloor = 2 < 3$, so it has no child at all and the answer is just $4$ — note the sample's quadrilateral is deliberately drawn as a thin sliver, which changes nothing. The heptagon gives $\lfloor 7/2 \rfloor = 3$, a triangle, and then $\lfloor 3/2 \rfloor = 1$ stops the chain: $7 + 3 = 10$.

The real work is I/O: $\sum N \leq 2 \times 10^6$ vertex pairs must be read and discarded quickly, so read the whole stream at once rather than parsing per line.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1 + 2 * n          # the coordinates do not matter at all
        total = 0
        while n >= 3:
            total += n
            n //= 2               # every second vertex is the largest child
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case, all of it input reading
- **Space:** $O(1)$
