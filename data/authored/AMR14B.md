---
topic: Graphs
subtopic: Compare the cheapest shortest-path tree with an MST
time: $O(M\log N)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
With positive edge lengths, a tree minimises the sum of distances from root zero exactly when every root-to-vertex path is a shortest path in the original graph. For each non-root vertex, choose the cheapest possible last edge among all its shortest paths. Distances strictly increase along such edges, so these independent choices form a tree and minimise total edge weight among shortest-path trees.

Run Dijkstra, breaking equal-distance relaxations by the smaller last-edge weight. Separately compute an MST using Prim's algorithm. A common optimal tree exists exactly when the sum of chosen shortest-path-tree edges equals the MST weight. Reject disconnected graphs.

## Edge cases

- Vertices are zero-based.
- Equal shortest distances may have different last-edge costs.
- Disconnected graphs return `NO`.
- Positive weights ensure parent choices cannot create a cycle.

## Dry run

For edges `0-1:1,0-2:2,1-2:2`, cheapest shortest-path edges cost `1+2=3`, matching the MST. Both objectives can use the same tree, so the answer is `YES`.
