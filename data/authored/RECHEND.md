---
topic: Arrays
subtopic: A diagonal chain of blocks touching both boundary arcs separates the corners
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A monotone path from the top-left to the bottom-right corner is impossible exactly when a chain of blocked cells, connected through edges or corners, links the "upper-right" boundary (the top row or the right column) with the "lower-left" boundary (the bottom row or the left column) - such a chain is a wall between the two corners.

There is exactly one block in every row and in every column, so two blocks can only touch diagonally, and only if they are in consecutive rows with columns that differ by one. The chains are therefore maximal runs of consecutive rows in which the block column changes by exactly $\pm 1$ from row to row.

Scan the rows in order. Start a new chain whenever the column jumps by anything other than 1. A chain touches the upper-right boundary if it contains row 1 or column $N$, and the lower-left boundary if it contains row $N$ or column 1. If some chain touches both, print NO; otherwise YES.

## Edge cases

- The start and the end cell are guaranteed to be free.
- A lone block in the top-right or bottom-left corner touches only one arc and blocks nothing by itself.
- The full anti-diagonal is one chain touching both arcs.
- The flags must be reset together when a chain ends.

## Dry run

`N = 3`, blocks at `(1,2) (2,3) (3,1)`, i.e. columns by row `2 3 1`.

- Row 1, column 2: new chain; it contains row 1, so it touches the upper-right arc.
- Row 2, column 3: differs by 1, same chain; still only the upper-right arc.
- Row 3, column 1: differs by 2, new chain; it contains row 3 and column 1, the lower-left arc only.

No chain touches both arcs: YES. For `N = 2` with columns `2 1` the single chain contains row 1 and row 2: NO.
