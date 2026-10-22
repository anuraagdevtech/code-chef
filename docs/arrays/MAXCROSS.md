# 363. Maximal crosses

> CodeChef problem code [`MAXCROSS`](https://www.codechef.com/problems/MAXCROSS) &middot; difficulty **1570** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Maximal runs along rows, columns and both diagonals |
| **Time** | $O(n^2)$ |
| **Space** | $O(n^2)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

On the matrix A sized n×n, some cells were marked by crosses (X). For each cell (i,j) (with i – the row index, j – the column index), we define B(i,j) as the maximal number of continuous crosses “going across” the cell (i,j) in the same horizontal, vertical or diagonal; B(i,j)=0 if A(i,j) is empty ( '.' ).
[ Empty cells are marked by '.'] .

Clarification:

Continuous crosses going across cell (i,j) in horizontal direction = x1 + x2 - 1

where x1 = highest possible x such that

          j + x - 1<= n and A(i, j ... j + x - 1) are all 'X'

and x2 = highest possible x such that

          j - x + 1 > 0  and A(i, j - x + 1...j) are all 'X'

Similarily we can extend the definition for vertical and diagonal directions.

**Task**

Given matrix A as input, calculate matrix B.

**Input**

-  The first line contains the integer n.

                -  Then follow n lines , each containing n characters. The j-th character of the i-th line represents the cell (i,j) of the matrix A, with A(i,j)='X' if it contains a cross, or A(i,j)='.' if it is empty.

**Output**

Output n lines, each contains n integers, the j-th integer of the i-th line shows the value of B(i,j).
***(Each integer on a same line must be separated by exactly one space character)***

**Limitations**

0<n≤1 000

## Constraints

- $0 < n \leq 1000$
- each cell of $A$ is 'X' or '.'
- the input holds a single case (there is no leading $T$), and each output line separates its integers by exactly one space

## Sample

**Sample input**

```
10
..X....XX.
XX.X..XX.X
.....XX..X
.XXX..X.X.
.....X..XX
....X....X
X.X....XX.
.X...X.X.X
X.X..X....
..XXXXX.XX
```

**Sample output**

```
0 0 2 0 0 0 0 3 3 0
2 2 0 2 0 0 3 3 0 2
0 0 0 0 0 3 3 0 0 2
0 3 3 3 0 0 3 0 2 0
0 0 0 0 0 3 0 0 2 2
0 0 0 0 3 0 0 0 0 3
4 0 3 0 0 0 0 2 3 0
0 4 0 0 0 3 0 3 0 2
3 0 4 0 0 3 0 0 0 0
0 0 5 5 5 5 5 0 2 2
```

<details><summary>Explanation</summary>

**Cell $(0,0)$:** The cell is empty, thus $B(0,0) = 0$.

**Cell $(0,2)$:** The maximum number of continuous crosses are present diagonally to the bottom left and bottom right. The maximum number of crosses is $2$.

**Cell $(0,8)$:** The maximum number of continuous crosses are present diagonally to the bottom left. The maximum number of crosses is $3$.

**Cell $(9,2)$:** The maximum number of continuous crosses is present to the right. The maximum number of crosses is $5$.

</details>

## Approach

The statement's $x_1 + x_2 - 1$ definition is just a long way of saying "the length of the **maximal run** of crosses through $(i,j)$": $x_1$ reaches to the far end of the run, $x_2$ to the near end, and the overlap at $(i,j)$ itself is counted twice, hence the $-1$. So

$$B(i,j) = \max_{\text{4 directions}} \bigl(\text{length of the maximal run of 'X' containing } (i,j)\bigr)$$

and $0$ on an empty cell.

That reframing removes all the per-cell arithmetic. Instead of expanding outward from each cell — $O(n^3)$ in the worst case of a solid board — walk each **line** once, split it into maximal runs of crosses, and stamp the run's length onto all of its cells. There are four families of lines: $n$ rows, $n$ columns, and $2n-1$ diagonals in each of the two directions. Every cell lies on exactly four lines, so the whole computation is $O(n^2)$, with each cell taking the max over its four stamps.

The answer grid shows all four directions mattering somewhere. Cell $(1,3)$ scores $2$ from a diagonal (its own row and column give only $1$), while the bottom row's five-in-a-row horizontal gives the grid's maximum of $5$, and $(7,1)$ scores $4$ from an anti-diagonal running up-right.

Note a lone cross scores $1$, not $0$ — a run of length one still contains the cell. Only '.' yields $0$.

Also note the input has no leading $T$: just $n$ and the grid. At $n = 1000$ this is $4 \times 10^6$ cell visits, fine in C++ and merely slow in Python.

## Solution (Python)

```python
import sys

CROSS = 0x58


def stamp(cells, best):
    """Mark every cell of each maximal run with that run's length."""
    k = len(cells)
    i = 0
    while i < k:
        j = i
        while j < k and cells[j] is not None:
            j += 1
        if j > i:
            length = j - i
            for p in range(i, j):
                if length > best[cells[p]]:
                    best[cells[p]] = length
            i = j
        else:
            i += 1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grid = data[1:1 + n]
    best = [0] * (n * n)
    mark = [[(r * n + c) if grid[r][c] == CROSS else None for c in range(n)]
            for r in range(n)]

    for r in range(n):
        stamp(mark[r], best)
    for c in range(n):
        stamp([mark[r][c] for r in range(n)], best)
    # Diagonals keep r - c constant; anti-diagonals keep r + c constant, and
    # the two indices run over different ranges.
    for d in range(-n + 1, n):
        stamp([mark[r][r - d] for r in range(max(0, d), min(n, n + d))], best)
    for d in range(2 * n - 1):
        stamp([mark[r][d - r] for r in range(max(0, d - n + 1), min(n, d + 1))], best)

    out = [" ".join(map(str, best[r * n:(r + 1) * n])) for r in range(n)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

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

---

Same problem in rating order (#334 of 486): [../../by-rating/334-MAXCROSS.md](../../by-rating/334-MAXCROSS.md)
