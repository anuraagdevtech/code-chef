---
topic: Dynamic Programming
subtopic: Kadane extremes on prefixes and suffixes, joined at every split point
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The two ranges are disjoint with the first entirely to the left of the second, so some boundary separates them. For a fixed boundary the difference is largest when one side takes its maximum subarray sum and the other its minimum subarray sum.

Kadane's recurrence gives the best (and worst) non-empty subarray ending at each position; a running maximum/minimum of those gives the extremes over each prefix. The same scan from the right gives the extremes over each suffix. For every boundary evaluate both pairings, max-left minus min-right and max-right minus min-left, and keep the largest absolute value.

## Edge cases

- Both ranges must be non-empty, so the Kadane variants never return an empty sum.
- All-negative or all-positive arrays still work because both a maximum and a minimum are tracked.
- Sums reach about $10^{9} \cdot N$, far beyond 32 bits.
- $N = 2$: the only choice is the two single elements.

## Dry run

`D = [1, 2, 3, 4, 5]`. The prefix minimum subarray sums are all 1 (the single element 1) and the suffix maximum sums are 14, 12, 9, 5 for suffixes starting at positions 2 to 5.

At the boundary after position 1: $|1 - 14| = 13$. Later boundaries give at most $|1 - 12| = 11$.

Answer 13.
