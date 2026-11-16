---
topic: Graphs
subtopic: 0-1 BFS on original and reversed edge choices
time: $O(N+M)$ overall
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Keep each original directed edge with traversal cost zero and add its reverse with cost one. A path's total cost is precisely the number of edge reversals it requires. Therefore the requested answer is the shortest path from 1 to $N$ in this 0-1 weighted graph.

Use a deque: a zero-cost improvement goes to the front, and a one-cost improvement goes to the back. Skip stale distance entries. If the destination stays unreachable, output minus one.

## Edge cases

- Original and reverse edges may both exist.
- Self-loops never help lower a shortest path.
- If source equals destination, zero reversals suffice.
- Reversals cannot connect separate undirected components.

## Dry run

The sample path `1-2-3-4-7` uses reverse directions for edges `3->2` and `7->4`, giving cost two.
