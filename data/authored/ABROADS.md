---
topic: Disjoint Set Union
subtopic: Process the queries backwards - deletions become unions
time: $O((N + M + Q) \log (N + M + Q))$
space: $O(N + M + Q)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A disjoint-set union can merge but not split, so read all queries first and answer them in reverse.

Forward pass over the input: for a `P` query remember the old population before overwriting it; for a `D` query mark the road as removed. Afterwards build the DSU of the final state: the final populations and all roads that were never removed, with the total population stored at each root.

Backward pass: the state before undoing query $i$ is the state right after it, so first record the current maximum region population as the answer to query $i$, then undo it - a `D` becomes a union of the road's endpoints, a `P` restores the old population by adjusting the sum at the town's root.

The maximum is kept in a max-heap of (sum, root) with lazy deletion: every time a root's sum changes a new entry is pushed, and entries whose vertex is no longer a root or whose sum is outdated are discarded when they reach the top.

## Edge cases

- A road is removed at most once; undoing joins two components or does nothing if they are already joined.
- Population updates can lower a region's total, which is why stale heap entries must be validated.
- Answers are produced in reverse and printed in the original order.
- The query type is a letter, so the input is tokenised as bytes rather than integers.

## Dry run

Towns `1 2 3` with roads `1-2, 2-3, 3-1`; queries `P 1 3`, `D 1`, `P 2 3`, `D 2`, `P 3 10`, `D 3`.

Final state: populations `3 3 10`, no roads; maximum 10 (answer to query 6).

Undo backwards: add road `3-1` -> regions `{1,3} = 13`, `{2} = 3` (answer 13 for query 5); restore town 3 to 3 -> `{1,3} = 6` (answer 6); add road `2-3` -> one region of 9 (answer 9); restore town 2 to 2 -> 8 (answer 8); add road `1-2` -> still 8 (answer 8).

Output `8 8 9 6 13 10`.
