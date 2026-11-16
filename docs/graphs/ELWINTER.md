[&larr; 561. Soccer League](M3.md) &middot; [Index](../../README.md) &middot; [655. Travelling in the Graph &rarr;](TRAVELLING.md)

# 625. Winter

> CodeChef problem code [`ELWINTER`](https://www.codechef.com/problems/ELWINTER) &middot; difficulty **2007** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Lazy multi-source BFS driven by a time-ordered heap |
| **Time** | $O((N + M) \log N + Q)$ |
| **Space** | $O(N + M)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Uneori îmi spun: am să mor
atât de singuratecă-n mijlocul lor;
limba simplă a bucuriilor n-am învâțat;
am să mor ca o pasăre care prea mult a zburat,
dar n-a făcut cuib nicăieri.

― Oamenii ma uimesc, Magda Isafost
__________________________________________________________

As of writing the informal statement, the winter just came and the statement was in season. Now, it is not winter anymore, so here is the formal statement instead:

You are given a connected graph with $N$ nodes and $M$ edges. You are given $Q$ queries of the following types:
- $\texttt{1 u}$: Given node $u$ $(1 \leq u \leq N)$, set the state of the node $u$ to frozen.
- $\texttt{2 t}$: Given $t$, let $t$ units of time pass by.
- $\texttt{3 v}$: Given node $v$ $(1 \leq v \leq N)$, answer if node $v$ is currently frozen.

Initially, **no** node is frozen.
The graph has the following property:
- If, at time $T$, a node $u$ is frozen, then, at time $(T+1)$, **all neighbours** of $u$ become frozen.

For each query of type $3$, answer whether the node is currently frozen.

**Note:**
- If a node is already frozen, it remains unaffected after a type $1$ query.
- If, for a frozen node $u$, a neighbour $v$ of node $u$ is frozen at time $T$, node $v$ remains unaffected at time $(T+1)$.

**Input**

- The first line of input contains three integers $N, M,$ and $Q$.
- $M$ lines follow, the $i^{th}$ of which contains two integers $u_i$ and $v_i$, representing there is an edge between nodes $u_i$ and $v_i$.
- Then, $Q$ lines follow, the $j^{th}$ of which contains two integers $type_j$ and $x_j$.
If $type_j$ is $1$ or $2$, it indicates that you must effectuate an update of the type $type_j$ with parameter $x_j$. Otherwise, answer the query with parameter $x_j$

**Output**

For each query of type $3$, print $\texttt{YES}$ if the queried node is frozen. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

## Constraints

- $1 \le N, Q \le 10^5$
- $1 \le M \le 3 \cdot 10^5$
- $1 \le u_i, v_i \le N$
- $1 \le type_j \le 3$
- $1 \le x_j \le N$, if the query type is $1$ or $3$.
- $1 \le x_j \le 10^9$, if the query type is $2$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \le N \le 1000, 1 \le Q \le 2000, 1 \le M \le 3000$.
- **Subtask 2 (30 points):** Each node in the given graph has **at most two** neighbours.
- **Subtask 3 (60 points):** Original constraints.

## Sample

**Sample input**

```
6 6 6
1 2
2 3
4 1
5 4
6 1
6 5
1 1
3 1
1 5
2 1
3 4
3 3
```

**Sample output**

```
YES
YES
NO
```

<details><summary>Explanation</summary>

**Test Case $1$:** The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine4.png)
- Query $1$: Freeze the node $1$. The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine2.png)
- Query $2$: Find the status of node $1$. Since node $1$ is frozen, we print $\texttt{YES}$.
- Query $3$: Freeze the node $5$. The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine5.png)
- Query $4$: $1$ unit of time passes. Before this, nodes $1$ and $5$ were frozen.
After $1$ second, all the neighbours of node $1$, i.e., nodes $2, 4,$ and $6$, and all the neighbours of node $5$, i.e., nodes $4$ and $6$ are frozen.
Thus, after this query, the frozen nodes in the graph are $1, 2, 4, 5,$ and $6$. The graph looks like:
![](https://s3.amazonaws.com/codechef_shared/download/Images/LTIME106/cine3.png)
- Query $5$: Find the status of node $4$. Since node $4$ is frozen, we print $\texttt{YES}$.
- Query $6$: Find the status of node $3$. Since node $3$ is not frozen, we print $\texttt{NO}$.

</details>

## Approach

Freezing spreads one edge per unit of time from every frozen node, so this is a multi-source BFS in which new sources appear over time and the clock only advances on type-2 queries.

Keep a clock `now` and a min-heap of (freeze time, node) for nodes whose neighbours have not been processed yet. A type-1 query freezes the node immediately and pushes it with the current time. A type-2 query advances the clock by $t$ and then pops every event whose time is strictly less than the new `now`: such a node has had at least one full unit of time to spread, so each unfrozen neighbour is frozen and pushed with time + 1. A type-3 query just reads the flag.

Every node is pushed once and every edge is scanned at most twice, regardless of how large the time jumps are.

## Solution (Python)

```python
import sys
import sys, heapq


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    m = next(tokens)
    q = next(tokens)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(tokens) - 1
        v = next(tokens) - 1
        graph[u].append(v)
        graph[v].append(u)
    frozen = [False] * n
    events = []
    now = 0
    out = []
    for _ in range(q):
        kind = next(tokens)
        x = next(tokens)
        if kind == 1:
            if not frozen[x - 1]:
                frozen[x - 1] = True
                heapq.heappush(events, (now, x - 1))
        elif kind == 2:
            now += x
            while events and events[0][0] < now:
                t, u = heapq.heappop(events)
                for v in graph[u]:
                    if not frozen[v]:
                        frozen[v] = True
                        heapq.heappush(events, (t + 1, v))
        else:
            out.append('YES' if frozen[x - 1] else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O((N + M) \log N + Q)$
- **Space:** $O(N + M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Time jumps can be $10^9$; the loop is bounded by the graph, not by $t$.
- Freezing an already frozen node does nothing.
- An event with time equal to `now` has not spread yet and stays in the heap.
- Whether a node is frozen never needs its exact freeze time - marking it early while processing in time order is safe because the pending event keeps the correct time.

## Dry run

Sample graph with edges `1-2, 2-3, 4-1, 5-4, 6-1, 6-5`.

- `1 1`: node 1 frozen at time 0. `3 1` answers YES.
- `1 5`: node 5 frozen at time 0.
- `2 1`: the clock becomes 1. Events (0, 1) and (0, 5) are popped: nodes 2, 4, 6 freeze with time 1. Those events are not earlier than 1, so they wait.
- `3 4`: YES. `3 3`: NO - node 3 would freeze at time 2.

> CodeChef tags: `Algorithms`, `Graph Algos`, `Traversals`, `BFS`, `Queries`

---

Same problem in rating order (#569 of 735): [../../by-rating/569-ELWINTER.md](../../by-rating/569-ELWINTER.md)
