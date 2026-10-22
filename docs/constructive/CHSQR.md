[&larr; 284. Prefix Permutation](PREFPERM.md) &middot; [Index](../../README.md) &middot; [300. K Odd Sum &rarr;](ADVITIYA5.md)

# 292. Chef and squares

> CodeChef problem code [`CHSQR`](https://www.codechef.com/problems/CHSQR) &middot; difficulty **1576** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A shifted cyclic Latin square |
| **Time** | $O(K^2)$ per test case |
| **Space** | $O(K)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

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

## Edge cases

- **$K$ is odd**, so the centre is a single cell at $((K-1)/2, (K-1)/2)$ and the distance to the nearest $1$ is well defined — an even $K$ would have four central cells and a different answer.
- **A Latin square forces a $1$ in every row**, so the nearest one can never be far: within $\lceil K/2 \rceil$ rows of the centre there must be a $1$, and the construction pushes it as far as that allows.
- **$K = 1$** is the degenerate case: the only cell holds $1$ and sits at the centre, so the distance is $0$.
- **The shift by $(K+1)/2$ is what maximises the distance.** A plain cyclic square $((c - r) \bmod K) + 1$ puts a $1$ on the main diagonal, which passes straight through the centre; shifting the diagonal moves it off.
- **Python's `%` on a negative operand returns a non-negative result**, which is what keeps `(c - r - s) % k` in range without an explicit `+ k`.
- **This square differs from the sample's** at $K = 3$ (`2 3 1 / 1 2 3 / 3 1 2` against `3 2 1 / 1 3 2 / 2 1 3`), but the $1$s sit in the same three cells, so both achieve the same $F(K)$ — a special judge measures the distance.

## Dry run

$K = 3$, so the shift is $s = 2$ and the centre is cell $(1,1)$ (0-based).

| row | row contents | position of the $1$ | distance to centre |
|---:|---|---|---:|
| 0 | `2 3 1` | $(0, 2)$ | 2 |
| 1 | `1 2 3` | $(1, 0)$ | **1** |
| 2 | `3 1 2` | $(2, 1)$ | **1** |

The closest $1$ is one step away, which is the best a $3 \times 3$ Latin square allows.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#335 of 486): [../../by-rating/335-CHSQR.md](../../by-rating/335-CHSQR.md)
