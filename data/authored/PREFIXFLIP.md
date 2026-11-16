---
topic: Strings
subtopic: Sliding window over mandatory boundary flips
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a fixed window, every unequal adjacent pair inside it requires one flip ending at that boundary. A prefix flip changes no other internal boundary. In addition, its rightmost character must become one, requiring one further flip if it is zero. Thus the exact cost is the number of internal transitions plus the indicator that the last character is zero.

Slide a length-$K$ window, removing its old left boundary and adding its new right boundary. Take the smallest exact cost.

## Edge cases

- $K=1$ has no internal boundaries.
- An existing run of $K$ ones costs zero.
- A full zero window needs just one flip.

## Dry run

For `10101`, $K=3$, the three window costs are `2, 3, 2`; the minimum is `2`.
