---
topic: Basic Math
subtopic: Manhattan bisector from an adjacent placement
time: $O(1)$ per test case
space: $O(1)$
---
Both fronts advance one cell per round, but the infection moves **first**, so a cell falls to whichever source reaches it sooner, with ties going to the infection:

$$\text{vaccinated} \iff d_V(c) < d_I(c)$$

with $d$ the Manhattan distance. Placing the vaccine in a cell **orthogonally adjacent** to the infection makes that comparison collapse to a single coordinate. For the vaccine one row below, at $(x+1, y)$, the column terms cancel and

$$d_V - d_I = |r - x - 1| - |r - x| < 0 \iff r \geq x+1$$

so the vaccine takes every row below the infection: $M(N-x)$ cells. The other three directions give $M(x-1)$, $N(M-y)$ and $N(y-1)$, and the answer is the largest:

$$\max\bigl(M(N-x),\ M(x-1),\ N(M-y),\ N(y-1)\bigr)$$

Adjacency is what makes this optimal. Moving the vaccine two rows away shifts the boundary to $r \geq x+2$, losing a whole row, and a diagonal placement cuts the region down to a quadrant, $(N-x)(M-y)$, which is never better than the half-grid. A distant corner is worse still, since the Manhattan bisector then slices diagonally.

The samples bear it out. On $3 \times 3$ with the infection at $(1,2)$, the vaccine at $(2,2)$ claims the two rows below — $6$ cells, leaving only the top row infected. On $3 \times 2$ with the infection in the corner $(1,1)$, the best is again downward: $2 \times 2 = 4$ cells, beating the $3 \times 1 = 3$ from going sideways.

## Edge cases

- **The infection moves first each round**, so the vaccine is always one step behind — which means it can never get around the infection, only block one side of it.
- **Placing the vaccine adjacent to the source claims that entire half-grid.** From $(x+1, y)$ the vaccine spreads across rows $x+1 \dots N$ before the infection can reach them, saving $M(N-x)$ cells.
- **So the answer is the largest of the four half-grids**, one per direction — and the best direction is simply the one with the most cells beyond the source.
- **A source on an edge kills one direction**, making the opposite side the obvious choice: the second sample's $(1,1)$ has nothing above or to the left.
- **The vaccine must go on a non-infected cell**, which an adjacent cell always is at time $0$.
- **$N, M \geq 2$** guarantees at least one adjacent cell exists in some direction.
- **Products reach $10^{10}$** at $N = M = 10^5$, past 32-bit.

## Dry run

First sample: a $3 \times 3$ grid with the infection at $(1, 2)$.

| vaccine direction | cells claimed |
|---|---:|
| below, at $(2,2)$ | $3 \times (3-1) = $ **6** |
| above | $3 \times 0 = 0$ |
| right, at $(1,3)$ | $3 \times (3-2) = 3$ |
| left, at $(1,1)$ | $3 \times (2-1) = 3$ |

Output `6` — the whole bottom two rows are saved.
