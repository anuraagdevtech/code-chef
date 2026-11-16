---
topic: Graphs
subtopic: Lazy multi-source BFS driven by a time-ordered heap
time: $O((N + M) \log N + Q)$
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Freezing spreads one edge per unit of time from every frozen node, so this is a multi-source BFS in which new sources appear over time and the clock only advances on type-2 queries.

Keep a clock `now` and a min-heap of (freeze time, node) for nodes whose neighbours have not been processed yet. A type-1 query freezes the node immediately and pushes it with the current time. A type-2 query advances the clock by $t$ and then pops every event whose time is strictly less than the new `now`: such a node has had at least one full unit of time to spread, so each unfrozen neighbour is frozen and pushed with time + 1. A type-3 query just reads the flag.

Every node is pushed once and every edge is scanned at most twice, regardless of how large the time jumps are.

## Edge cases

- Time jumps can be $10^9$; the loop is bounded by the graph, not by $t$.
- Freezing an already frozen node does nothing.
- An event with time equal to `now` has not spread yet and stays in the heap.
- Whether a node is frozen never needs its exact freeze time - marking it early while processing in time order is safe because the pending event keeps the correct time.

## Dry run

Sample graph with edges `1-2, 2-3, 4-1, 5-4, 6-1, 6-5`.

- `1 1`: node 1 frozen at time 0. `3 1` answers YES.
- `1 5`: node 5 frozen at time 0.
- `2 1`: the clock becomes 1. Events (0, 1) and (0, 5) are popped: nodes 2, 4, 6 freeze with time 1. Those events are not earlier than 1, so they wait.
- `3 4`: YES. `3 3`: NO - node 3 would freeze at time 2.
