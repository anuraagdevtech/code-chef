---
topic: Dynamic Programming
subtopic: Profile tiling with exponentiated transfer matrices
time: $O(\log N)$ per test case after $O(\log N_{max})$ fixed-size matrix preprocessing
space: $O(\log N_{max})$ for fixed-size matrix powers
complexity_note: Auxiliary space excludes the buffered input and output.
---
A column has two cells. Represent cells already covered from the previous column by a two-bit mask. Fill the first uncovered cell with either a one-cell block or one of the four orientations of an L-shaped three-cell block. The L block occupies cells in the current and next column. Reject overlaps and accumulate a transition to the resulting next-column mask.

This produces a $4	imes4$ transfer matrix. Starting from empty mask zero, after $N$ transitions the coefficient of empty mask zero counts exactly complete walls. Precompute binary powers of the matrix once, then multiply the initial row vector by powers selected by the bits of $N$. All arithmetic is modulo $10^9+7$.

## Edge cases

- Only final mask zero is a completed wall.
- All four L rotations are allowed.
- A single-column wall has just the two single-cell blocks.
- Precompute powers once across the test cases.

## Dry run

For width two, there is one arrangement using only single cells and four arrangements containing one L block with one single cell. Thus the answer is 5.
