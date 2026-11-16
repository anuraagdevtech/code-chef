[&larr; 718. Road Decoration](718-AMR14B.md) &middot; [Index](README.md) &middot; [720. IS IT DSU HARD!! &rarr;](720-CFMAR04.md)

# 719. Graph on an Array

> [`ARRGRAPH`](https://www.codechef.com/problems/ARRGRAPH) &middot; difficulty **unrated** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Check coprime connectivity, then add a universal prime |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(N^2\log V)$ per test case with $V=50$ |
| **Space** | $O(N)$ |

## Question

You are given a sequence of integers $A_1, A_2, \dots, A_N$. You may change any number of its elements (possibly zero), obtaining a new sequence of positive integers $B_1, B_2, \dots, B_N$. Each element of $B$ must be an integer between $2$ and $50$ (both inclusive).

Let's define an undirected graph $G$ with $N$ vertices (numbered $1$ through $N$). For each pair of different vertices $i$ and $j$, there is an edge between $i$ and $j$ if and only if $B_i$ and $B_j$ are coprime.

You should choose the sequence $B$ in such a way that $G$ is a connected graph. The number of elements which need to be changed to obtain $B$ from $A$ should be minimum possible. Find one such sequence $B$ and the minimum required number of changes.

It can be proven that a solution always exists — it is always possible to modify sequence $A$ in such a way that $G$ is connected.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

**Output**
For each test case, print two lines. The first line should contain a single integer — the minimum required number of changes. The second line should contain $N$ space-separated integers $B_1, B_2, \dots, B_N$ — the modified sequence.

If there are multiple solutions, you may print any one.

**Constraints**
- $1 \le T \le 3 \cdot 10^4$
- $1 \le N \le 50$
- $2 \le A_i \le 50$ for each valid $i$

**Subtasks**
**Subtask #1 (100 points):** original constraints

**Example Input**
```
2
2
2 3
2
2 4
```

**Example Output**
```
0
2 3
1
2 3
```

**Explanation**
**Example 1**: There is an edge in $G$ between vertices $1$ and $2$. This graph is connected, so there is no need to change any elements.

**Example 2**: There is no edge between vertices $1$ and $2$ since $\mathrm{gcd}(2, 4) \neq 1$. This graph is not connected. We can change element $A_2=4$ to $3$ and make this graph connected.

## Constraints

- $1 \le T \le 3 \cdot 10^4$
- $1 \le N \le 50$
- $2 \le A_i \le 50$ for each valid $i$

## Approach

First traverse the implicit graph, adding an edge whenever two values have GCD one. If it is connected, no changes are necessary.

Otherwise one change always suffices. If 47 is absent, replace one value by 47: among allowed values 2 through 50, only 47 itself shares a factor with 47, so the new vertex is adjacent to every other vertex. If 47 is already present in a disconnected graph, every value must be 47, since any other value would connect all 47 vertices. Replace one occurrence by 43, producing a connected star. Thus the minimum is exactly zero or one.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        seen = [False]*n
        seen[0] = True
        stack = [0]
        while stack:
            u = stack.pop()
            for v in range(n):
                if not seen[v] and gcd(a[u],a[v]) == 1:
                    seen[v] = True
                    stack.append(v)
        changes = 0
        if not all(seen):
            changes = 1
            a[0] = 43 if 47 in a else 47
        out.append(str(changes))
        out.append(' '.join(map(str,a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- A single vertex is connected without changes.
- Every output value must stay between 2 and 50.
- Merely checking the GCD of all elements is insufficient for graph connectivity.

## Dry run

For `[2,3]`, the GCD-one edge already connects both vertices. For `[2,4]`, replace one value by 47; it is coprime with the other, so one change suffices.

---

Same problem grouped by topic: [../docs/constructive/ARRGRAPH.md](../docs/constructive/ARRGRAPH.md)
