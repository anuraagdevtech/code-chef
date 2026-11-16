---
topic: Bit Manipulation
subtopic: Memoised search over bitmasks with maximal windows and dominance pruning
time: $O(2^N \cdot N^2)$ in the worst case; pruning keeps the visited states far below that for $N \le 30$
space: $O(2^N)$ worst case for the memo
complexity_note: Auxiliary space excludes the buffered input and output.
---
Only one thing matters about an element: whether it already equals the maximum. Encode the array as a bitmask of those positions. An operation on $[l, r]$ turns the whole window into the maximum exactly when the median of the window is the maximum, i.e. when at least half of its entries are ones; any other operation cannot create a new maximum and is useless.

Search with memoisation on the mask:

- full mask: 0 operations;
- at least half of all positions set: 1 operation on the whole array;
- otherwise try windows. For a fixed left end only the farthest right end with a non-negative balance (ones minus zeros) is worth trying, since a larger filled window is never worse. Among the resulting masks, skip any that is a subset of another already kept one.

The answer for a state is one plus the best successor; a successor that finishes in one more operation cannot be beaten, so the loop stops at 2.

## Edge cases

- If every element is already the maximum the answer is 0.
- The median index is $\lfloor n/2 \rfloor + 1$, so a window with exactly half ones already works - the balance test is `>= 0`.
- A window that does not change the mask is not a move.
- The memo is per test case because the meaning of a mask depends on $N$.

## Dry run

`A = [1, 2, 3]`: mask `001` (only the last position). One of three is less than half, so one operation is not enough.

From left end 2 the window `[2, 3]` has balance 0, giving mask `011`. Now two of three positions are set, which is at least half: one more operation on the whole array finishes.

Answer 2. For `[2, 1, 1, 2]` the mask `1001` already has half of the positions, so the answer is 1.
