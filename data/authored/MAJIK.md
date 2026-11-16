---
topic: Greedy
subtopic: Keep the two extremes and absorb the largest absolute values into them
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Each operation removes two elements and inserts one combination of them, so $P + Q$ operations can fold at most $P + Q$ other elements into the two elements that will end up as the maximum and the minimum.

Folding an element $x$ into an extreme can widen the gap by exactly $|x|$ and never by more: with the addition, a positive $x$ is added to the maximum and a negative $x$ to the minimum; with the other operation the roles are mirrored. So whichever kind of operation is still available, any leftover element can be used, and its contribution is its absolute value.

Start from the gap between the original maximum and minimum - those two are the best bases - and add the $P + Q$ largest absolute values among the remaining $N - 2$ elements.

## Edge cases

- $P = Q = 0$: the answer is simply max minus min.
- $N = 1$: there is nothing to combine and the answer is 0.
- At most $N - 2$ elements can be absorbed, so a surplus of operations is harmless.
- The gap can reach about $N \cdot 10^9$.

## Dry run

`A = [8, -1, -4, 2, 6, -3]`, `P = 1, Q = 2`.

Sorted: `-4 -3 -1 2 6 8`. Base gap $8 - (-4) = 12$. Absolute values of the middle elements, largest first: `6 3 2 1`; three operations take $6 + 3 + 2 = 11$.

Answer $12 + 11 = 23$.
