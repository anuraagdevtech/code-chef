# Kingdom Unity (KINGCON)

[Problem statement](https://www.codechef.com/problems/KINGCON) · [Python solution](../../solutions/KINGCON.py)

## Approach

Exactly the articulation points require shields. An iterative low-link DFS marks nonroot vertices separating a child subtree and roots with multiple DFS children. Multiply their count by the shield price.

## Complexity

- Time: O(N+M).
- Space: O(N+M).
