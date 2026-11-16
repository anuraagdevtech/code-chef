---
topic: Strings
subtopic: Circular gaps between ones - at most one may be too long
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Place the string on a circle. Between consecutive ones there are gaps of zeros, and with $m \ge 2$ ones there are $m$ such circular gaps, including the one that wraps from the last `1` to the first.

A rotation chooses where the circle is cut. The gap that contains the cut becomes the leading and trailing zeros of the linear string and is no longer "between two adjacent ones", while every other gap stays as it is. So a valid rotation exists exactly when at most one circular gap is longer than $C$: cut inside that one, or anywhere if there is none.

With fewer than two ones there are no adjacent ones at all and the answer is YES.

## Edge cases

- No `1` or a single `1`: YES.
- With exactly two ones there are two gaps, and the answer is NO only if both exceed $C$.
- The wrap-around gap is $N + \text{first} - \text{last} - 1$.
- $C = 0$ demands that all ones be contiguous on the circle.

## Dry run

`N = 6, C = 1, S = 101001`. Ones at indices 0, 2, 5.

Gaps: between 0 and 2 one zero; between 2 and 5 two zeros; wrapping from 5 to 0 none. Only one gap exceeds $C = 1$, so cut there: the rotation `110100` works. YES.

For `0101` with $C = 0$ both gaps have one zero, two gaps exceed the limit: NO.
