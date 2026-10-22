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

## Edge cases

- **Selection sort fits the budget exactly.** Each of the first $n-1$ positions is fixed with at most one swap, so the total never exceeds $n-1$ — which is precisely the allowance.
- **A position already holding its minimum is skipped**, so the count can be well below $n-1$ — the sample uses just one swap for three elements.
- **The swaps may use any two indices**, not only adjacent ones, which is what lets selection sort apply at all.
- **Minimisation is explicitly not required**, so there is no need to count inversions or find the cycle decomposition — any sequence within budget is accepted.
- **The reported pairs must be replayable in order**, which the emission order guarantees.
- **An already-sorted array yields zero swaps**, and the output is the count alone.
- **Equal elements need no swap**, since `min` picks the earliest index among ties and the guard then skips it.
- **$n \leq 500$** makes the quadratic scan trivial, and the statement explicitly permits it.

## Dry run

Sample: $A = 3, 2, 1$.

| position | smallest in the suffix | at index | swap? | array after |
|---:|---:|---:|---|---|
| 0 | 1 | 2 | yes, $(0, 2)$ | $1, 2, 3$ |
| 1 | 2 | 1 | no | $1, 2, 3$ |

One swap, so the output is `1` then `0 2`.
