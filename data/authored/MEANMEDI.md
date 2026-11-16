---
topic: Dynamic Programming
subtopic: Fixed median with cardinality-indexed subset-sum bitsets on both sides
time: $O(N \cdot K \cdot S / w + N \cdot S)$ per test case, $S$ the largest reachable sum
space: $O(N \cdot S / w)$ machine words
complexity_note: Auxiliary space excludes the buffered input and output.
---
Sort the numbers and fix which position $i$ supplies the median. With $K$ chosen numbers the median is the $\lfloor (K+1)/2 \rfloor$-th smallest, so exactly $\lfloor (K-1)/2 \rfloor$ chosen numbers come from before $i$ and $\lfloor K/2 \rfloor$ from after it.

$|\text{mean} - \text{median}| = |\text{sum} - K \cdot a_i| / K$, so we want the left sum plus the right sum to be as close as possible to $(K-1) \cdot a_i$. A knapsack indexed by how many numbers are taken, stored as big-integer bitsets, gives for every prefix the set of sums reachable with exactly the left count, and symmetrically for every suffix.

For each median position, walk over the set bits of the left bitset; for a left sum $s$ the best partner is the reachable right sum nearest to $(K-1) a_i - s$, found with two bit tricks: the highest set bit at or below the target and the lowest set bit at or above it. Stop early once a difference of zero is found, and print the best difference divided by $K$ with three decimals.

## Edge cases

- $K = 1$: both counts are zero, the mean equals the median and the answer is `0.000`.
- Even $K$ uses the lower middle element, so the two sides have different sizes.
- Equal values are harmless: sorting places them consistently and any of them may act as the median.
- The target for the right sum can be negative when the left sum already overshoots; then the smallest right sum is the best partner.

## Dry run

`N = 3, K = 3`, values `[1, 2, 4]`. One number is needed on each side, so only the middle position can be the median: $a_i = 2$, target $(K-1) \cdot 2 = 4$.

Left sums `{1}`, right sums `{4}`. For $s = 1$ the wanted right sum is 3; the nearest reachable one is 4, distance 1.

Answer $1/3$, printed as `0.333`.
