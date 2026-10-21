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
