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
