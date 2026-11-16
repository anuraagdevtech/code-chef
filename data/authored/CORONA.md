---
topic: Graphs
subtopic: Multi-source Dijkstra seeded with hospital prices
time: $O((N+M)\log N)$ per test case
space: $O(N+M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Imagine a new source connected to each hospital by an edge equal to that hospital's test price. A shortest route from this source to any city pays exactly one hospital price plus the road distance from it.

There is no need to materialise the new vertex: initialise every hospital's distance to its price and put all hospitals in the heap. Run Dijkstra on the bidirectional roads. Hospital cities can improve through a cheaper hospital elsewhere.

## Edge cases

- A hospital city need not use its own hospital.
- Prices and road distances can produce totals beyond 32 bits.
- Discard stale heap entries after shorter routes are found.

## Dry run

In sample two, city 2 can use city 1 at cost `5+1=6`, improving on its own price 10. City 3 then uses the same hospital for `6+9=15`.
