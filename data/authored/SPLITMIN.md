---
topic: Sorting
subtopic: The larger maximum is at least the largest of the pair minima; pair it with its nearest lower value
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $L = \max_i \min(A_i, B_i)$. Whatever is chosen, the pair attaining $L$ contributes a value of at least $L$, so the larger of the two pile maxima is at least $L$.

Conversely, take any value $X \ge L$ from some pair and any value $Y \le X$ from a *different* pair. They can be made the two maxima: put $Y$ alone in one pile, and put $X$ together with the smaller element of every other pair - each at most $L \le X$ - in the other. The difference is $X - Y$.

So the answer is the minimum of $X - Y$ over values $X \ge L$ and $Y \le X$ belonging to different pairs. Sort all $2N$ values tagged with their pair index; for each $X \ge L$ the best partner is the closest earlier value in sorted order with a different tag, and since a pair has only two values at most one earlier entry is skipped.

## Edge cases

- Both piles must be non-empty, which the construction guarantees ($Y$ is alone in its pile).
- The two maxima may be equal, giving 0.
- $X$ and $Y$ must come from different pairs - both elements of one pair cannot be chosen.
- With $N = 2$ the answer is simply the best of the four cross differences.

## Dry run

Pairs `(1, 9)` and `(4, 6)`: $L = \max(1, 4) = 4$.

Sorted values with owners: `1(a) 4(b) 6(b) 9(a)`.

- $X = 4$: previous value of another pair is 1, difference 3.
- $X = 6$: skip 4 (same pair), take 1, difference 5.
- $X = 9$: previous is 6 from the other pair, difference 3.

Answer 3.
