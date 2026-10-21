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
