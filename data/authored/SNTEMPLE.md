---
topic: Arrays
subtopic: Runs computed from both directions
time: $O(n)$ per test case
space: $O(n)$
---
A temple with peak $x$ has heights $1, 2, \ldots, x-1, x, x-1, \ldots, 1$, which sum to

$$\underbrace{\frac{x(x-1)}{2}}_{\text{left}} + x + \underbrace{\frac{x(x-1)}{2}}_{\text{right}} = x^2$$

Everything else must be flattened to zero, and heights may only be **reduced**. So the total cost is $\sum h_i - x^2$, and minimising cost means **maximising the peak** $x$.

For a peak at index $i$, the left slope must descend $x-1, x-2, \ldots, 1$ and the right slope likewise. The tallest ascent that can end at $i$ is

$$\mathrm{left}[i] = \min\bigl(h_i,\ \mathrm{left}[i-1] + 1\bigr)$$

— capped by the block's own height, and by one more than whatever the previous block can support. The mirror recurrence going right-to-left gives $\mathrm{right}[i]$, and a peak at $i$ can reach

$$x_i = \min(\mathrm{left}[i], \mathrm{right}[i])$$

Taking the maximum over $i$ gives the best peak in two linear sweeps.

The `min` with $h_i$ is what encodes "reduce only" — a block can never be raised to support a taller slope.

Sample case 3, $[1,2,6,2,1]$, has a central block of height $6$, but its neighbours cap the slopes at $3$ on each side, so $x = 3$ and the cost is $12 - 9 = 3$ — the tall block is cut down to $3$. Sample case 2, $[1,1,2,1]$, supports $x = 2$ at index $2$, costing $5 - 4 = 1$: the leading block is flattened.

Sample case 1 is already a temple and costs nothing.

## Edge cases

- **Blocks may only be reduced, never raised**, so the tallest slope ending at a block is capped by its own height — which is what the two running arrays compute, one from each side.
- **The peak of the temple is $\min(\text{left}, \text{right})$ at that block**, since both arms must fit; the best temple is the largest such value over all positions.
- **A temple of peak $x$ uses $x^2$ blocks** ($1 + 2 + \dots + x + \dots + 2 + 1$), so the removal count is the total height minus $x^2$.
- **Every block outside the temple must go entirely**, which is why the answer subtracts from the full sum rather than from a window.
- **A peak of $1$ is always available** (a single block reduced to height $1$), so the answer is well defined even on a flat range.
- **The first sample is already a temple**, so nothing is removed.
- **A tall isolated block is wasted**: the third sample's $6$ can only support a peak of $3$, because its neighbours cap the arms.
- **$h_i$ up to $10^9$ with $n$ up to $10^5$** makes the total reach $10^{14}$, past 32-bit.

## Dry run

Third sample: $h = 1, 2, 6, 2, 1$.

| block | left arm | right arm | possible peak |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | **3** |
| 4 | 2 | 2 | 2 |
| 5 | 1 | 1 | 1 |

Best peak is $3$, using $9$ blocks out of a total height of $12$ — so `3` blocks are removed.
