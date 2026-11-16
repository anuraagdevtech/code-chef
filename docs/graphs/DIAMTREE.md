[&larr; 518. Snakes and transition from Capitalism to Socialism](SNSOCIAL.md) &middot; [Index](../../README.md) &middot; [521. Root the Tree &rarr;](ROOTTREE.md)

# 520. Find Tree Diameter

> CodeChef problem code [`DIAMTREE`](https://www.codechef.com/problems/DIAMTREE) &middot; difficulty **1620** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Two breadth-first searches find a tree diameter |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You're given a tree with $N$ vertices numbered from $1$ to $N$. A tree is defined as a connected, undirected graph with $N$ vertices and $N-1$ edges. The distance between two vertices in a tree is equal to the number of edges on the unique simple path between them.

The diameter of a tree is the maximum distance between two nodes. Your task is to determine the diameter of the tree.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- Each of the following $N−1$ lines contains two space-separated integers $u$ and $v$ denoting an edge between nodes $u$ and $v$.

**Output**
For each test case, output in a single line the answer to the problem - the diameter of the tree.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq u, v \leq N$

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq u, v \leq N$

## Sample

**Sample input**

```
2
6
1 2
1 3
2 4
2 5
3 6
5
1 2
1 3
3 4
3 5
```

**Sample output**

```
4
3
```

<details><summary>Explanation</summary>

**Example case 1:** The structure of the given tree is shown below.
<img src="https://s3.amazonaws.com/discourseproduction/original/2X/d/d932b48ade701ee947490515af1060eacddd98ca.png" class="center" width="300" height="250">
- The diameter corresponds to the path $4?2?1?3?6$ or $5?2?1?3?6$.

</details>

## Approach

In a tree, a vertex farthest from any chosen start is an endpoint of some diameter. BFS once from vertex 1 to locate such an endpoint, then BFS from it. The largest distance in the second search is the diameter.

Store distances rather than recurse, so a chain of $10^5$ vertices does not overflow Python's call stack.

## Solution (Python)

```python
import sys
from collections import deque


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
        def farthest(start):
            distance = [-1]*n
            distance[start] = 0
            queue = deque([start])
            last = start
            while queue:
                last = queue.popleft()
                for v in graph[last]:
                    if distance[v] == -1:
                        distance[v] = distance[last]+1
                        queue.append(v)
            return last,distance[last]
        endpoint,_ = farthest(0)
        _,diameter = farthest(endpoint)
        out.append(str(diameter))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A one-vertex tree has diameter zero.
- Count edges, not vertices on the path.
- Multiple farthest endpoints are interchangeable.

## Dry run

The first sample has path `4-2-1-3-6`, containing four edges. Two BFS traversals return diameter four.

---

Same problem in rating order (#369 of 735): [../../by-rating/369-DIAMTREE.md](../../by-rating/369-DIAMTREE.md)
