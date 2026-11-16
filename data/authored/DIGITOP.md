---
topic: Strings
subtopic: Length invariance and global digit deficits
time: $O(\sum |A_i|+\sum |B_i|)$ per test case
space: $O(N)$ for the input arrays
complexity_note: Auxiliary space excludes the buffered input and output.
---
Both operations preserve the length of every array entry. If any corresponding lengths differ, conversion is impossible.

Otherwise all digit positions can be permuted for free: swaps between different entries are allowed, and a third position in another nonempty entry lets us simulate a swap within an entry. There are at least two entries. Count all digits globally. Every missing target digit requires one paid replacement, and replacing surplus digits supplies all deficits. The minimum cost is the sum of positive target-minus-source frequency differences.

## Edge cases

- Equal total lengths do not replace the per-entry length check.
- Leading zeros are characters and must be retained.
- The guarantee $N\ge2$ is needed for free within-entry rearrangement.

## Dry run

In sample three, source digit counts lack one `8` and have one extra `2`. One replacement resolves the deficit, while free swaps arrange the digits, so budget one succeeds.
