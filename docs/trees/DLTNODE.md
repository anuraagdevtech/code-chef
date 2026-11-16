[&larr; 649. Full Path Eraser](FPE.md) &middot; [Index](../../README.md) &middot; [713. A Special Tree &rarr;](SPTREE.md)

# 672. Sardar and GCD

> CodeChef problem code [`DLTNODE`](https://www.codechef.com/problems/DLTNODE) &middot; difficulty **2190** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Rerooting - subtree gcds below, complement gcds above |
| **Time** | $O(N \log A)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Sardar Khan has finally decided to attack Ramadhir - he will bomb one of Ramadhir's businesses in Wasseypur. Sardar Khan knows that Ramadhir has $N$ businesses (numbered $1$ to $N$) and that there are $N - 1$ roads connecting pairs of these businesses in such a way that all businesses are connected. Further, Sardar knows that each business has a specific value - the $i$-th business has value $A_i$.

When Sardar Khan destroys a business, he also destroys every road directly connected to it.
Formally, destroying business $v$ also destroys all existing roads of the form $(u, v)$.

Sardar thinks that the damage dealt to Ramadhir upon destroying business $v$ equals the sum of the [greatest common divisors](https://en.wikipedia.org/wiki/Greatest_common_divisor) of every remaining maximal connected set of businesses. More formally,
* Let the connected components of the graph obtained on deleting $v$ and edges incident to it be $C_1, C_2, \dots, C_k$.
* Define $\gcd(C_i)$ to be $\gcd(A_{i_1}, A_{i_2}, \dots, A_{i_r})$ where $C_i$ consists of vertices $i_1, i_2, \dots, i_r$.
* The damage caused by destroying $v$ is then $\sum_{i = 1}^k \gcd(C_i)$.

Sardar Khan wants to maximize the damage he deals. Can you find the maximum possible damage he can achieve, given that he destroys **exactly one** business?

If the process of computing damage is still unclear, please refer to sample test cases for an explained example.

**Input**

- The first line of input contains an integer $T$, denoting the total number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$, denoting the number of businesses Ramadhir owns.
- Each of the next $N-1$ lines contains $2$ integers $a$ and $b$, denoting a road between businesses $a$ and $b$.
- Finally, the last line of each test case contains $N$ space-separated positive integers $A_1, A_2, \ldots, A_N$, where $A_i$ is the value of the $i$-th business.

**Output**

- For each test case, output a single line containing one integer - the maximum possible damage that Sardar Khan can deal.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases will not exceed $5 \cdot 10^5$.
- It is guaranteed that the given roads connect every business.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
1
5
1 2
1 3
3 4
3 5
4 6 8 12 15
```

**Sample output**

```
29
```

<details><summary>Explanation</summary>

* If business $1$ is bombed, the remaining connected components are $\{(2), (3, 4, 5)\}$. This gives a damage of $\gcd(A_2) + \gcd(A_3, A_4, A_5) = 6 + 1 = 7$.
* If business $2$ is bombed, the remaining connected components are $\{(1, 3, 4, 5)\}$. This gives a damage of $\gcd(A_1, A_3, A_4, A_5) = 1$.
* If business $3$ is bombed, the remaining connected components are $\{(1, 2), (4), (5)\}$. This gives a damage of $\gcd(A_1, A_2) + \gcd(A_4) + \gcd(A_5) = 2 + 12 + 15 = 29$.
* If business $4$ is bombed, the remaining connected components are $\{(1, 2, 3, 5)\}$. This gives a damage of $\gcd(A_1, A_2, A_3, A_5) = 1$.
* If business $5$ is bombed, the remaining connected components are $\{(1, 2, 3, 4)\}$. This gives a damage of $\gcd(A_1, A_2, A_3, A_4) = 2$.

Clearly, bombing business $3$ gives the maximum possible damage, that being 29.

</details>

## Approach

Destroying vertex $u$ leaves one component per child of $u$ - that child's whole subtree - and, unless $u$ is the root, one component containing everything outside the subtree of $u$. The damage is the sum of the gcds of these components.

Subtree gcds come from a bottom-up pass. For the outside part define `outside[v]` as the gcd of all vertices not in the subtree of $v$. For a child $v$ of $u$ it is the gcd of `outside[u]`, the value of $u$, and the subtree gcds of all *other* children of $u$. Computing "all but one" for every child with prefix and suffix gcds over the child list keeps this linear even at vertices of high degree.

The answer is the maximum over $u$ of `outside[u]` plus the sum of its children's subtree gcds; for the root the outside part is empty and counts 0.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = next(tokens) - 1
            v = next(tokens) - 1
            graph[u].append(v)
            graph[v].append(u)
        values = [next(tokens) for _ in range(n)]
        parent = [-1] * n
        order = [0]
        parent[0] = 0
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        subtree_gcd = values[:]
        outside_gcd = [0] * n
        for u in reversed(order[1:]):
            subtree_gcd[parent[u]] = gcd(subtree_gcd[parent[u]], subtree_gcd[u])
        best = 0
        for u in order:
            children = [v for v in graph[u] if parent[v] == u]
            best = max(best, outside_gcd[u] + sum((subtree_gcd[v] for v in children)))
            prefix = [gcd(outside_gcd[u], values[u])]
            for v in children:
                prefix.append(gcd(prefix[-1], subtree_gcd[v]))
            suffix = 0
            for i in range(len(children) - 1, -1, -1):
                v = children[i]
                outside_gcd[v] = gcd(prefix[i], suffix)
                suffix = gcd(suffix, subtree_gcd[v])
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \log A)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Destroying a leaf leaves a single component.
- The root has no outside component.
- A star's centre has many children; the prefix/suffix trick avoids a quadratic scan there.
- In this problem the edges come before the values in the input.

## Dry run

Edges `1-2, 1-3, 3-4, 3-5`, values `4 6 8 12 15`.

Subtree gcds (root 1): $g_2 = 6$, $g_4 = 12$, $g_5 = 15$, $g_3 = \gcd(8, 12, 15) = 1$.

- Destroy 1: $g_2 + g_3 = 7$.
- Destroy 3: outside is $\gcd(4, 6) = 2$; children give $12 + 15$; total 29.
- Destroying 2, 4 or 5 leaves one component with gcd 1.

Answer 29.

> CodeChef tags: `Data Structures`, `Graphs`, `Advanced Algorithms`, `Mathematics`, `Number Theory`, `Algorithms`, `Graph Algos`, `Traversals`, `Simple Algos`

---

Same problem in rating order (#632 of 735): [../../by-rating/632-DLTNODE.md](../../by-rating/632-DLTNODE.md)
