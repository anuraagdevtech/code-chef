---
topic: Trees
subtopic: Rerooting a "best source minus distance" value in two passes
time: $O(N + K)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a special node $u$ the term $d(a, u)$ does not depend on $b$. Give every special node the weight $w_u = d(a, u)$; then the quantity asked for at $b$ is

$$\max_u \bigl(w_u - d(b, u)\bigr),$$

the classic "best source, losing one per edge" problem on a tree.

Root the tree at $a$; a BFS gives the depths, which are exactly $d(a, \cdot)$, and an order for the two passes. Initialise `value[u] = depth[u]` and `witness[u] = u` for special nodes, minus infinity elsewhere.

- Bottom-up: a node takes the best value of its children minus one - this accounts for all sources inside its subtree.
- Top-down: a node takes its parent's final value minus one if that is better - this brings in the sources outside its subtree. If the parent's best source lies inside the child's own subtree, the offer is two worse than what the child already has and is ignored, so no "second best" bookkeeping is needed.

The witness is copied along with every improvement, giving a special node that attains the maximum.

## Edge cases

- For $b = a$ every special node gives 0, so the value is 0.
- Values can be negative when all special nodes are closer to $a$ than to $b$.
- Any maximising special node may be printed, so the second line is checked by a validator.
- The tree is processed iteratively to avoid deep recursion.

## Dry run

Edges `1-2, 1-3, 2-4, 2-5`, $a = 3$, the only special node is 2 with weight $d(3, 2) = 2$.

Subtracting the distance from node 2: node 2 gets 2, nodes 1, 4, 5 get 1, node 3 gets 0.

Output `1 2 0 1 1` and the witness `2` for every node.
