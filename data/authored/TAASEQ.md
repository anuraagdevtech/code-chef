---
topic: Arrays
subtopic: A constant number of removal candidates, each verified in linear time
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Either one of the first two elements is removed, or both stay and their difference $d$ is the common difference of the result. In the latter case scan for the first adjacent pair whose difference is not $d$: the removed element has to be one of those two, since otherwise that defect would survive. If no defect exists the array is already an arithmetic progression and only an end element can be removed.

That leaves at most five candidate positions - indices 0, 1, $N-1$ and the two around the first defect. For each, build the array without it and check directly that it is an arithmetic progression. Print the smallest value among the valid removals, or -1.

## Edge cases

- Arrays of length at most 2 after removal are always arithmetic progressions.
- When several removals work the smallest removed value is required, not the first position.
- An array that is already a progression loses its first or last element - whichever is smaller.
- A constant array allows any removal; the candidates still contain its minimum.

## Dry run

`A = [2, 4, 6, 7, 8, 10]`. The first difference is 2 and the first pair that breaks it is (6, 7), so the candidates are indices 0, 1, 5, 2 and 3.

Removing index 3 (the 7) leaves `2 4 6 8 10`, a progression. Removing any other candidate leaves the pair 6, 7, 8 with difference 1 next to a difference of 2.

Answer 7.
