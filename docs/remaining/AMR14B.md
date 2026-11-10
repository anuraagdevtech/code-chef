# Road Decoration (AMR14B)

[Problem statement](https://www.codechef.com/problems/AMR14B) · [Python solution](../../solutions/AMR14B.py)

## Approach

Dijkstra computes shortest root distances and, among shortest-path parents, the cheapest possible final edge for each vertex. Positive weights ensure these edges form a shortest-path tree. Compare their total with a Kruskal MST cost; equality means the two objectives can share a tree.

## Complexity

- Time: O(M log M+N log N).
- Space: O(N+M).
