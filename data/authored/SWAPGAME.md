---
topic: Basic Math
subtopic: A potential function makes the score independent of the moves
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Define the potential $\Phi = \sum_i i \cdot A_i$. Swapping $A_i$ and $A_{i+1}$ changes it by

$$\bigl(i A_{i+1} + (i+1) A_i\bigr) - \bigl(i A_i + (i+1) A_{i+1}\bigr) = A_i - A_{i+1},$$

which is exactly the number of points the move earns. So the total score of any sequence of moves equals $\Phi(\text{final}) - \Phi(\text{initial})$, no matter which moves are made or in what order.

The final array must be $B$, and it is guaranteed to be reachable, so every valid sequence scores

$$\sum_i i \cdot (B_i - A_i),$$

and that is both the maximum and the only possible value.

## Edge cases

- $A = B$: the answer is 0, even though detours are possible - they earn nothing in total.
- The answer can be negative.
- Whether indices start at 0 or 1 does not matter, because both arrays have the same sum.
- Values up to $10^5$ and $N$ up to $5 \cdot 10^5$ give totals beyond 32 bits.

## Dry run

`A = [3, 2, 1]`, `B = [1, 2, 3]`.

With 0-based weights: $0 \cdot (1 - 3) + 1 \cdot (2 - 2) + 2 \cdot (3 - 1) = 4$.

Check with actual moves: swap (3, 2) for 1 point, (3, 1) for 2 points, (2, 1) for 1 point - 4 points and the array is `1 2 3`.
