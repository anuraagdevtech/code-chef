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

## Edge cases

- **Four directions, and the two diagonal families index differently.** Diagonals keep $r - c$ constant, which ranges over $[-(n-1), n-1]$; anti-diagonals keep $r + c$ constant, which ranges over $[0, 2n-2]$. Reusing one loop range for both silently drops cells near a corner — a real bug here, caught by the sample.
- **An isolated `X` scores $1$**, since the statement's $x_1 + x_2 - 1$ counts the cell itself once in each direction.
- **A `.` cell scores $0$** regardless of its surroundings.
- **Each cell takes the maximum over the four directions**, so the stamping writes a run length only when it beats what is already recorded.
- **Every cell of a run gets the whole run's length**, not its distance from an end — the bottom row of the sample has five consecutive crosses, and all five report `5`.
- **There is no leading test count**: the input begins with $n$ and then the grid.
- **The output rows separate values by exactly one space**, so the whole row is joined at once.
- **$n$ up to $1000$** means $10^6$ cells and four passes, so the runs must be found with a linear sweep per line rather than by probing outward from each cell.

## Dry run

Take the cross at row $1$, column $3$ of the sample (1-based), whose answer is $2$.

| direction | run through it | length |
|---|---|---:|
| horizontal | just itself (`..X....XX.` has `.` on both sides) | 1 |
| vertical | rows $1$–$2$ of column $3$ are `X`, `.` | 1 |
| diagonal ($r - c$) | $(1,3)$ and $(2,4)$ are both `X` | **2** |
| anti-diagonal ($r + c$) | just itself | 1 |

Maximum is `2`.
