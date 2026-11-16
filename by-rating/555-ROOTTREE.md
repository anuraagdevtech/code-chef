[&larr; 554. Appy Loves One](554-HMAPPY1.md) &middot; [Index](README.md) &middot; [556. Moving Segments &rarr;](556-SEGDIR.md)

# 555. Root the Tree

> [`ROOTTREE`](https://www.codechef.com/problems/ROOTTREE) &middot; difficulty **1934** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Count excess incoming edges in a directed tree |
| **CodeChef tags** | `Data Structures`, `Graphs`, `Algorithms`, `Constructive`, `Directed Graphs`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

A *directed tree* is a directed graph such that if all edges were undirected, this graph would be a tree. A *rooted directed tree* is a directed tree in which there is one vertex (the *root*, let's denote it by $r$) such that it is possible to reach all vertices of the graph from $r$ by moving along the directed edges.

You are given a directed tree with $N$ vertices (numbered $1$ through $N$). You may perform the following operation on it any number of times (including zero):
- Choose some edge which currently exists in the graph.
- Remove this edge.
- Add a new edge in such a way that the graph becomes a directed tree again.

What is the smallest number of operations which need to be performed in order to make the directed tree rooted?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- Each of the next $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that there is a directed edge from $u$ to $v$ in the tree.

**Output**
For each test case, print a single line containing one integer ― the smallest number of operations we need to perform to create a rooted directed tree.

**Constraints**
- $1 \le N \le 10^4$
- $1 \le u, v \le N$
- the graph described on the input is a directed tree
- the sum of $N$ over all test cases does not exceed $10^5$

**Subtasks**
**Subtask #1 (20 points):** for each edge, $u = 1$ or $v = 1$ (the graph is a directed star)

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le N \le 10^4$
- $1 \le u, v \le N$
- the graph described on the input is a directed tree
- the sum of $N$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
2
3
1 2
3 2
3
1 2
2 3
```

**Sample output**

```
1
0
```

<details><summary>Explanation</summary>

**Example case 1:** We can delete the edge from vertex $3$ to vertex $2$ and insert an edge from $3$ to $1$. Then, the graph becomes a rooted directed tree with vertex $3$ as the root. However, there are many other possible solutions.

**Example case 2:** The graph is already a rooted directed tree; the root is vertex $1$.

</details>

## Approach

A rooted outward tree has one vertex of indegree zero and indegree one everywhere else. If the current tree has $s$ zero-indegree vertices, its total excess indegree is $s-1$, because it has $N-1$ edges.

At least $s-1$ edges must be replaced to supply incoming edges to all but one source. This is attainable by removing excess incoming edges, leaving outward-rooted components, then connecting those components into one outward tree. Hence the answer is the number of sources minus one.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        indegree = [0]*n
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            indegree[v] += 1
        out.append(str(sum(d == 0 for d in indegree)-1))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- The root may be any vertex.
- Edges may be reattached, rather than only reversed.
- A single vertex already forms a rooted tree.

## Dry run

For edges `1->2` and `3->2`, sources are 1 and 3, so one replacement suffices. The chain `1->2->3` has one source and needs zero.

---

Same problem grouped by topic: [../docs/graphs/ROOTTREE.md](../docs/graphs/ROOTTREE.md)
