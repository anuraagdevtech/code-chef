---
topic: Arrays
subtopic: Maximal runs along rows, columns and both diagonals
time: $O(n^2)$
space: $O(n^2)$
---
The statement's $x_1 + x_2 - 1$ definition is just a long way of saying "the length of the **maximal run** of crosses through $(i,j)$": $x_1$ reaches to the far end of the run, $x_2$ to the near end, and the overlap at $(i,j)$ itself is counted twice, hence the $-1$. So

$$B(i,j) = \max_{\text{4 directions}} \bigl(\text{length of the maximal run of 'X' containing } (i,j)\bigr)$$

and $0$ on an empty cell.

That reframing removes all the per-cell arithmetic. Instead of expanding outward from each cell — $O(n^3)$ in the worst case of a solid board — walk each **line** once, split it into maximal runs of crosses, and stamp the run's length onto all of its cells. There are four families of lines: $n$ rows, $n$ columns, and $2n-1$ diagonals in each of the two directions. Every cell lies on exactly four lines, so the whole computation is $O(n^2)$, with each cell taking the max over its four stamps.

The answer grid shows all four directions mattering somewhere. Cell $(1,3)$ scores $2$ from a diagonal (its own row and column give only $1$), while the bottom row's five-in-a-row horizontal gives the grid's maximum of $5$, and $(7,1)$ scores $4$ from an anti-diagonal running up-right.

Note a lone cross scores $1$, not $0$ — a run of length one still contains the cell. Only '.' yields $0$.

Also note the input has no leading $T$: just $n$ and the grid. At $n = 1000$ this is $4 \times 10^6$ cell visits, fine in C++ and merely slow in Python.
