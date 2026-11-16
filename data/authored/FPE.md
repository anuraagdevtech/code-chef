---
topic: Trees
subtopic: Subtree gcds and a DP over where the removed root path continues
time: $O(N \log A)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Removing the path from the root to $v$ leaves exactly the subtrees hanging off the path: for every removed vertex, all its children that are not on the path, each as a whole subtree. The beauty of such a component is the gcd of that subtree, so first compute `subtree_gcd` for every vertex bottom-up, and for every vertex the sum of its children's subtree gcds.

Let `best[u]` be the best total obtainable inside the subtree of $u$ given that $u$ is removed. If the path stops at $u$, all children's subtrees are components: the sum of their gcds. If it continues into a child $c$, that child's gcd is replaced by `best[c]`:

$$\text{best}[u] = \sum_{c} g_c + \max\bigl(0, \max_c (\text{best}[c] - g_c)\bigr).$$

The root is always removed, so the answer is `best[1]`. The tree is processed in reverse BFS order to avoid recursion.

## Edge cases

- $N = 1$: removing the root leaves nothing and the answer is 0.
- Choosing a leaf removes it and creates no component below it.
- Continuing the path is optional - the gain may be negative.
- The total length is bounded over all test cases, so per-test allocations stay linear.

## Dry run

Sample tree: 1 has children 2, 5; 2 has 3, 4; 5 has 6, 7, 8; 7 has 9, 10. Values `15 30 15 5 3 15 3 3 5 5`.

Subtree gcds: $g_3 = 15$, $g_4 = 5$, $g_2 = 5$, $g_6 = 15$, $g_9 = g_{10} = 5$, $g_7 = 1$, $g_8 = 3$, $g_5 = 1$.

- `best[7]` = $5 + 5 = 10$.
- `best[5]` = $(15 + 1 + 3) + \max(0, 10 - 1) = 28$.
- `best[2]` = $15 + 5 = 20$.
- `best[1]` = $(5 + 1) + \max(0,\; 20 - 5,\; 28 - 1) = 33$.

Answer 33, by choosing $v = 7$.
