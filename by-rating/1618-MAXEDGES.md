# 1618 &middot; MaxEdges

> CodeChef problem code [`MAXEDGES`](https://www.codechef.com/problems/MAXEDGES) &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Complete layered DAG minus the forbidden pairs |
| **CodeChef tags** | `Mathematics`, `Combinatorics` |
| **CodeChef category** | easy |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/combinatorics/MAXEDGES.md](../docs/combinatorics/MAXEDGES.md)

## Question

Tracy gives Charlie a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) with $N$ vertices. Among these $N$ vertices, $K$ vertices are *sources*, and $L$ vertices are *sinks*.

Find out the **maximum** number of edges this graph can have.

Note:
- A *source* is a vertex with **no incoming** edge.
- A *sink* is a vertex with **no outgoing** edge.
- A vertex can be **both**, a source, and a sink.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three space-separated integers $N, K,$ and $L$ - the number of vertices, the number of sources and the number of sinks respectively.

**Output**

- For each test case, output in a single line, the **maximum** number of edges this graph can have.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^9$
- $1 \leq K \lt N$
- $1 \leq L \lt N$

## Sample

**Sample input**

```
2
3 1 1
5 3 3
```

**Sample output**

```
3
4
```

<details><summary>Explanation</summary>

**Test case $1$:** Assume that the vertices are numbered $1,2,$ and $3$. Let $1$ be a source and $3$ be a sink. The edges of a possible DAG are $1\rightarrow 2, 2\rightarrow 3,$ and $1\rightarrow 3$.

The number of edges in this graph are $3$. It can be shown that this is the maximum number of edges possible under given constraints.

**Test case $2$:** Assume that the vertices are numbered $1,2,3,4,$ and $5$. Let $1,2,$ and $3$ be sources and $3, 4, $ and $5$ be  sinks. The edges of a possible DAG are $1\rightarrow 4, 2\rightarrow 4, 1\rightarrow 5$ and $2\rightarrow 5$.

The number of edges in this graph are $4$. It can be shown that this is the maximum number of edges possible under given constraints.

</details>

## Approach

A DAG's edges all point forward in some topological order, so the ceiling is the complete forward graph with $\binom{N}{2}$ edges. The source and sink requirements only remove edges from it.

Lay the vertices out as **sources, then middles, then sinks**. Every forward edge is allowed except two families:

- an edge between two sources would give the later one an incoming edge, so all $\binom{K}{2}$ source-source pairs are forbidden;
- symmetrically all $\binom{L}{2}$ sink-sink pairs are forbidden.

Everything else is fine, and this layout simultaneously satisfies the middles (each gets an edge from a source and one to a sink, so it is neither a source nor a sink).

When $K + L > N$ the groups cannot be disjoint, and a vertex that is both a source and a sink is **isolated** — no edges at all. Since isolated vertices only waste capacity, take as few as the counts force:

$$b = \max(0,\ K + L - N)$$

and apply the layout to the other $N - b$ vertices, which then have $K - b$ pure sources and $L - b$ pure sinks:

$$\text{answer} = \binom{N-b}{2} - \binom{K-b}{2} - \binom{L-b}{2}$$

The samples show both regimes. $N = 3, K = L = 1$ has $b = 0$ and no forbidden pairs, so the full $\binom{3}{2} = 3$ edges. $N = 5, K = L = 3$ forces $b = 1$: one vertex is isolated, and the remaining four split into two sources and two sinks with no middles, giving $6 - 1 - 1 = 4$ — only the four source-to-sink edges survive.

With $N$ up to $10^9$ the count reaches about $5 \times 10^{17}$, which needs 64-bit arithmetic in C++; Python's integers are unbounded.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k, l = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        # Vertices that must be both source and sink end up isolated.
        both = k + l - n
        if both < 0:
            both = 0
        n -= both
        k -= both
        l -= both
        out.append(str(n * (n - 1) // 2 - k * (k - 1) // 2 - l * (l - 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
