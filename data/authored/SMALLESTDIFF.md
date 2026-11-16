---
topic: Constructive
subtopic: A tight window of sorted values for the path, with decoys beside it
time: $O(N M \log (N M))$ per test case
space: $O(N M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The car visits exactly $L = N + M - 1$ cells, and the aim is to make the difference between the largest and the smallest visited value as small as possible. The best conceivable choice is a window of $L$ consecutive values in sorted order - but the grid has to force the car along the cells holding them.

Assume $N \le M$ (otherwise build the transposed grid). Lay the window down the first column and then along the last row. While the car is in the first column, at row $i$ the mover chooses between the cell below (on the path) and the cell to the right (a decoy). Chef moves on even steps and takes the larger value, so the decoy must be smaller than the path cell; Chefina moves on odd steps and takes the smaller, so the decoy must be larger. In the last row only moves to the right exist.

So $\lceil (N-1)/2 \rceil$ decoys must be smaller than the whole window and $\lfloor (N-1)/2 \rfloor$ larger. Among all windows of $L$ consecutive sorted values that leave enough smaller values before them and enough larger values after them, take the one with the smallest spread. Place the window on the path, the decoys in the second column, and fill the other cells with the remaining values in any order.

At least $\min(N, M) - 1$ decisions are made before the car first touches the far boundary, each needing a rejected neighbour on the appropriate side, which is why no arrangement can do better than such a window.

## Edge cases

- All values are distinct, so every decision is unambiguous.
- For $N > M$ the roles of rows and columns are swapped by transposing at the end.
- With $N = 2$ only one decoy, a smaller value, is needed.
- Several grids are optimal, so the output is validated by a checker.

## Dry run

`2 x 2` with values `5 10 20 40`. $L = 3$; one smaller decoy is needed and no larger one.

The only window leaving one value below it is `10 20 40`. Path: `10` at $(1,1)$, `20` at $(2,1)$, `40` at $(2,2)$. Decoy `5` at $(1,2)$.

Grid `10 5 / 20 40`: Chef moves down to 20 (larger than 5), Chefina then has only the move to 40. Spread $40 - 10 = 30$.
