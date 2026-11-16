[&larr; 213. Maximum Trio](213-MXMTRIO.md) &middot; [Index](README.md) &middot; [215. Turn It &rarr;](215-NFS.md)

# 214. Cricket Match

> [`CRIMCH`](https://www.codechef.com/problems/CRIMCH) &middot; difficulty **1350** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Bipartite colouring of every connected component |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N+M)$ per test case |
| **Space** | $O(N+M)$ |

## Question

There are $N$ people numbered from $1$ to $N$ and they want to play a cricket match between them by forming two teams that may not be of the same size. There are $M$ pairs of peoples and for each pair of peoples, they can not be in the same team. Now Chef wants to know if there is any way to split them into two teams such that Chef can organize the cricket match between two teams. If possible then print `"YES"` (without quotes), otherwise print `"NO"` (without quotes).

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- Each of the following $M$ lines follows. Each line has two space-separated numbers $u$ and $v$.

**Output**
For each test case, output in a single line the answer to the problem.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 2000$
- $1 \leq M \leq 10000$
- $1 \leq u < v \leq N$

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 2000$
- $1 \leq M \leq 10000$
- $1 \leq u < v \leq N$

## Sample

**Sample input**

```
2
3 3
1 2
1 3
2 3
4 2
1 4
2 3
```

**Sample output**

```
NO
YES
```

<details><summary>Explanation</summary>

**Example case 1:** It's impossible to divide them into two teams.

**Example case 2:** Both the teams will look like $[1, 2]$ and $[3, 4]$.

</details>

## Approach

Create an undirected edge for every pair that cannot be teammates. The requested team assignment is exactly a two-colouring in which every edge has differently coloured endpoints.

BFS or iterative DFS each unvisited component, assigning opposite colours across edges. If an edge joins equal colours, an odd cycle makes the assignment impossible. Otherwise the two colour classes are valid teams.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        colour = [-1]*n
        possible = True
        for start in range(n):
            if colour[start] != -1:
                continue
            colour[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if colour[v] == -1:
                        colour[v] = colour[u]^1
                        stack.append(v)
                    elif colour[v] == colour[u]:
                        possible = False
        out.append('YES' if possible else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Disconnected components all require checking.
- Isolated vertices can be assigned either colour.
- A triangle is impossible even when other components are bipartite.

## Dry run

The first sample is a triangle, forcing an equal-colour edge and `NO`. The second sample contains two independent edges, which can both be coloured, giving `YES`.

---

Same problem grouped by topic: [../docs/graphs/CRIMCH.md](../docs/graphs/CRIMCH.md)
