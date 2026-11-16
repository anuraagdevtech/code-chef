---
topic: Dynamic Programming
subtopic: Process oriented edges in batches of equal differences
time: $O(N+M\log M)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Orient every edge from smaller value to larger value and discard equal-valued edges. Its weight is the positive difference. Process these edges by increasing weight, with $dp[v]$ storing the best path length ending at $v$ using processed weights.

For edges of weight $d$, propose `dp[u]+1` at each destination, but apply none of those proposals until the whole equal-weight batch has been read. This prevents consecutive differences from being equal. Every valid path is built from its last edge, so these transitions find the longest path.

## Edge cases

- A path length counts vertices; isolated vertices have length one.
- Equal differences must be processed together.
- Self-loops and edges joining equal values cannot extend a path.
- Parallel edges do not change the recurrence.

## Dry run

In sample two, edge `1->2` has difference one and sets the path length at 2 to two. Edge `2->5` has difference three and extends it to three vertices.
