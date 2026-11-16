---
topic: Graphs
subtopic: Dijkstra with counts of equal shortest routes
time: $O((N+M)\log N)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Maintain shortest distance and number of shortest paths for each vertex. A strictly shorter relaxation replaces both the distance and the count with the predecessor's count. An equal-distance relaxation adds the predecessor's count.

All road lengths are positive, so every predecessor of a shortest path is settled before its destination. This guarantees the count is complete when that destination is processed. Counts are exact integers; the problem requests no modulus.

## Edge cases

- Multiple equal-length routes must all count.
- A direct edge may tie a multi-edge route.
- Do not add counts for stale heap entries.

## Dry run

In sample two, direct path `1-3` and path `1-2-3` both have length nine. The equal-distance relaxation adds their counts, returning two.
