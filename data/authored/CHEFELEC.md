---
topic: Greedy
subtopic: Remove the largest gap between consecutive powered villages
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Connecting every consecutive village costs $x_{N-1}-x_0$. Before the first powered village and after the last, every gap is necessary. Between two consecutive powered villages, all interior villages can be supplied from either end. Exactly one gap may be omitted, and omitting the largest gap saves the most wire.

Scan adjacent gaps, tracking their maximum since the previous powered village. On reaching another powered village, subtract that maximum from the total.

## Edge cases

- At least one powered village is guaranteed.
- With only one source, no gap can be removed.
- Adjacent powered villages need no wire between them.

## Dry run

For positions `[1,5,6]` and status `100`, every gap is needed, so the cost is `6-1=5`.
