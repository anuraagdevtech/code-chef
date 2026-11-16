[&larr; 681. Minimal Travel Time](681-CLASSES.md) &middot; [Index](README.md) &middot; [683. Weird Values &rarr;](683-WRDVLS.md)

# 682. Tree Distances

> [`TDISTS`](https://www.codechef.com/problems/TDISTS) &middot; difficulty **2383** &middot; time limit **0.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Only the bipartition sizes matter; realise them with a double star |
| **CodeChef tags** | `Data Structures`, `Graphs`, `Algorithms`, `Trees`, `Greedy`, `Observation` |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{x + y})$ per test case |
| **Space** | $O(\sqrt{x + y})$ for the output |

## Question

A tree is defined as a connected, undirected graph with $n$ vertices and $n−1$ edges. The distance between two vertices in a tree is equal to the number of edges on the unique simple path between them.

You are given two integers $x$ and $y$. Construct a tree with the following properties:
- The number of pairs of vertices with an **even** distance between them equals $x$.
- The number of pairs of vertices with an **odd** distance between them equals $y$.

By a pair of vertices, we mean an ordered pair of two (possibly, the same or different) vertices.

**Input**
The first line of the input contains a single integer $T$ denoting the number of test cases. Each test case consists of one line containing two space-separated integers $x$ and $y$.

**Output**
For each test case, if there is no tree satisfying the given properties, print ``"NO"`` (without quotes).

Otherwise, on the first line print ``"YES"`` (without quotes). Then print integer $n$ denoting the number of vertices in the tree, followed by $n−1$ lines describing the edges of the tree in any order. Vertices are numbered from $1$ to $n$. If there are multiple answers, print any of them.

**Constraints**
- $1 \leq T \leq 100$
- $1 \leq x,y \leq 10^9$
- $x + y \leq 10^9$

**Example Input**
```
4
2 2
29 20
3 12
6 3
```

**Example Output**
```
YES
2
1 2
YES
7
1 2
1 3
2 4
2 5
3 6
3 7
NO
NO
```

**Explanation**
In the first test case,  the pairs $(1 ,1)$ and $(2 ,2)$ have an even distance, while the pairs $(1 ,2)$ and $(2 ,1)$ have an odd distance.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq x,y \leq 10^9$
- $x + y \leq 10^9$

## Approach

A tree is bipartite, and the distance between two vertices is even exactly when they are on the same side. If the sides have $a$ and $b$ vertices, the ordered pairs (a vertex may be paired with itself) give

$$x = a^2 + b^2, \qquad y = 2ab .$$

Hence $x + y = (a + b)^2$ and $x - y = (a - b)^2$: both must be perfect squares, $n = \sqrt{x + y}$ is the number of vertices, and $|a - b| = \sqrt{x - y}$ must have the same parity as $n$ so that $a = (n + |a - b|)/2$ is an integer. Since $y \ge 1$, both sides are non-empty.

Any sizes $a, b \ge 1$ are realised by a double star: vertices $1 \dots a$ form one side and $a + 1 \dots n$ the other; join vertex 1 to every vertex of the second side, and join vertex $a + 1$ to the remaining vertices of the first side. That is $b + (a - 1) = n - 1$ edges, connected, and every edge crosses between the sides.

## Solution

```python
import sys
from math import isqrt


def solve(tokens):
    x, y = (next(tokens), next(tokens))
    n = isqrt(x + y)
    gap = isqrt(max(0, x - y))
    if n * n != x + y or x < y or gap * gap != x - y or (n - gap) % 2:
        return 'NO'
    part_a = (n + gap) // 2
    part_b = n - part_a
    if part_b == 0:
        return 'NO'
    edges = ['1 ' + str(i) for i in range(part_a + 1, n + 1)] + [str(part_a + 1) + ' ' + str(i) for i in range(2, part_a + 1)]
    return 'YES\n' + str(n) + '\n' + '\n'.join(edges)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $x < y$ is impossible because $a^2 + b^2 \ge 2ab$.
- Either $x + y$ or $x - y$ not being a perfect square gives NO.
- A parity mismatch between $n$ and $|a - b|$ gives NO.
- Many trees have the right bipartition, so the output is validated by a checker.

## Dry run

`x = 29, y = 20`: $x + y = 49 = 7^2$ and $x - y = 9 = 3^2$, so $n = 7$, $a = 5$, $b = 2$ ($25 + 4 = 29$, $2 \cdot 10 = 20$).

Sides `{1, 2, 3, 4, 5}` and `{6, 7}`. Edges: `1-6`, `1-7`, then `6-2`, `6-3`, `6-4`, `6-5`.

`x = 3, y = 12`: $x < y$, so NO.

---

Same problem grouped by topic: [../docs/constructive/TDISTS.md](../docs/constructive/TDISTS.md)
