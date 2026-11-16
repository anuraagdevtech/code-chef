---
topic: Dynamic Programming
subtopic: Interval-minimum sweep and pruned removal knapsack
time: $O((N+M)\log M+N\log K+KB)$ per test case with $B\le\min(N,\sum_{c=1}^{200}\lfloor K/c\rfloor)$
space: $O(N+M+K+B)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Removing a nonnegative-rated dish cannot help. For each negative dish, find the cheapest judge covering its index: sort interval starts and maintain a heap ordered by removal price, lazily discarding intervals whose right endpoint has passed.

A removable negative dish becomes a 0-1 item with cost equal to that cheapest price and gain equal to the negated rating. For any cost $c$, at most $K//c$ such dishes can be removed. Keep only that many largest gains with a min-heap; every discarded gain is dominated by enough equally priced better dishes. Run ordinary descending-capacity knapsack over the retained items and add its best gain to the original total rating.

## Edge cases

- An uncovered negative dish cannot be removed.
- Never pay to remove a positive or zero rating.
- Overlapping judges use their minimum price.
- Equal-cost pruning preserves the optimum.

## Dry run

The sample begins with total zero. Budget ten can remove the dish rated minus five for ten rupees, giving final rating five; the minus-ten dish costs fifteen and is unaffordable.
