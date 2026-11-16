[&larr; 558. Little Elephant and Mouses](558-LEMOUSE.md) &middot; [Index](README.md) &middot; [560. String Merging &rarr;](560-STRMRG.md)

# 559. Even Edges

> [`EVEDG`](https://www.codechef.com/problems/EVEDG) &middot; difficulty **1945** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Parity of the edge count and vertex degrees |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N+M)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has a simple undirected graph with $N$ vertices (numbered $1$ through $N$) and $M$ edges. He wants to divide it into $K$ parts (subgraphs) for some integer $K$.

First, Chef divides the vertices in the graph into $K$ sets such that each vertex belongs to exactly one set; the subgraphs and sets are numbered $1$ through $K$ such that for each valid $i$, vertices from the $i$-th set belong to the $i$-th subgraph. Then, Chef checks all the edges in the graph. For an edge connecting vertices $u$ and $v$, if $u$ and $v$ are both in the $i$-th set, then this edge belongs to the $i$-th subgraph. Otherwise, this edge does not belong to any of these $K$ subgraphs.

At the end, Chef checks these $K$ subgraphs. If each subgraph contains an even number of edges, then Chef thinks that this way of dividing the graph is *delicious*.

Chef wants to divide the graph in a delicious way such that $K$ is the smallest possible. Find the minimum $K$ and one such way to divide the graph.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- Each of the next $M$ lines contains two space-separated integers $u$ and $v$ denoting that vertices $u$ and $v$ are connected by an edge.

**Output**
For each test case, print two lines. The first of these lines should contain a single integer ― the minimum $K$. The second line should contain $N$ space-separated integers, where for each valid $i$, the $i$-th integer denotes the subgraph that vertex $i$ belongs to.

If there are multiple solutions, you may output any one.

**Constraints**
- $1 \le T \le 3,000$
- $1 \le M \le 100,000$
- $2 \le N \le 100,000$
- $1 \le u \neq v \le N$
- the graph contains no duplicate edges or self-loops
- the sum of $N$ over all test cases does not exceed $10^6$
- the sum of $M$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (30 pts):** $2 \le N \le 10$

**Subtask #2 (70 pts):** original constraints

## Constraints

- $1 \le T \le 3,000$
- $1 \le M \le 100,000$
- $2 \le N \le 100,000$
- $1 \le u \neq v \le N$
- the graph contains no duplicate edges or self-loops
- the sum of $N$ over all test cases does not exceed $10^6$
- the sum of $M$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
1
5 5
1 2
1 3
2 3
2 4
3 4
```

**Sample output**

```
2
1 2 1 1 2
```

<details><summary>Explanation</summary>

**Example case 1:** Subgraph $1$ contains vertices $1$, $3$, $4$ and edges $(1,3)$ and $(3,4)$. Subgraph $2$ contains vertices $2$ and $5$, but no edges.

</details>

## Approach

If $M$ is even, one part already works. If $M$ is odd and some vertex has odd degree, place it alone: removing its incident odd number of edges leaves an even number in the other part.

If every degree is even, two parts cannot work: any cut has even size, so its two induced edge counts sum to an odd number. Three parts suffice. Choose any edge $(u,v)$ and put its endpoints in separate singleton parts. Removing their incident edges deletes $deg(u)+deg(v)-1$ edges, an odd number, leaving an even edge count in the remaining part.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        degree = [0]*n
        first = None
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            degree[u] += 1
            degree[v] += 1
            if first is None:
                first = (u,v)
        labels = [1]*n
        if m%2 == 0:
            k = 1
        else:
            odd = next((u for u in range(n) if degree[u]%2),None)
            if odd is not None:
                k = 2
                labels[odd] = 2
            else:
                k = 3
                u,v = first
                labels[u],labels[v] = 2,3
        out.append(str(k))
        out.append(' '.join(map(str,labels)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Singleton parts have zero edges, which is even.
- Use any input edge when all degrees are even and $M$ is odd.
- Isolated vertices may remain in the main part.

## Dry run

In the sample, $M=5$ and vertex 2 has degree three. Put vertex 2 alone; the other part retains two edges, so two parts suffice.

---

Same problem grouped by topic: [../docs/constructive/EVEDG.md](../docs/constructive/EVEDG.md)
