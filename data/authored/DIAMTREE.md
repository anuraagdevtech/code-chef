---
topic: Graphs
subtopic: Two breadth-first searches find a tree diameter
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
In a tree, a vertex farthest from any chosen start is an endpoint of some diameter. BFS once from vertex 1 to locate such an endpoint, then BFS from it. The largest distance in the second search is the diameter.

Store distances rather than recurse, so a chain of $10^5$ vertices does not overflow Python's call stack.

## Edge cases

- A one-vertex tree has diameter zero.
- Count edges, not vertices on the path.
- Multiple farthest endpoints are interchangeable.

## Dry run

The first sample has path `4-2-1-3-6`, containing four edges. Two BFS traversals return diameter four.
