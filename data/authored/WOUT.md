---
topic: Prefix Sums
subtopic: Difference array per row, then the best window of H rows
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The corridor is $H$ consecutive rows that must be empty in all $N$ columns, so clearing it costs $N \cdot H$ minus the number of cells in those rows that are already empty. We want the window of $H$ rows containing the most existing gap cells.

Each column contributes one gap cell to every row in $[l_i, h_i]$. Add all of these intervals with a difference array, take a prefix sum to get the number of gap cells in each row, and slide a window of $H$ rows over that array.

## Edge cases

- $H = N$: there is a single window and the answer is the number of soil cells.
- A column whose gap already covers the window contributes $H$ and costs nothing.
- The answer can reach $N \cdot H$, about $10^{12}$ for the largest inputs.
- Rows are 0-indexed from the bottom and the gap bounds are inclusive.

## Dry run

`N = 5, H = 2`, gaps `[2,3] [1,2] [2,3] [1,2] [2,3]`.

Gap cells per row 0-4: `0 2 5 3 0`. Windows of two rows: `2, 7, 8, 3`. The best holds 8 empty cells out of $5 \cdot 2 = 10$.

Answer $10 - 8 = 2$.
