# Find Tree Diameter (DIAMTREE)

[Problem statement](https://www.codechef.com/problems/DIAMTREE) · [Python solution](../../solutions/DIAMTREE.py)

## Approach

Traverse from an arbitrary vertex to a farthest endpoint, then traverse again from that endpoint. The greatest second distance is the tree diameter. Both traversals are iterative.

## Complexity

- Time: O(N).
- Space: O(N).
