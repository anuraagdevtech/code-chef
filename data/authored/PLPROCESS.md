---
topic: Prefix Sums
subtopic: Minimising the heavier side of a split
time: $O(N)$ per test case
space: $O(1)$
---
The split point is the only decision: the first processor takes a prefix, the second takes the rest. Both run **simultaneously**, so the finishing time is the larger of the two workloads, not their sum:

$$\min_{0 \leq c \leq N} \max\bigl(\text{prefix}(c),\ \text{total} - \text{prefix}(c)\bigr)$$

Computing the total once, then sweeping $c$ from $0$ to $N$ with a running prefix sum, evaluates every split in $O(N)$ with no stored array.

Taking the **maximum** rather than the sum is the crux. Sample case 1, $[4,2,3]$, totals $9$ but finishes in $5$ — one processor runs $4$ while the other runs $2+3 = 5$, and they overlap.

The split must be a **contiguous prefix**, which is what keeps this simple. Were any subset allowed, this would be the partition problem and NP-hard; the prefix restriction reduces it to a linear scan.

Note the two extreme splits are legal — all tasks to one processor — so $c = 0$ and $c = N$ must both be considered. Sample case 3, a single task, relies on that: whichever processor takes it, the answer is $5$.

Sample case 2 splits six unit tasks evenly into $3$ and $3$. The best split is not always perfectly even, though: with $[4,2,3]$ the halves are $4$ and $5$, since the boundary can only fall between tasks.

Values reach $10^5$ with $N$ up to $10^5$, so totals reach $10^{10}$ — beyond 32 bits, though Python is unaffected.
