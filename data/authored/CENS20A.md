---
topic: Prefix Sums
subtopic: Two-dimensional xor difference array
time: $O(N \cdot M + Q)$
space: $O(N \cdot M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A query flips every bit of a rectangle, and flips compose by xor, so a cell ends up flipped exactly when an odd number of rectangles cover it. The order of the queries is irrelevant.

Use a 2D difference array over GF(2): for a rectangle with corners $(x_1, y_1)$ and $(x_2, y_2)$ toggle the four cells $(x_1, y_1)$, $(x_1, y_2 + 1)$, $(x_2 + 1, y_1)$ and $(x_2 + 1, y_2 + 1)$. The 2D prefix xor of this array is then 1 exactly on the cells covered an odd number of times.

After all queries, compute the prefix xor row by row (a running xor along the row combined with the finished row above) and xor it with the original matrix.

## Edge cases

- A cell flipped twice returns to its original value.
- The difference array needs one extra row and column for the far corners.
- Rows are given as strings without separators and must be printed the same way.
- With up to $10^6$ queries, each must cost $O(1)$.

## Dry run

`2 x 2` zero matrix, queries `(1,1)-(1,1)`, `(2,2)-(2,2)`, `(1,1)-(2,2)`.

Coverage counts per cell: `2 1 / 1 2`. Odd coverage is on the anti-diagonal, so those cells are flipped.

Output `01` / `10`.
