[&larr; 676. Two Piles](676-SPLITMIN.md) &middot; [Index](README.md) &middot; [678. Two Averages &rarr;](678-TWOAVG.md)

# 677. A Special Tree

> [`SPTREE`](https://www.codechef.com/problems/SPTREE) &middot; difficulty **2350** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Rerooting a "best source minus distance" value in two passes |
| **CodeChef tags** | `Algorithms`, `Graph Algos`, `Traversals`, `DFS` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + K)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given a tree with $N$ nodes (numbered $1$ through $N$). There are $K$ special nodes $f_1,f_2,\ldots,f_K$ in this tree.

We define $d(p,q)$ to be the number of edges on the unique path from node $p$ to node $q$.

You are given a node $a$. For each node $b$ from $1$ to $N$, find the maximum value of $d(a,u)-d(b,u)$ where $u$ is a special node, as well as any special node $u$ for which that maximum value is attained.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $K$, $a$.
- The second line contains $K$ space-separated integers $f_1,f_2,\ldots,f_K$.
- $N-1$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $u_i$ and $v_i$ denoting an edge of the tree.

**Output**

For each test case, print two lines.

In the first line print $N$ space-separated integers. For each valid $i$, the $i$-th integer should be the maximum value of $d(a,u)-d(i,u)$ where $u$ is a special node.

In the second line print $N$ space-separated integers. For each valid $i$, the $i$-th integer should be any special node $u$ for which the maximum of $d(a,u)-d(i,u)$ is attained.

## Constraints

- $1 \le T \le 200$
- $1 \le K \le N \le 2 \cdot 10^5$
- $1 \le a \le N$
- $1 \le f_i \le N$ for each valid $i$
- $f_i \neq f_j$ for each valid $i$ and $j$ such that $i \neq j$
- $1 \le u_i,v_i \le N$ for each valid $i$
- the graph described on the input is a tree
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^5$

**Subtasks**

**Subtask #1 (10 points):**
- $T \le 11$
- $N \le 200$
- the sum of $N$ over all test cases does not exceed $400$

**Subtask #2 (20 points):**
- $T \le 51$
- $N \le 2000$
- the sum of $N$ over all test cases does not exceed $4000$

**Subtask #3 (30 points):**
- It holds that $u_i=i$, $v_i=i+1$ for each valid $i$.

**Subtask #4 (40 points):** original constraints

## Sample

**Sample input**

```
2
5 1 3
2
1 2
1 3
2 4
2 5
8 3 2
6 5 8
1 2
2 3
2 4
2 5
4 6
5 7
5 8
```

**Sample output**

```
1 2 0 1 1
2 2 2 2 2
-1 0 -1 1 1 2 0 2
5 5 5 6 5 6 5 8
```

<details><summary>Explanation</summary>

**Example case 1:**  The following picture shows the tree in the first example case with special nodes in bold:

<img src="https://s3.amazonaws.com/codechef_shared/download/Images/LTIME95/SPTREE/SPTREE_1.png">

The only special node is the node $2$ and $a=3$. Therefore, the desired maximum is $d(a,2)-d(b,2)=d(3,2)-d(b,2)=2-d(b,2)$ for each node $b$ and it is always attained for the special node $u=2$.

**Example case 2:** The following picture shows the tree in the second example case with special nodes bolded:

<img src="https://s3.amazonaws.com/codechef_shared/download/Images/LTIME95/SPTREE/SPTREE_2.png">

The special nodes are $6$, $5$ and $8$, and $a=2$. The maximum values of $d(a,u)-d(b,u)$ ($u$ being a special node) for each $b$ are as follows:

- $b=1$: The maximum value of $d(2,u)-d(1,u)$ is $-1$ and it is achieved for $u=5$ since $d(2,5)-d(1,5)=1-2=-1$.

- $b=2$: The maximum value of $d(2,u)-d(2,u)$ is $0$ and it is achieved for $u=5$ since $d(2,5)-d(2,5)=1-1=0$.

- $b=3$: The maximum value of $d(2,u)-d(3,u)$ is $-1$ and it is achieved for $u=5$ since $d(2,5)-d(3,5)=1-2=-1$.

- $b=4$: The maximum value of $d(2,u)-d(4,u)$ is $1$ and it is achieved for $u=6$ since $d(2,6)-d(4,6)=2-1=1$.

- $b=5$: The maximum value of $d(2,u)-d(5,u)$ is $1$ and it is achieved for $u=5$ since $d(2,5)-d(5,5)=1-0=1$.

- $b=6$: The maximum value of $d(2,u)-d(6,u)$ is $2$ and it is achieved for $u=6$ since $d(2,6)-d(6,6)=2-0=2$.

- $b=7$: The maximum value of $d(2,u)-d(7,u)$ is $0$ and it is achieved for $u=5$ since $d(2,5)-d(7,5)=1-1=0$.

- $b=8$: The maximum value of $d(2,u)-d(8,u)$ is $2$ and it is achieved for $u=8$ since $d(2,8)-d(8,8)=2-0=2$.

</details>

## Approach

For a special node $u$ the term $d(a, u)$ does not depend on $b$. Give every special node the weight $w_u = d(a, u)$; then the quantity asked for at $b$ is

$$\max_u \bigl(w_u - d(b, u)\bigr),$$

the classic "best source, losing one per edge" problem on a tree.

Root the tree at $a$; a BFS gives the depths, which are exactly $d(a, \cdot)$, and an order for the two passes. Initialise `value[u] = depth[u]` and `witness[u] = u` for special nodes, minus infinity elsewhere.

- Bottom-up: a node takes the best value of its children minus one - this accounts for all sources inside its subtree.
- Top-down: a node takes its parent's final value minus one if that is better - this brings in the sources outside its subtree. If the parent's best source lies inside the child's own subtree, the offer is two worse than what the child already has and is ignored, so no "second best" bookkeeping is needed.

The witness is copied along with every improvement, giving a special node that attains the maximum.

## Solution

```python
import sys
from collections import deque


def solve(tokens):
    n, k, anchor = (next(tokens), next(tokens), next(tokens) - 1)
    special = [next(tokens) - 1 for _ in range(k)]
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = (next(tokens) - 1, next(tokens) - 1)
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    order = [anchor]
    parent[anchor] = anchor
    for u in order:
        for v in graph[u]:
            if parent[v] < 0:
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)
    value = [-10 ** 9] * n
    witness = [-1] * n
    for u in special:
        value[u] = depth[u]
        witness[u] = u
    for u in reversed(order[1:]):
        up = parent[u]
        if value[u] - 1 > value[up]:
            value[up] = value[u] - 1
            witness[up] = witness[u]
    for u in order[1:]:
        up = parent[u]
        if value[up] - 1 > value[u]:
            value[u] = value[up] - 1
            witness[u] = witness[up]
    return ' '.join(map(str, value)) + '\n' + ' '.join((str(x + 1) for x in witness))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- For $b = a$ every special node gives 0, so the value is 0.
- Values can be negative when all special nodes are closer to $a$ than to $b$.
- Any maximising special node may be printed, so the second line is checked by a validator.
- The tree is processed iteratively to avoid deep recursion.

## Dry run

Edges `1-2, 1-3, 2-4, 2-5`, $a = 3$, the only special node is 2 with weight $d(3, 2) = 2$.

Subtracting the distance from node 2: node 2 gets 2, nodes 1, 4, 5 get 1, node 3 gets 0.

Output `1 2 0 1 1` and the witness `2` for every node.

---

Same problem grouped by topic: [../docs/trees/SPTREE.md](../docs/trees/SPTREE.md)
