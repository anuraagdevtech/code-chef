[&larr; 610. Odd Binomial Coefficients](610-ODDBIN.md) &middot; [Index](README.md) &middot; [612. Maximum Size &rarr;](612-RISK.md)

# 611. Travelling in the Graph

> [`TRAVELLING`](https://www.codechef.com/problems/TRAVELLING) &middot; difficulty **2108** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | 0-1 BFS where only unit-length added edges are ever needed |
| **CodeChef tags** | `Algorithms`, `Graph Algos`, `Shortest Paths`, `Dijkstra's Algorithm`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(N + M)$ |

## Question

You are given a graph with $N$ vertices (numbered $1$ to $N$) and $M$ bidirectional edges, which doesn't contain multiple edges or self-loops — that is, the given graph is a simple undirected graph.

For each pair of vertices $a, b$ such that $1 \leq a, b \leq N$, it is possible to add a new edge between vertices $a$ and $b$ to the graph, with a cost of $(a - b)^2$.

Find the minimum cost of adding edges so that vertex $N$ is reachable from vertex $1$.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains $2$ space-separated integers, $N$ and $M$.
- The $i^{th}$ of the next $M$ lines contains $2$ space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between vertex $u_i$ and vertex $v_i$ in the graph.

**Output**

For each test case, output the answer in a single line.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 2 \cdot 10^5$
- $0 \leq M \leq 2 \cdot 10^5$
- $1 \leq u_i, v_i \leq N$
- The graph doesn't contain self-loops or multiple edges
- Sum of $N$ over all testcases is no more than $2 \cdot 10^5$.
- Sum of $M$ over all testcases is no more than $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
2 0
5 4
3 2
1 4
5 3
4 2
6 3
1 2
3 2
1 3
```

**Sample output**

```
1
0
3
```

<details><summary>Explanation</summary>

**Test Case $1$:** Add an edge between vertices $1$ and $2$, with cost $(1-2)^2 = 1$.

**Test Case $2$:** Vertices $1$ and $5$ are already connected, so no edges need to be added.

</details>

## Approach

An added edge between $a$ and $b$ costs $(a - b)^2$. Replacing it by the chain $a, a \pm 1, \dots, b$ of $|a - b|$ unit edges costs only $|a - b|$ and connects at least as much. So an optimal solution only buys edges between consecutive labels, each for cost 1.

That turns the task into a shortest path from 1 to $N$ in a graph with the original edges at weight 0 and an edge of weight 1 between every $i$ and $i + 1$. A 0-1 BFS with a deque - weight-0 relaxations go to the front, weight-1 relaxations to the back - computes it in linear time.

## Solution

```python
import sys
import heapq


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u = next(tokens) - 1
            v = next(tokens) - 1
            graph[u].append(v)
            graph[v].append(u)
        dist = [n + 1] * n
        dist[0] = 0
        from collections import deque
        queue = deque([0])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] > dist[u]:
                    dist[v] = dist[u]
                    queue.appendleft(v)
            for v in (u - 1, u + 1):
                if 0 <= v < n and dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        out.append(str(dist[-1]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Vertices 1 and $N$ already connected: answer 0.
- No edges at all: the answer is $N - 1$.
- A path may walk "backwards" along the labels to reach a useful component.
- Buying the same unit edge twice never helps; the shortest path uses each at most once.

## Dry run

`N = 6`, edges `1-2, 3-2, 1-3`.

Vertices 1, 2, 3 are at distance 0. From 3, the unit edges to 4, 5, 6 cost 1 each: distances 1, 2, 3.

Answer 3.

---

Same problem grouped by topic: [../docs/graphs/TRAVELLING.md](../docs/graphs/TRAVELLING.md)
