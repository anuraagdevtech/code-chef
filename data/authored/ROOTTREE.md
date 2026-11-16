---
topic: Graphs
subtopic: Count excess incoming edges in a directed tree
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A rooted outward tree has one vertex of indegree zero and indegree one everywhere else. If the current tree has $s$ zero-indegree vertices, its total excess indegree is $s-1$, because it has $N-1$ edges.

At least $s-1$ edges must be replaced to supply incoming edges to all but one source. This is attainable by removing excess incoming edges, leaving outward-rooted components, then connecting those components into one outward tree. Hence the answer is the number of sources minus one.

## Edge cases

- The root may be any vertex.
- Edges may be reattached, rather than only reversed.
- A single vertex already forms a rooted tree.

## Dry run

For edges `1->2` and `3->2`, sources are 1 and 3, so one replacement suffices. The chain `1->2->3` has one source and needs zero.
