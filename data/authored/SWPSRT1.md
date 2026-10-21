---
topic: Sorting
subtopic: Selection sort meets the swap budget exactly
time: $O(n^2)$
space: $O(n)$
---
The budget is $n-1$ arbitrary swaps, and **selection sort** fits it precisely.

For each position $i$ from $0$ upward, find the minimum of the unsorted suffix and swap it into place. That is at most one swap per position, and the final position needs none — so at most $n-1$ swaps, matching the limit exactly.

The reason selection sort is the right tool rather than, say, bubble sort is that the swaps are **unrestricted**: any two indices may be exchanged. Bubble sort only swaps neighbours and can need $\binom{n}{2}$ of them, blowing the budget. Selection sort exploits the freedom to move an element directly to its destination.

A swap is skipped when the minimum is already in place, so the reported count can be fewer than $n-1$ — the problem asks only that it not exceed the budget, not that it be minimal.

With $n \leq 500$ the $O(n^2)$ scan is trivially fast, and the statement explicitly permits it.

The output format is the count $m$ followed by $m$ lines of index pairs, applied in order. For the sample $[3,2,1]$ this gives a single swap of positions $0$ and $2$, matching the published answer — though **any valid sequence is accepted**, so this is judged by a checker that replays the swaps and confirms the result is sorted and within budget.

Duplicate values need no special handling: selection sort places equal elements in some order, and the problem asks only for non-decreasing output, not stability.
