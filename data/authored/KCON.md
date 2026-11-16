---
topic: Dynamic Programming
subtopic: Kadane over two copies plus profitable middle copies
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A subarray either lies inside one copy or crosses a copy boundary. Kadane over two copies covers every possible start and end fragment. If the total sum of one copy is positive, all $K-2$ middle copies improve a crossing subarray; otherwise including additional full copies cannot help.

For $K=1$, run Kadane once. For $K\ge2$, run it over two copies and add $\max(0,(K-2)\sum A)$. Initialise from an actual element because the subarray must be nonempty.

## Edge cases

- All-negative arrays return their largest element, never zero.
- $K=1$ cannot use a cross-boundary subarray.
- A zero total needs no extra middle-copy contribution.

## Dry run

For `[1,2]`, `K=3`, Kadane over two copies gives 6, and one positive middle copy contributes 3, giving 9. For `[1,-2,1]`, two copies give 2 and total zero adds nothing.
