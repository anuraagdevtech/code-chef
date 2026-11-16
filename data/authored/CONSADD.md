---
topic: Arrays
subtopic: Greedy elimination with window operations, rows first and then the last columns
time: $O(R \cdot C)$ per test case
space: $O(R \cdot C)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Work with the difference $D = A - B$; the goal is to make it all zero.

Sweep each row from left to right. The leftmost non-zero cell of a row can only be fixed (as far as row operations go) by the window that starts there, so apply that window with the right value whenever it fits. A difference array carries the effect of the windows already applied. Afterwards every row is zero except possibly in its last $X - 1$ columns, where no window can start.

Now do the same down each of those last $X - 1$ columns with vertical windows: the topmost non-zero cell is cancelled by the window starting there. What may remain are cells in the last $X - 1$ rows of the last $X - 1$ columns; if any of them is non-zero the answer is No.

Vertical windows in the earlier columns need not be considered: modulo row operations, a unit in column $j$ is an integer combination of units in the last $X - 1$ columns of the same row, so such a window is already a combination of the operations used.

## Edge cases

- $X = 1$: every single cell can be adjusted and the answer is always Yes.
- $X$ larger than both dimensions: no operation exists, so $A$ must already equal $B$.
- $X$ larger than the row length but not the column length: only vertical windows exist; the row sweep then changes nothing.
- Values of $v$ may be negative and unbounded, so only the linear structure matters.

## Dry run

Sample 1: $A = \begin{pmatrix}1 & 2\\ 0 & 1\end{pmatrix}$, $B = 0$, $X = 2$, so $D = A$.

Rows: in row 1 the window at column 1 cancels the 1 and turns the row into `0 1`; row 2 is already `0 1`.

Last column: the vertical window at the top cancels the 1 in row 1 and, with it, the 1 in row 2. Nothing is left, so the answer is Yes.
