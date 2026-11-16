---
topic: Prefix Sums
subtopic: Circular sliding window grouped by starting offset
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The states are $o_1$ consecutive blocks of $o_2$ districts on a circle, so a partition is completely determined by where the first block starts, and only the start modulo $o_2$ matters - there are just $o_2$ different partitions.

Slide a window of width $o_2$ around the circle (append the first $o_2$ values to unroll it) and record for each start whether the window holds more ones than zeros. A window starting at $i$ belongs to the partition with offset $i \bmod o_2$, so add its result to that offset's counter. The president can be a One exactly when some offset collects more than $o_1 / 2$ One-governors.

## Edge cases

- $o_2 = 1$: every district is its own state and there is only one partition.
- $o_1 = 1$: one state containing everything; the offset does not matter.
- Both numbers are odd, so neither vote can be tied.
- Windows that wrap past district $N$ are valid states and are covered by the unrolled array.

## Dry run

`o1 = 3, o2 = 3`, districts `0 0 1 1 0 1 1 0 0`.

Window sums by start: `1 2 2 2 2 2 1 0 0`; a window is won with at least 2 ones, so wins by start are `0 1 1 1 1 1 0 0 0`.

Offset 0 collects starts 0, 3, 6: 1 win. Offset 1 collects starts 1, 4, 7: 2 wins. Offset 2 collects starts 2, 5, 8: 2 wins. Two governors out of three is a majority, so the answer is 1.
