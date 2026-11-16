[&larr; 533. Tourists in Mancunia](TOURISTS.md) &middot; [Index](../../README.md) &middot; [536. Chef and Digit Jumps &rarr;](DIGJUMP.md)

# 535. Chef and Reversing

> CodeChef problem code [`REVERSE`](https://www.codechef.com/problems/REVERSE) &middot; difficulty **1879** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | 0-1 BFS on original and reversed edge choices |
| **Time** | $O(N+M)$ overall |
| **Space** | $O(N+M)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Sometimes mysteries happen. Chef found a directed graph with **N** vertices and **M** edges in his kitchen!

The evening was boring and chef has nothing else to do, so to entertain himself, Chef thought about a question "What is the minimum number of edges he needs to reverse in order to have at least one path from vertex **1** to vertex **N**, where the vertices are numbered from **1** to **N**.

**Input**

Each test file contains only one test case.

The first line of the input contains two space separated integers **N** and **M**, denoting the number of vertices and the number of edges in the graph respectively. The **i**^th line of the next **M** lines contains two space separated integers **X_i** and **Y_i**, denoting that the **i**^th edge connects vertices from **X_i** to **Y_i**.

**Output**

In a single line, print the minimum number of edges we need to revert. If there is no way of having at least one path from **1** to **N**, print **-1**.

**Constraints**

- **1 ≤ N, M ≤ 100000 = 10^5**

- **1 ≤ X_i, Y_i ≤ N**

- There can be multiple edges connecting the same pair of vertices, There can be self loops too i.e. ** X_i = Y_i**

## Constraints

- 1 ≤ N, M ≤ 100000 = 10^5
- 1 ≤ X_i, Y_i ≤ N
- There can be multiple edges connecting the same pair of vertices, There can be self loops too i.e.  X_i = Y_i

## Sample

**Sample input**

```
7 7
1 2 
3 2
3 4
7 4
6 2
5 6
7 5
```

**Sample output**

```
2
```

<details><summary>Explanation</summary>

We can consider two paths from **1** to **7**:

-  **1-2-3-4-7**

-  **1-2-6-5-7**

In the first one we need to revert edges **(3-2), (7-4)**. In the second one - **(6-2), (5-6), (7-5)**. So the answer is  **min(2, 3) = 2**.

</details>

## Approach

Keep each original directed edge with traversal cost zero and add its reverse with cost one. A path's total cost is precisely the number of edge reversals it requires. Therefore the requested answer is the shortest path from 1 to $N$ in this 0-1 weighted graph.

Use a deque: a zero-cost improvement goes to the front, and a one-cost improvement goes to the back. Skip stale distance entries. If the destination stays unreachable, output minus one.

## Solution (Python)

```python
import sys
from collections import deque


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = next(tokens)-1,next(tokens)-1
        graph[u].append((v,0))
        graph[v].append((u,1))
    distance = [n+m+1]*n
    distance[0] = 0
    queue = deque([(0,0)])
    while queue:
        current,u = queue.popleft()
        if current != distance[u]:
            continue
        for v,cost in graph[u]:
            candidate = current+cost
            if candidate < distance[v]:
                distance[v] = candidate
                if cost:
                    queue.append((candidate,v))
                else:
                    queue.appendleft((candidate,v))
    print(distance[-1] if distance[-1] < n+m+1 else -1)

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N+M)$ overall
- **Space:** $O(N+M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Original and reverse edges may both exist.
- Self-loops never help lower a shortest path.
- If source equals destination, zero reversals suffice.
- Reversals cannot connect separate undirected components.

## Dry run

The sample path `1-2-3-4-7` uses reverse directions for edges `3->2` and `7->4`, giving cost two.

---

Same problem in rating order (#544 of 735): [../../by-rating/544-REVERSE.md](../../by-rating/544-REVERSE.md)
