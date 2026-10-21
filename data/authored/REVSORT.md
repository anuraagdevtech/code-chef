---
topic: Arrays
subtopic: Constraining which inversions may be undone
time: $O(N)$ per test case
space: $O(N)$
---
Reversing a subarray of length $2$ is just swapping an adjacent pair, so the pair $(x, y)$ can be swapped only when $x + y \leq X$. That single observation drives everything.

**Necessity.** If two elements $x$ and $y$ satisfy $x + y > X$, they can never cross each other — not directly, and not by any sequence of moves, since any reversal that reorders them relative to one another would have to contain both and therefore have sum exceeding $X$. So every pair that is **out of order** in the input must be cheap enough to swap:

$$\text{for all } i < j \text{ with } A_i > A_j: \quad A_i + A_j \leq X$$

**Sufficiency.** If that holds, bubble sort works: it only ever swaps adjacent pairs that are currently inverted, and any pair inverted now was inverted in the original array, so its sum is within budget.

Checking all pairs is $O(N^2)$, but only the **worst** inversion matters. Sweeping left to right with a running prefix maximum, each position $j$ contributes the candidate $\max(A_1 \ldots A_{j-1}) + A_j$ whenever that maximum exceeds $A_j$. The answer is `YES` exactly when the largest such candidate is at most $X$ — or when no inversion exists at all.

The already-sorted case is where this matters most. Sample case 1 is $[1,2,3,4]$ with $X = 1$: nothing can be swapped, but nothing needs to be, so `YES`. Sample case 2 is the same tiny budget with one inversion, $2$ before $1$, costing $3 > 1$ — `NO`. Sample case 3 has inversions costing at most $5$, inside the budget of $7$.

## Edge cases

- **Already sorted** (the first row): no inverted pair exists, so `worst` stays $0$ and even $X = 1$ answers `YES`.
- **One inverted pair decides it** (the second row, where the pair $(2, 1)$ sums to $3 > X = 1$): `NO`.
- **Equal values are not inversions.** The third row holds $3, 3, 3$ and $2, 2$; the strict `>` skips them, whereas `>=` would charge $6$ for a pair of $3$s and answer `NO`.
- **The criterion is about pairs, not about whole reversals.** The sample's own explanation for the third case reverses a three-element subarray summing to $7$, but bubble sort reduces any permutation to adjacent swaps of inverted pairs, and the costliest such pair here sums to only $5$ — so the pairwise bound is what governs, and it is both necessary and sufficient.
- **A running maximum replaces all $O(N^2)$ pairs**, because the costliest inversion ending at position $j$ pairs $A_j$ with the largest value before it.
- **$A_i, X \leq 2 \cdot 10^9$** makes a pair sum reach $4 \cdot 10^9$ — past 32-bit signed, though native in Python.

## Dry run

Third sample: $A = 3, 2, 2, 3, 3$ with $X = 7$.

| $j$ | $A_j$ | prefix max | inverted? | pair sum | worst so far |
|---:|---:|---:|:---:|---:|---:|
| 2 | 2 | 3 | yes | 5 | **5** |
| 3 | 2 | 3 | yes | 5 | 5 |
| 4 | 3 | 3 | no | — | 5 |
| 5 | 3 | 3 | no | — | 5 |

$5 \leq 7$, so `YES`.
