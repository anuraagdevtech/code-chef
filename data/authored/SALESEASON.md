---
topic: Conditionals & Case Work
subtopic: Ordered threshold ladder
time: $O(1)$ per test case
space: $O(1)$
---
The discount is a step function of the bill $X$: nothing up to $100$, then $25$, then $100$, then $500$ above $5000$. The answer is $X$ minus whichever step applies.

The one thing to get right is that the bands are **half-open and ordered**, so an `if / elif` ladder tested from the smallest band upward is enough — once a branch matches, the later ones are skipped and the lower bound of each band is implied by the branch above it. Writing independent `if` statements instead would apply several discounts to the same bill.

Watch the boundaries, which are deliberately awkward: the first band is $X \le 100$, so $X = 100$ gets **no** discount, while $X = 101$ gets $25$. The third band is $1000 < X \le 5000$, so $X = 1000$ still sits in the $25$ band — sample case 4 pins this down, paying $1000 - 25 = 975$ rather than $900$.

A table-driven alternative is to store `(limit, discount)` pairs and walk them, which generalises better if the bands ever grow; for four fixed bands the explicit ladder is clearer.

## Edge cases

- **Exactly on each boundary.** $X = 100$ sits in the first band, so no discount; $X = 1000$ is still in the second band, so $25$ off, giving $975$ (the sample checks this); $X = 5000$ takes $100$ off.
- **One past a boundary.** $X = 101$ drops into the second band for $76$ — a single rupee more than $100$ costs $25$ less.
- **Smallest input** ($X = 1$): no discount, so $1$.
- **Largest input** ($X = 10000$): $500$ off, so $9500$.
- **Band order matters.** The tests are written ascending with `<=` so the first match wins; reordering them, or using open intervals, silently applies the wrong discount.
- The discount never exceeds the price in any band, so the answer cannot go negative.

## Dry run

| $X$ | band | discount | output |
|---:|---|---:|---|
| 15 | $X \leq 100$ | 0 | `15` |
| 70 | $X \leq 100$ | 0 | `70` |
| 250 | $100 < X \leq 1000$ | 25 | `225` |
| 1000 | $100 < X \leq 1000$ | 25 | `975` |

The last row is the boundary: $1000$ belongs to the second band, not the third.
