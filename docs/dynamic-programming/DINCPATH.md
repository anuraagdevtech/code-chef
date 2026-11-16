[&larr; 526. Subtree Removal](SUBREM.md) &middot; [Index](../../README.md) &middot; [558. Birthday Gift &rarr;](CHEFGIFT.md)

# 534. Doubly Increasing Path

> CodeChef problem code [`DINCPATH`](https://www.codechef.com/problems/DINCPATH) &middot; difficulty **2493** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Process oriented edges in batches of equal differences |
| **Time** | $O(N+M\log M)$ per test case |
| **Space** | $O(N+M)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are given an undirected graph with $N$ nodes (numbered $1$ through $N$) and $M$ edges. Each node has a value; let's denote the value of node $i$ by $A_i$. Note that the graph is not necessarily simple.

A *doubly increasing path* is a directed path such that both the values of nodes and differences of values of nodes on this path are strictly increasing. Formally, it is a sequence of nodes $p_1, p_2, p_3, \ldots, p_k$ for some integer (the length of this path) $k \ge 1$ such that $0 \lt A_{p_2} - A_{p_1} \lt A_{p_3} - A_{p_2} \lt \ldots \lt A_{p_k} - A_{p_{k-1}}$ and for each valid $i$, nodes $p_i$ and $p_{i-1}$ are connected by an edge.

You need to find the length of the longest doubly increasing path in the graph.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- Each of the following $M$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.

**Output**
For each test case, print a single line containing one integer — the maximum length of a doubly increasing path.

**Constraints**
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le M \le 10^5$
- $1 \le u, v \le N$
- $|A_i| \le 10^{15}$ for each valid $i$

## Constraints

- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le M \le 10^5$
- $1 \le u, v \le N$
- $|A_i| \le 10^{15}$ for each valid $i$

## Sample

**Sample input**

```
2
5 4
1 2 3 4 5
2 4
1 5
1 3
3 5
5 4
1 2 3 4 5
3 5
1 2
4 5
5 2
```

**Sample output**

```
2
3
```

<details><summary>Explanation</summary>

**Example case 1:** Any path with length $2$ from a smaller node to a larger one is doubly increasing. There is no doubly increasing path with length greater than $2$.

**Example case 2:** The path $1 \rightarrow 2 \rightarrow 5$ is doubly increasing.

</details>

## Approach

Orient every edge from smaller value to larger value and discard equal-valued edges. Its weight is the positive difference. Process these edges by increasing weight, with $dp[v]$ storing the best path length ending at $v$ using processed weights.

For edges of weight $d$, propose `dp[u]+1` at each destination, but apply none of those proposals until the whole equal-weight batch has been read. This prevents consecutive differences from being equal. Every valid path is built from its last edge, so these transitions find the longest path.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            if a[u] > a[v]:
                u,v = v,u
            if a[u] < a[v]:
                edges.append((a[v]-a[u],u,v))
        edges.sort()
        dp = [1]*n
        i = 0
        while i < len(edges):
            j = i
            pending = {}
            while j < len(edges) and edges[j][0] == edges[i][0]:
                _,u,v = edges[j]
                pending[v] = max(pending.get(v,1),dp[u]+1)
                j += 1
            for v,value in pending.items():
                dp[v] = max(dp[v],value)
            i = j
        out.append(str(max(dp)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N+M\log M)$ per test case
- **Space:** $O(N+M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A path length counts vertices; isolated vertices have length one.
- Equal differences must be processed together.
- Self-loops and edges joining equal values cannot extend a path.
- Parallel edges do not change the recurrence.

## Dry run

In sample two, edge `1->2` has difference one and sets the path length at 2 to two. Edge `2->5` has difference three and extends it to three vertices.

---

Same problem in rating order (#697 of 735): [../../by-rating/697-DINCPATH.md](../../by-rating/697-DINCPATH.md)
