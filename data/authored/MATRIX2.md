---
topic: Dynamic Programming
subtopic: Largest upper-triangular square from the row run and the diagonal neighbour
time: $O(N \cdot M)$
space: $O(M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $f(i, j)$ be the largest $h$ for which the square with top-left corner $(i, j)$ has ones on and above its main diagonal. Every smaller $h$ works as well, so the answer is the sum of $f$ over all cells.

Such a square of size $h$ is its first row - $h$ consecutive ones starting at $(i, j)$ - together with an upper-triangular square of size $h-1$ whose corner is $(i+1, j+1)$. Hence

$$f(i, j) = \min(\text{run}(i, j),\; f(i+1, j+1) + 1),$$

where $\text{run}(i, j)$ is the number of consecutive ones to the right starting at $(i, j)$. Process rows from the bottom up and columns from right to left, keeping only the previous row of $f$.

## Edge cases

- A zero cell has run 0 and contributes nothing.
- On the last row or the last column the diagonal neighbour is outside the matrix, treated as 0, so $f \le 1$ there.
- The count can reach roughly $N \cdot M \cdot \min(N, M) / 2$; Python integers do not overflow.
- There is a single test case and the rows are given as strings without spaces.

## Dry run

Sample `011 / 111`.

Bottom row `111`: runs from the right are 1, 2, 3 and there is nothing below, so $f = 1, 1, 1$ (sum 3).

Top row `011`: column 3 has run 1, giving 1; column 2 has run 2 and the diagonal neighbour has $f = 1$, giving $\min(2, 2) = 2$; column 1 is a zero, giving 0 (sum 3).

Total 6.
