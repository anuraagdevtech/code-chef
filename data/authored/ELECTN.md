---
topic: Arrays
subtopic: Counting with a predicate
time: $O(N)$ per test case
space: $O(1)$
---
A person votes when their age is **at least** $X$, so the answer is the number of array entries satisfying $A_i \geq X$ — one linear scan with a counter, no sorting and no auxiliary storage.

In Python, `sum(1 for a in ages if a >= x)` expresses it directly; summing the boolean generator counts the matches. The structure is identical to the to-do-list problem, with only the comparison direction and the threshold changed, which is the point of seeing both: "count the elements passing a test" is a single reusable shape.

The wording "at least $X$" makes the comparison inclusive, so someone aged exactly $X$ *can* vote. Sample case 3 leans on this — with $X = 2$ and ages $2, 1, 2, 4$, the two people aged exactly $2$ both count, giving $3$. Using a strict `>` would wrongly return $1$.

The answer can legitimately be zero, as in case 4 where nobody reaches the voting age of $6$, so there is no need to special-case an empty result.

Each test case spans two lines and $N$ varies between cases, so a cursor into the flat token stream is the tidiest way to walk the input.

## Edge cases

- **An age exactly $X$ votes**, since the rule is "at least $X$". The sample's third case has $X = 2$ with two voters aged exactly $2$, and both count — an off-by-one gives $1$ instead of $3$.
- **Nobody eligible**: the last sample case sets $X = 6$ above every age, so the answer is $0$.
- **Everybody eligible** when $X$ is at or below the minimum age.
- **$N = 1$**: a single citizen, counted or not.
- Only the tally is needed, so the ages never have to be stored or sorted.

## Dry run

| $X$ | ages | aged $\geq X$ | output |
|---:|---|---|---:|
| 3 | $5, 3, 1, 2$ | $5, 3$ | `2` |
| 2 | $1, 3, 4$ | $3, 4$ | `2` |
| 2 | $2, 1, 2, 4$ | $2, 2, 4$ | `3` |
| 6 | $1, 2, 3, 4, 5$ | none | `0` |

Row 3 is the inclusive boundary: both twos vote.
