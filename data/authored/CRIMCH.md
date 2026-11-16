---
topic: Graphs
subtopic: Bipartite colouring of every connected component
time: $O(N+M)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Create an undirected edge for every pair that cannot be teammates. The requested team assignment is exactly a two-colouring in which every edge has differently coloured endpoints.

BFS or iterative DFS each unvisited component, assigning opposite colours across edges. If an edge joins equal colours, an odd cycle makes the assignment impossible. Otherwise the two colour classes are valid teams.

## Edge cases

- Disconnected components all require checking.
- Isolated vertices can be assigned either colour.
- A triangle is impossible even when other components are bipartite.

## Dry run

The first sample is a triangle, forcing an equal-colour edge and `NO`. The second sample contains two independent edges, which can both be coloured, giving `YES`.
