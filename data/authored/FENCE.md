---
topic: Sets
subtopic: Perimeter as sides minus shared edges
time: $O(K)$ per test case
space: $O(K)$
---
The two conditions say the fence must be exactly the **boundary of the plant region**: passable between adjacent plants, impassable everywhere else. So a cell side needs a fence precisely when it separates a plant from a non-plant — another plant's side, the weeds, or the outside.

Count from the plants' point of view. Each of the $K$ plant cells has $4$ sides, giving $4K$ in all. A side shared by **two** plants is counted twice and needs no fence, so each adjacent plant pair removes $2$:

$$\text{answer} = 4K - 2P, \qquad P = \#\{\text{side-adjacent plant pairs}\}$$

Every other side borders weeds or the grid edge and must be fenced, which is why the grid dimensions $N$ and $M$ never enter the formula — a plant on the boundary fences that side against the outside exactly as it would against weeds.

With $N, M$ up to $10^9$ the grid cannot be materialised, but $K \leq 10^5$, so store the plant coordinates in a hash set and count $P$ by checking, for each plant, whether the cell to its right and the cell below are also plants. Looking only right and down counts each pair once.

The first sample has $9$ plants in a horseshoe shape with $8$ adjacencies, giving $36 - 16 = 20$. The isolated plant at $(1,4)$ contributes its full $4$ sides, three against weeds and one against the grid edge — which is what makes that shape's answer larger than a compact block of nine would be. The second sample is that single-cell case alone: $4 - 0 = 4$.

## Edge cases

- **The fence is the boundary of the plant region**, so its length is the region's perimeter: four sides per cell, minus two for every shared edge between adjacent plants.
- **Each adjacent pair must be counted once**, which is why only the right and down neighbours are probed — checking all four directions double-counts every edge.
- **A single plant** gives $4$ (the second sample row), with no shared edges.
- **The grid may be enormous** ($N, M$ up to $10^9$) while $K$ is at most $10^5$, so the cells must live in a hash set rather than a grid — a dense array is out of the question.
- **The plant cells are pairwise distinct**, so the set size really is $K$ and no deduplication is needed.
- **Diagonal adjacency does not count**, since the statement defines adjacency by a shared side.
- **Disconnected plant regions are fine**: the formula sums the perimeters of all of them, which is exactly the total fencing needed.

## Dry run

First sample: $K = 9$ plants in a $4 \times 4$ field.

| plant | right neighbour? | down neighbour? |
|---|:---:|:---:|
| $(1,4)$ | no | no |
| $(2,1)$ | yes | yes |
| $(2,2)$ | yes | no |
| $(2,3)$ | no | yes |
| $(3,1)$ | no | yes |
| $(3,3)$ | no | yes |
| $(4,1)$ | yes | no |
| $(4,2)$ | yes | no |
| $(4,3)$ | no | no |

Eight shared edges, so $4 \cdot 9 - 2 \cdot 8 = 36 - 16 = $ `20`.
