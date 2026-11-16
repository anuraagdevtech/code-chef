---
topic: Greedy
subtopic: Sort zero blocks downwards and one blocks upwards
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A zero block contributes its size times the total length of all later one blocks. Those suffix totals decrease from left to right, so larger zero blocks belong earlier. Equivalently, a one block contributes its size times all preceding zeros; those prefix totals increase, so larger one blocks belong later.

Sorting zero blocks descending and one blocks ascending satisfies both exchange arguments simultaneously. Interleave them, then accumulate the score with a running zero count.

## Edge cases

- Swaps are allowed only within the same parity of block indices.
- A final zero block contributes no pairs.
- Print both the optimal compression array and the count.

## Dry run

For `[2,3,4,3]`, sort zero blocks to `[4,2]`. Interleaving gives `[4,3,2,3]`; its score is `4*3+6*3=30`.
