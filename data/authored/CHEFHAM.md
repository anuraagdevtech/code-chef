---
topic: Constructive
subtopic: Rotate sorted values by the maximum frequency
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Group equal values by sorting their original indices. Let $f$ be the maximum frequency. Rotate the sorted sequence by $f$ positions and assign the rotated values back to the original indices.

An equal-value block has length at most $f$. If $f\le N/2$, shifting by $f$ separates every block from itself. If $f>N/2$, at least $2f-N$ positions must match by pigeonhole; the rotation attains exactly this lower bound. Thus the construction maximises Hamming distance, including the small cases where full derangement is impossible.

## Edge cases

- A single element necessarily has distance zero.
- For `[1,2,1]`, at most two positions differ.
- Print the actual distance and preserve the input multiset.

## Dry run

For `[1,2,1]`, sorted indices carry values `[1,1,2]`. Rotate by two to get `[2,1,1]`; restoring indices yields `[2,1,1]`, differing at exactly two positions.
