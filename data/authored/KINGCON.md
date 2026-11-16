---
topic: Graphs
subtopic: Iterative low-link articulation-point search
time: $O(N+M)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A city needs a shield exactly when removing it disconnects the remaining graph: it is an articulation point. Use DFS discovery times and low-link values. A non-root vertex $u$ is an articulation point when some DFS child $v$ cannot reach a proper ancestor of $u$, meaning $low[v]\ge tin[u]$. A DFS root is an articulation point exactly when it has more than one DFS child.

Maintain the next adjacency position in each explicit DFS stack frame, propagating low-link values when frames finish. Count marked vertices and multiply by the shield price.

## Edge cases

- Vertices are zero-based.
- Treat DFS roots separately from other vertices.
- Mark a city once even if several child subtrees separate.
- A two-vertex graph has no articulation point.

## Dry run

The sample tree has internal vertices 1, 2, and 4 whose removal separates other cities. Three shields at cost five each give 15.
