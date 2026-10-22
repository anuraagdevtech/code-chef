# 452. Save People

> [`FIZZBUZZ2306`](https://www.codechef.com/problems/FIZZBUZZ2306) &middot; difficulty **1750** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Manhattan bisector from an adjacent placement |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has a $2$-D grid with $N$ rows and $M$ columns. The cell at the intersection of the $i$-th row and $j$-th column is denoted cell $(i, j)$.
Initially, *only* cell $(x, y)$ of the grid is infected.

Chef can select **exactly one** non-infected cell and *vaccinate* it.
Then, the infection and the vaccine spread across the grid, as follows:
- First, any cell that is neither vaccinated nor infected, but is adjacent (horizontally or vertically) to an infected cell, becomes infected itself.
- Next, any cell that is neither vaccinated nor infected, but is adjacent (horizontally or vertically) to a vaccinated cell, becomes vaccinated itself.

This process repeats till every cell in the grid is either infected or vaccinated.
For example, on a $6\times 6$ grid with $(x, y) = (2, 2)$ and the vaccine placed at $(5, 4)$ initially, the spread would look like:
<img src = "https://cdn.codechef.com/download/Contest+images/START106/image_5.gif" width=400 />

Find the **maximum** possible number of vaccinated cells Chef can obtain, if he chooses the initial position of the vaccine optimally.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the dimensions of the grid.
    - The second line of each test case contains two space-separated integers $x$ and $y$ — the coordinates of the infected cell.

**Output**

For each test case, output on a new line the maximum number of vaccinated cells attainable.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N, M \leq 10^5$
- $1 \leq x \leq N$
- $1 \leq y \leq M$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
3 3
1 2
3 2
1 1
```

**Sample output**

```
6
4
```

<details><summary>Explanation</summary>

**Test case $1$:** It's optimal to vaccinate cell $(2, 2)$.
The spread of infection and vaccine is visualized below.
![](https://cdn.codechef.com/download/Contest+images/START106/image_4.gif)

$6$ cells are vaccinated, and this is the best we can do.

**Test case $2$:** It's optimal to vaccinate cell $(2, 1)$.
The spread of infection and vaccine is visualized below.
![](https://cdn.codechef.com/download/Contest+images/START106/image_3.gif)

$4$ cells are vaccinated, which is the best we can do.

</details>

## Approach

Both fronts advance one cell per round, but the infection moves **first**, so a cell falls to whichever source reaches it sooner, with ties going to the infection:

$$\text{vaccinated} \iff d_V(c) < d_I(c)$$

with $d$ the Manhattan distance. Placing the vaccine in a cell **orthogonally adjacent** to the infection makes that comparison collapse to a single coordinate. For the vaccine one row below, at $(x+1, y)$, the column terms cancel and

$$d_V - d_I = |r - x - 1| - |r - x| < 0 \iff r \geq x+1$$

so the vaccine takes every row below the infection: $M(N-x)$ cells. The other three directions give $M(x-1)$, $N(M-y)$ and $N(y-1)$, and the answer is the largest:

$$\max\bigl(M(N-x),\ M(x-1),\ N(M-y),\ N(y-1)\bigr)$$

Adjacency is what makes this optimal. Moving the vaccine two rows away shifts the boundary to $r \geq x+2$, losing a whole row, and a diagonal placement cuts the region down to a quadrant, $(N-x)(M-y)$, which is never better than the half-grid. A distant corner is worse still, since the Manhattan bisector then slices diagonally.

The samples bear it out. On $3 \times 3$ with the infection at $(1,2)$, the vaccine at $(2,2)$ claims the two rows below — $6$ cells, leaving only the top row infected. On $3 \times 2$ with the infection in the corner $(1,1)$, the best is again downward: $2 \times 2 = 4$ cells, beating the $3 \times 1 = 3$ from going sideways.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 4 * i]), int(data[2 + 4 * i])
        x, y = int(data[3 + 4 * i]), int(data[4 + 4 * i])
        # An adjacent vaccine claims the whole half-grid on its side.
        out.append(str(max(m * (n - x), m * (x - 1), n * (m - y), n * (y - 1))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The infection moves first each round**, so the vaccine is always one step behind — which means it can never get around the infection, only block one side of it.
- **Placing the vaccine adjacent to the source claims that entire half-grid.** From $(x+1, y)$ the vaccine spreads across rows $x+1 \dots N$ before the infection can reach them, saving $M(N-x)$ cells.
- **So the answer is the largest of the four half-grids**, one per direction — and the best direction is simply the one with the most cells beyond the source.
- **A source on an edge kills one direction**, making the opposite side the obvious choice: the second sample's $(1,1)$ has nothing above or to the left.
- **The vaccine must go on a non-infected cell**, which an adjacent cell always is at time $0$.
- **$N, M \geq 2$** guarantees at least one adjacent cell exists in some direction.
- **Products reach $10^{10}$** at $N = M = 10^5$, past 32-bit.

## Dry run

First sample: a $3 \times 3$ grid with the infection at $(1, 2)$.

| vaccine direction | cells claimed |
|---|---:|
| below, at $(2,2)$ | $3 \times (3-1) = $ **6** |
| above | $3 \times 0 = 0$ |
| right, at $(1,3)$ | $3 \times (3-2) = 3$ |
| left, at $(1,1)$ | $3 \times (2-1) = 3$ |

Output `6` — the whole bottom two rows are saved.

---

Same problem grouped by topic: [../docs/basic-math/FIZZBUZZ2306.md](../docs/basic-math/FIZZBUZZ2306.md)
