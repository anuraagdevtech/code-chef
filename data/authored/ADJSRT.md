---
topic: Sorting
subtopic: Insertion sort performs exactly the inversions
time: $O(n + \text{inversions})$
space: $O(n)$
---
Each adjacent swap changes the relative order of exactly **one** pair, so it can remove at most one inversion. A sorted array has none, so the minimum number of adjacent swaps is exactly the **inversion count** of the input.

**Insertion sort achieves that bound.** It only ever swaps a pair that is currently out of order, so every swap removes an inversion and none is wasted. Recording the left index of each swap as it happens produces the required sequence directly.

The complexity point matters here. Insertion sort is usually quoted as $O(n^2)$, but its real cost is $O(n + \text{inversions})$ — the comparisons are proportional to the swaps plus one per element. The problem guarantees at most $10^5$ inversions, so this runs in linear-ish time despite $n$ reaching $10^5$. Bubble sort, by contrast, would scan $O(n^2)$ times regardless of how few swaps it makes, and would time out.

Recording swaps **as they happen** is what makes the output valid: the indices refer to the array state at that moment, and replaying them in order reproduces the sort.

For the sample $[3,2,1]$ the swaps are at indices $0$, then $1$, then $0$ again — three swaps, matching the inversion count of $\binom{3}{2} = 3$ and the published answer exactly.

Equal elements are never swapped, since the comparison is strict, which keeps the count minimal — swapping equal neighbours would waste a move without removing an inversion.
