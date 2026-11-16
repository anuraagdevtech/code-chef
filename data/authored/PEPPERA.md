---
topic: Dynamic Programming
subtopic: Partition row imbalances and reconstruct the reversals
time: $O(N^2+ND/w)$ word operations per test case for $D\le N^2/2$ total absolute imbalance
space: $O(N^2+ND/w)$ machine words and stored row characters
complexity_note: Auxiliary space excludes the buffered input and output.
---
A row contributes the difference between its left-half and right-half pepperoni counts. Reversing it negates that contribution. Let $d_i$ be the absolute difference for each row. The problem is to choose signs minimising $|\sum \pm d_i|$, equivalent to subset sum as close as possible to half of $D=\sum d_i$.

Use a bitset to find reachable sums at most $D//2$. Retain the reachable bitset after each row. Reconstruct a maximum reachable sum backwards: skip a row when the previous bitset already reaches the current target, otherwise select it and reduce the target by its imbalance. Give those selected rows negative signs. Orient every row to realise its desired sign, preserving the row itself or reversing it.

## Edge cases

- Rows with equal half counts need no change.
- Reverse whole rows only; do not exchange characters arbitrarily.
- If exact balance is impossible, the nearest reachable half is optimal.

## Dry run

For two rows `01`, each absolute imbalance is one. Select one row for the negative contribution and orient the other positively, yielding `10` and `01` with zero total difference.
