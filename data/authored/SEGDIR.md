---
topic: Graphs
subtopic: Two-colour equal-speed interval overlaps by maximum depth
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
At the enormous target time, different speed magnitudes are separated regardless of their assigned signs. Only intervals with equal speeds and equal directions can still overlap. Therefore each speed group must be divided into two classes of pairwise disjoint closed intervals.

For intervals, two such classes exist exactly when no point belongs to three intervals. Sort each speed group by left endpoint and maintain a min-heap of active right endpoints. Remove endpoints strictly less than the next left endpoint, since touching is forbidden. If two intervals remain active before inserting another, three overlap and assignment is impossible.

## Edge cases

- Touching endpoints count as an overlap.
- Different speeds impose no final-time constraint.
- More than two intervals may share a speed if their overlaps form only depth two.

## Dry run

The second sample has four identical intervals of the same speed. Three already overlap at every point, so two directions cannot separate them and the answer is `NO`.
