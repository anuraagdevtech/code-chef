---
topic: Graphs
subtopic: Try the two starting vertices and follow unique letter transitions
time: $O(|S|)$ per test case
space: $O(|S|)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Vertices zero through four form the outer five-cycle; vertices five through nine form the inner star, and each outer vertex connects to its corresponding inner vertex. Both vertices with index congruent to $c$ modulo five carry letter $c$.

Each vertex has at most one neighbour with any requested letter. Hence the entire walk is forced once its starting vertex is fixed. Try the smaller starting vertex first; if its forced walk succeeds it is lexicographically smallest. Otherwise try the other start, and output minus one only if both fail.

## Edge cases

- A one-letter string uses the smaller corresponding vertex.
- Repeated letters require crossing the spoke.
- A locally possible start may fail later, requiring the second start.

## Dry run

For `AAB`, starting at 0 forces `0->5`, but vertex 5 has no `B` neighbour. Starting at 5 forces `5->0->1`, so the least valid walk is `501`.
