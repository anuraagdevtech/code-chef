[&larr; 539. Graph on an Array](ARRGRAPH.md) &middot; [Index](../../README.md) &middot; [571. Yet Another Problem About Sequences &rarr;](EARTSEQ.md)

# 545. Path-etic Sums

> CodeChef problem code [`PATHSUMS`](https://www.codechef.com/problems/PATHSUMS) &middot; difficulty **1838** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Assign one and two to the two tree colour classes |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are given a tree with $N$ nodes (numbered $1$ through $N$). A tree is a connected undirected graph without cycles.

You have to assign an integer to each node; for each valid $i$, let's denote the integer assigned to node $i$ by $A_i$. This assignment must satisfy the following conditions:
- For each valid $i$, $1 \le A_i \le 10^5$.
- For each simple path in the tree which contains at least two nodes, let's denote the set of nodes in this path by $S$. Then, $\sum_{v \in S} A_v$ is not divisible by $|S|$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- Each of the next $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.

**Output**
For each test case, print a single line containing $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

If there are multiple solutions, you may find any one of them. It can be proved that a solution always exists under the given constraints.

**Constraints**
- $1 \le T \le 200$
- $2 \le N \le 100$
- $1 \le u, v \le N$

## Constraints

- $1 \le T \le 200$
- $2 \le N \le 100$
- $1 \le u, v \le N$

## Sample

**Sample input**

```
2
7
1 2
4 6
3 5
1 4
7 5
5 1
3
1 2
2 3
```

**Sample output**

```
4 9 12 1 9 8 4
4 3 6
```

<details><summary>Explanation</summary>

**Example case 1:**
<img src="https://codechef_shared.s3.amazonaws.com/download/Images/COOK123/PATHSUMS/pathetic.png" alt="pathetic.png" />
This assignment satisfies all the conditions. For example, for the path $3 \rightarrow 5 \rightarrow 1 \rightarrow 2$, the sum $12 + 9  + 4 + 9 = 34$ is not divisible by $4$ (the number of nodes in the path).

</details>

## Approach

Two-colour the tree and assign value one to one class and value two to the other. Every path containing at least two vertices includes an edge, hence includes both values. Its average is strictly between one and two, so it cannot be an integer. Therefore the path sum is not divisible by its vertex count.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        answer = [0]*n
        answer[0] = 1
        stack = [0]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if answer[v] == 0:
                    answer[v] = 3-answer[u]
                    stack.append(v)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Single-vertex paths are excluded by the condition.
- Either colour may receive value one.
- Values one and two satisfy the output bound.

## Dry run

For path `1-2-3`, assign `[1,2,1]`. Its two-edge subpaths have sums 3 over two vertices, and the full path has sum 4 over three vertices; none is divisible by its length.

> CodeChef tags: `Data Structures`, `Graphs`, `Algorithms`, `Graph Algos`, `Traversals`

---

Same problem in rating order (#532 of 735): [../../by-rating/532-PATHSUMS.md](../../by-rating/532-PATHSUMS.md)
