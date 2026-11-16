---
topic: Sorting
subtopic: Exchange argument - order rods by beauty per unit length
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Take two rods $x$ and $y$ that are adjacent in the arrangement. Swapping them does not move any other rod. If $x$ comes first, $y$ starts $A_x$ later than otherwise and the pair contributes an extra $A_x B_y$; if $y$ comes first the extra is $A_y B_x$. So $x$ should be before $y$ when

$$A_x B_y \ge A_y B_x \iff \frac{B_x}{A_x} \le \frac{B_y}{A_y}.$$

Sorting by increasing $B / A$ makes every adjacent pair optimal, and by the usual exchange argument the whole order is optimal: rods that are long and not very beautiful go first, pushing the valuable short ones to large coordinates. The comparison is done with integer cross products to avoid floating point, and the answer is accumulated in one pass.

## Edge cases

- Equal ratios can be ordered either way without changing the total.
- A single rod starts at 0 and scores 0.
- Cross-multiplication keeps the comparison exact.
- The total can reach about $10^{17}$.

## Dry run

Rods (length, beauty): `(1, 4)` and `(2, 6)`. Ratios 4 and 3, so the rod `(2, 6)` goes first.

Positions: 0 for `(2, 6)`, 2 for `(1, 4)`. Beauty $0 \cdot 6 + 2 \cdot 4 = 8$.

The other order would give $1 \cdot 6 = 6$.
