[&larr; 693. Good Sequence](693-GSEQ.md) &middot; [Index](README.md) &middot; [695. Minimum Popping &rarr;](695-DEQUEUE.md)

# 694. Treeversion

> [`TREEVERS`](https://www.codechef.com/problems/TREEVERS) &middot; difficulty **2453** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Sort child blocks by an exact cross-product comparator |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given a rooted tree with $N$ nodes (numbered $1$ through $N$); the root is node $1$. For each valid $i$, node $i$ has weight $w_i$, which is either $0$ or $1$.

We want to traverse the tree using depth first search. The order in which the nodes are visited is not uniquely defined, since we may visit the children of each node in an arbitrary order. Formally, the pseudocode of DFS-traversal is:
```
function DFS(node n):
	node n is visited
	for each node s (s is a son of n) in some order:
		call DFS(s)
	return
call DFS(root)
```

For each possible DFS-traversal of the tree, consider the sequence of weights of nodes in the order in which they are visited; each node is visited exactly once, so this sequence has length $N$. Calculate the number of inversions for each such sequence. The minimum of these numbers is the *treeversion* of our tree.

Find the treeversion of the given tree.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $w_1, w_2, \ldots, w_N$.
- Each of the following $N-1$ lines contains two space-separated integers $x$ and $y$ denoting that nodes $x$ and $y$ are connected by an edge.

**Output**
For each test case, print a single line containing one integer — the treeversion of the given tree.

**Constraints**
- $1 \le T \le 1,000$
- $1 \le N \le 10^5$
- $0 \le w_i \le 1$ for each valid $i$
- $1 \le x, y \le N$
- the graph on the input is a tree
- the sum of $N$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (50 points)**:
- $1 \le N \le 1,000$
- the sum of $N$ over all test cases does not exceed $10,000$

**Subtask #2 (50 points)**: original constraints

## Constraints

- $1 \le T \le 1,000$
- $1 \le N \le 10^5$
- $0 \le w_i \le 1$ for each valid $i$
- $1 \le x, y \le N$
- the graph on the input is a tree
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
1
3
1 0 1
1 2
1 3
```

**Sample output**

```
1
```

## Approach

Each child subtree forms one contiguous block in any DFS sequence. Suppose blocks $A,B$ contain $(o_A,z_A)$ and $(o_B,z_B)$ ones and zeros. Ordering $A$ before $B$ contributes $o_Az_B$ cross inversions, while reversing them contributes $o_Bz_A$. Sort children by this exact comparison to minimise all cross-block contributions.

In reverse tree order, first optimise every child. Start a node's merged block with its own weight, then append children in the sorted order. Add each child's internal inversions and `ones_already_seen * child_zeros`. This exchange-optimal ordering plus independent subtree optimisation gives the global minimum.

## Solution

```python
import sys
from functools import cmp_to_key


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        w = [int(next(tokens)) for _ in range(n)]
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
        ones = w[:]
        zeros = [1-x for x in w]
        inversions = [0]*n
        def compare(a,b):
            left,right = ones[a]*zeros[b],ones[b]*zeros[a]
            return (left > right)-(left < right)
        for u in reversed(order):
            children = sorted((v for v in graph[u] if v != parent[u]),key=cmp_to_key(compare))
            for v in children:
                inversions[u] += inversions[v]+ones[u]*zeros[v]
                ones[u] += ones[v]
                zeros[u] += zeros[v]
        out.append(str(inversions[0]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- A one-valued parent contributes an inversion with every zero descendant.
- Pure-one child blocks should come after blocks containing zeros.
- Cross products avoid division by zero and floating-point ratios.
- Use iterative traversal for deep trees.

## Dry run

For root weight 1 with children of weights 0 and 1, put the zero child first. Its zero still forms one unavoidable inversion with the root, so the answer is 1.

---

Same problem grouped by topic: [../docs/trees/TREEVERS.md](../docs/trees/TREEVERS.md)
