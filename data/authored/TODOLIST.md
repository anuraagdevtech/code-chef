---
topic: Arrays
subtopic: Counting with a predicate
time: $O(N)$ per test case
space: $O(1)$
---
Chef should keep only problems rated **strictly below** $1000$, so the number to remove is the count of ratings that are $\geq 1000$.

There is no need to sort, to build a filtered list, or to actually delete anything — the question asks only *how many*, so a single pass with a counter answers it in $O(N)$ time and $O(1)$ extra space. In Python the whole loop collapses to `sum(1 for d in ratings if d >= 1000)`, since summing a boolean generator counts the matches.

The trap is the direction of the comparison. "Keep ratings strictly less than $1000$" means remove $\geq 1000$, so $1000$ itself is **removed**. Sample case 2 isolates this: of $999, 1000, 1001, 1002$ only the $999$ survives, giving an answer of $3$. Case 4 pushes it further with five ratings of exactly $1000$, all of which must go.

Each test case spans two lines ($N$, then the array), but reading the entire input as one flat token stream makes the line breaks irrelevant — a cursor walks forward by $N$ after each case.

## Edge cases

- **A rating of exactly $1000$ counts as removed.** The list keeps problems *strictly below* $1000$, so the comparison is $\geq 1000$. The sample's fourth case is five ratings of exactly $1000$ and the answer is $5$ — an off-by-one here returns $0$.
- **Nothing to remove** (all ratings below $1000$): answer $0$, as in the last sample case.
- **Largest rating** ($D_i = 5000$): counted, like any other value at or above the threshold.
- **$N = 1$**: a single problem, removed or not.
- Only a count is needed, so the array never has to be stored or sorted — one pass with a running total suffices.

## Dry run

| ratings | at or above $1000$ | output |
|---|---|---:|
| $800, 1200, 900$ | $1200$ | `1` |
| $999, 1000, 1001, 1002$ | $1000, 1001, 1002$ | `3` |
| $1, 2, 2, 2, 5000$ | $5000$ | `1` |
| $1000 \times 5$ | all five | `5` |
| $900, 700, 800$ | none | `0` |

Row 2 shows $999$ staying and $1000$ going — the boundary in one line.
