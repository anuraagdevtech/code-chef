---
topic: Disjoint Set Union
subtopic: Fast-road connected components
time: $O((N+M+Q)\alpha(N))$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Union the endpoints of every fast road. Connectivity through a chain of fast roads is transitive, so two delivery locations belong together exactly when their DSU representatives agree. Path compression and union by size make all operations nearly constant time.

## Edge cases

- Locations are zero-based.
- Self-loops and repeated roads do not change components.
- The affirmative output is `YO`, not `YES`.

## Dry run

Edges `0-1` and `1-2` put locations 0, 1, and 2 together. Queries `0 2`, `0 3`, and `2 1` return `YO`, `NO`, `YO`.
