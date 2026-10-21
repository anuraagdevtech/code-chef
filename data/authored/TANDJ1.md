---
topic: Basic Math
subtopic: Grid reachability by distance and parity
time: $O(1)$ per test case
space: $O(1)$
---
Each step changes one coordinate by one, so the shortest route from $(a,b)$ to $(c,d)$ is the **Manhattan distance**

$$D = |a - c| + |b - d|$$

Reaching the target in *exactly* $K$ steps needs two conditions:

1. $K \geq D$ — the train cannot arrive faster than the direct route.
2. $K - D$ is **even** — any surplus must be burned off in wasted moves, and every detour returns to the same square only after an even number of steps (one away, one back).

Both are necessary and together sufficient, since surplus steps can always be spent pacing between two adjacent cells.

The parity condition is the whole problem, and it comes from a colouring argument: tint the grid like a chessboard, and each step changes colour. So after $K$ steps the train sits on a cell whose colour is determined by $K$'s parity, and $D$ fixes the colour of the target relative to the start. If those disagree, no route of length $K$ exists however long you wander.

Sample case 2 is the parity failure: $D = 3$ and $K = 4$ differ by an odd amount, so `NO` even though $K > D$. Sample case 1 has $K = D = 2$ exactly, and case 3 has a surplus of $2$ to waste.

The grid is $10^5$ on a side and $K$ reaches $2 \times 10^5$, but the walls never bind — there is always room to pace — so the bounds need no special handling.

## Edge cases

- **Surplus steps must be wasted in pairs.** Stepping away and back costs two moves, so $K - \mathrm{dist}$ has to be even — the second row has more than enough steps ($4$ against a distance of $3$) and still fails on parity.
- **Too few steps** → `NO` regardless of parity, which the `k >= dist` half of the test covers.
- **Exactly $K = \mathrm{dist}$** → `YES`, since a gap of $0$ is even (the first row).
- **Coordinates may be $0$** (the third row's target is $(1, 0)$), and the walk is unbounded, so no clamping to a grid is needed.
- **$(a,b) \neq (c,d)$ is guaranteed**, so the distance is at least $1$ and the degenerate "already there with $K = 0$" case never arises.
- **$T$ up to $10^5$** with constant work per case, read in one buffered call.

## Dry run

| from | to | Manhattan distance | $K$ | $K - \mathrm{dist}$ | even? | output |
|---|---|---:|---:|---:|:---:|---|
| $(1,1)$ | $(2,2)$ | 2 | 2 | 0 | yes | `YES` |
| $(1,1)$ | $(2,3)$ | 3 | 4 | 1 | **no** | `NO` |
| $(1,1)$ | $(1,0)$ | 1 | 3 | 2 | yes | `YES` |

Row 3 uses one step to arrive and wastes the other two on a step out and back.
