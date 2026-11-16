---
topic: Sorting
subtopic: Smallest value window that contains an option for every index
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
After the swaps, $A_i$ is simply one of the two values $\{A_i, B_i\}$, chosen independently for every index. So the task is: choose one value per index so that the range of the chosen values is as small as possible.

A range $[lo, hi]$ is achievable exactly when every index has at least one of its two values inside it. Put all $2N$ values, tagged with their index, into one sorted list and find the shortest window (in value) that contains every index at least once - the classic two-pointer "smallest window covering all colours". Extend the right end; while all indices are covered, record the width and shrink from the left.

## Edge cases

- $A_i = B_i$ contributes the same value twice; the multiplicity counter handles it.
- $N = 1$: the answer is 0.
- The optimal minimum and maximum are always among the given values, so only windows between listed values need checking.
- Values up to $10^9$ only matter through their order and differences.

## Dry run

`A = [1, 5, 3]`, `B = [2, 3, 1]`. Sorted (value, index): `(1,1) (1,3) (2,1) (3,2) (3,3) (5,2)`.

The right end first covers all three indices at `(3,2)`: window from `(1,1)`, width 2. Shrinking: drop `(1,1)` (index 1 still present via `(2,1)`), width $3 - 1 = 2$; drop `(1,3)` - index 3 is lost, stop. Extending to `(3,3)` covers again with left end `(2,1)`: width 1.

Answer 1 (choose 2, 3, 3).
