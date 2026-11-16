---
topic: Geometry
subtopic: Clip a Chebyshev-distance square to the chessboard
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A king reaches a square in the larger of its row and column displacements, since a diagonal move can reduce both at once. Thus reachable rows lie in $[R-K,R+K]$ and columns in $[C-K,C+K]$. Clip both intervals to 1 through 8 and multiply their lengths.

## Edge cases

- Include the starting square: the limit is at most $K$ moves.
- Clip both ends independently at board boundaries.
- Large $K$ reaches all 64 squares.

## Dry run

For `(R,C,K)=(1,3,1)`, reachable rows are 1 through 2 and columns 2 through 4, giving `2*3=6`.
