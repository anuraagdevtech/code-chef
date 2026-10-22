---
topic: Graphs
subtopic: Connected components, then alternating greedy picks
time: $O(NM)$ per test case
space: $O(NM)$
---
A turn captures one whole connected region of land — the cell chosen plus everything reachable from it through side-adjacent land. So the board is just a **multiset of component sizes**, and the game is "players alternately take one item, each wanting the largest total".

With independent items taken whole, both players simply take the biggest remaining component: swapping any choice for a larger available one strictly helps the chooser and never helps the opponent, so the greedy is the unique optimum. Sorting the sizes descending, Chef (first) takes positions $0, 2, 4, \ldots$ and Mike takes $1, 3, 5, \ldots$, so the answer — Mike's total — is

$$\sum_{j \text{ odd}} \text{size}_{(j)}$$

Finding the components is a flood fill over the grid. $N$ and $M$ reach $10^5$ individually, but $\sum NM \leq 10^6$, so the grid is always narrow in one direction and a flat array indexed by $r \cdot M + c$ with an explicit stack handles it without recursion depth trouble.

The samples show the three shapes. The $4 \times 4$ board has sizes $4, 1, 1, 1, 1$: Chef takes the block of four and then a corner, Mike takes two corners, so $2$. The $2 \times 2$ board is one component of four — Chef takes everything and Mike gets $0$. And the diagonal board has three singletons, giving Mike exactly $1$.

Note that it is the *sorted* order that matters, not the layout: the four corners of the first board are symmetric, so only their count enters the answer.

## Edge cases

- **A turn captures a whole connected component**, since the player keeps taking neighbouring land — so the game reduces to dealing out component sizes.
- **Both players take the largest component left**, which is optimal for each: a component once taken is gone, so grabbing the biggest maximises your own total and denies it to the opponent.
- **Chef plays second**, so he receives the $2$nd, $4$th, $6$th largest — the odd indices of the descending list, which is exactly `sizes[1::2]`.
- **A single component gives Chef nothing** (the second sample, one $2 \times 2$ block), since Mike takes it all.
- **Equal-sized components split evenly**, as in the third sample's three singletons where Chef gets one.
- **Adjacency is by shared side only**, so diagonal land forms separate components — which is why the third sample's diagonal gives three components rather than one.
- **The flood fill uses an explicit stack**, since $N \cdot M$ reaches $10^6$ and recursion would overflow.
- **The grid is flattened to a single `bytearray`**, with cells indexed as $r \cdot M + c$, keeping the fill allocation-free.

## Dry run

First sample: the $4 \times 4$ grid has four corner singletons and one central $2 \times 2$ block.

| component | size |
|---|---:|
| central block | 4 |
| each corner | 1 |

Sorted descending: $4, 1, 1, 1, 1$.

| turn | player | takes |
|---:|---|---:|
| 1 | Mike | 4 |
| 2 | **Chef** | 1 |
| 3 | Mike | 1 |
| 4 | **Chef** | 1 |
| 5 | Mike | 1 |

Chef's total is `2`.
