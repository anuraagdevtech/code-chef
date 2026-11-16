[&larr; 515. The Great Wall of Byteland](BWALL.md) &middot; [Index](../../README.md) &middot; [534. Doubly Increasing Path &rarr;](DINCPATH.md)

# 526. Subtree Removal

> CodeChef problem code [`SUBREM`](https://www.codechef.com/problems/SUBREM) &middot; difficulty **2010** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Keep a subtree optimally or remove it for one penalty |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are given a rooted tree with $N$ nodes (numbered $1$ through $N$); node $1$ is the root. Each node has a value; let's denote the value of node $i$ by $A_i$.

You may perform the following operation any number of times (including zero): choose any node which still exists in the tree and remove the whole subtree of this node including itself.

Let's define the *profit* as the sum of values of all nodes which currently exist in the tree minus $X \cdot k$, where $k$ denotes the number of times this operation was performed. Find the maximum possible profit.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- Each of the following $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.

**Output**
For each test case, print a single line containing one integer — the maximum profit.

**Constraints**
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le X \le 10^9$
- $1 \le u, v \le N$
- $|A_i| \le 10^9$ for each valid $i$
- the graph described on the input is a tree

**Subtasks**
**Subtask #1 (30 points):** $1 \le N \le 1,000$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le X \le 10^9$
- $1 \le u, v \le N$
- $|A_i| \le 10^9$ for each valid $i$
- the graph described on the input is a tree

## Sample

**Sample input**

```
1
3 5
1 -5 -10
1 2
2 3
```

**Sample output**

```
-4
```

## Approach

Let $dp[u]$ be the best profit obtainable from the subtree at $u$. Removing the entire subtree yields $-X$. Keeping $u$ yields $A_u+\sum dp[v]$ over its children, because their choices are independent.

Take the larger of those alternatives. Build a parent-first traversal iteratively and evaluate its reverse order so every child is complete before its parent.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,x = int(next(tokens)),int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1]*n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        dp = a[:]
        for u in reversed(order):
            dp[u] = max(-x,dp[u])
            if parent[u] != -1:
                dp[parent[u]] += dp[u]
        out.append(str(dp[0]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Removing the root is allowed and yields $-X$.
- A removed subtree incurs one penalty, regardless of its size.
- The optimal profit can be negative.

## Dry run

For chain values `[1,-5,-10]` and penalty 5, the leaf chooses removal, giving `-5`; its parent also chooses removal, giving `-5`; the root keeps itself and that choice, giving `1-5=-4`.

---

Same problem in rating order (#571 of 735): [../../by-rating/571-SUBREM.md](../../by-rating/571-SUBREM.md)
