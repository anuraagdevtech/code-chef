# 1576 &middot; Chef and squares

> CodeChef problem code [`CHSQR`](https://www.codechef.com/problems/CHSQR) &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A shifted cyclic Latin square |
| **CodeChef tags** | `Algorithms`, `Implementation` |
| **CodeChef category** | easy |
| **Time** | $O(K^2)$ per test case |
| **Space** | $O(K)$ |

Same write-up grouped by topic: [../docs/constructive/CHSQR.md](../docs/constructive/CHSQR.md)

## Question

Chef has finished his freshman year in college. As a present, his parents gave him a new problem to solve:

Chef has to fill a **K x K** square grid of integers in a certain way. Let us say that such a grid is *valid* if:

- Each cell contains an integer from **1** and **K** (inclusive).

   - No integer appears twice in the same row or the same column.

Let **F(K)** be maximum possible distance between the center of the square and the closest cell that contains **1**, among all possible squares with the side length **K**.

Here, we use the following notions:

-  The distance between cell **(x, y)** and **(i, j)** is equal to **|x-i|+|y-j|**.

  -  The center of a **K x K** square is cell **((K+1)/2, (K+1)/2)** for odd **K**.

**Input**

The first line of input contains a single integer **T** denoting the number of test cases.

Each test case consists of a single line containing a single odd integer **K**.

 

**Output**

For each test case, print **K** lines each consisting of **K** space separated integers giving some square grid where the distance from the center of the grid to the nearest **1** is exactly **F(K)**. If there's more than 1 possible answer output any of them.

 

**Constraints**

- **K_i** is odd.

**Subtask #1** (10 points)  :
-  **1** ≤ **T** ≤ **50**

-  **1** ≤ **K_i**≤ **5**

**Subtask #1** (90 points)  :
-  **1** ≤ **T** ≤ **10**

-  **1** ≤ **K_i** < **400**

## Constraints

- K_i is odd.

## Sample

**Sample input**

```
2
1
3
```

**Sample output**

```
1
3 2 1
1 3 2
2 1 3
```

## Approach

**What $F(K)$ is.** Row $\frac{K+1}{2}$ — the centre row — contains exactly one $1$, somewhere in columns $1 \ldots K$. Its distance to the centre is purely horizontal and at most $\frac{K-1}{2}$. So

$$F(K) \leq \frac{K-1}{2}$$

and the task is to build a grid achieving it.

**The construction.** Take the cyclic Latin square shifted by $s = \frac{K+1}{2}$:

$$L[r][c] = \bigl((c - r - s) \bmod K\bigr) + 1 \qquad (0\text{-indexed})$$

Each row is a rotation of $1 \ldots K$ and each column likewise, so it is a valid Latin square by construction. The $1$s sit exactly where $c \equiv r + s \pmod K$ — a diagonal wrapped by half the board.

Checking the distances with $m = \frac{K-1}{2}$ as the centre index: the row $r = m$ places its $1$ at column $0$, distance $m$; rows $m+1$ and $K-1$ also give $m$; and every other row gives $m+1$ or more. So the minimum is exactly $m$, meeting the bound.

The half-board shift is what matters. The *unshifted* cyclic square puts its $1$s on the main diagonal, which passes straight through the centre — distance $0$, the worst possible. Rotating by $\frac{K+1}{2}$ pushes the diagonal as far from the centre as it can go.

$K = 1$ falls out correctly: the single cell is the centre and holds $1$, so $F(1) = 0$.

For $K = 3$ this yields

```
2 3 1
1 2 3
3 1 2
```

whose nearest $1$ to the centre is at distance $1 = F(3)$. The published sample is a different grid with the same property — **any** valid answer is accepted, so this is judged by a checker.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[1 + i])
        # Shifting the cyclic square by (k+1)/2 pushes the diagonal of 1s
        # as far from the centre as a Latin square allows.
        s = (k + 1) // 2
        for r in range(k):
            row = [str((c - r - s) % k + 1) for c in range(k)]
            out.append(" ".join(row))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(K^2)$ per test case
- **Space:** $O(K)$
