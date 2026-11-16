[&larr; 603. Full Path Eraser](603-FPE.md) &middot; [Index](README.md) &middot; [605. TripTastic &rarr;](605-TRPTSTIC.md)

# 604. Can You Reach The End

> [`RECHEND`](https://www.codechef.com/problems/RECHEND) &middot; difficulty **2095** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | A diagonal chain of blocks touching both boundary arcs separates the corners |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `2D Arrays`, `Sorting`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given a positive integer $N$. Consider a square grid of size $N \times N$, with rows numbered  $1$ to $N$ from top to bottom and columns numbered $1$ to $N$ from left to right. Initially you are at $(1,1)$ and you have to reach $(N,N)$. From a cell you can either move one cell to the right or one cell down (if possible). Formally, if you are at $(i,j)$, then you can either move to $(i+1,j)$ if $i \lt N$, or to $(i,j+1)$ if $j \lt N$.

There are exactly $N$ blocks in the grid, such that each row contains exactly one block and each column contains exactly one block. You can't move to a cell which contains a block. It is guaranteed that blocks will not placed in $(1,1)$ and $(N,N)$.

You have to find out whether you can reach $(N,N)$.

**Input**

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains $N$ - the size of the square grid.
- The $i$-th line of the next $N$ lines contains two integers $X_i$ and $Y_i$ indicating that $(X_i, Y_i)$ is the position of a block in the grid.

**Output**

For each test case, if there exists a path from $(1,1)$ to $(N,N)$, output `YES`, otherwise output `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes` and `YES` will all be treated as identical).

## Constraints

- $1 \le T \le 1000$
- $2 \le N \le 10^6$
- $1 \le X_i,Y_i \le N$
- $(X_i, Y_i) \ne (1, 1)$ and $(X_i, Y_i) \ne (N, N)$ for all $1 \le i \le N$
- $X_i \ne X_j$ and $Y_i \ne Y_j$ for all $1 \le i \lt j \le N$
- Sum of $N$ over all test cases does not exceed $10^6$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
2
3
1 2
2 3
3 1
2
1 2
2 1
```

**Sample output**

```
YES
NO
```

<details><summary>Explanation</summary>

- **Test case $1$:** We can follow the path $(1,1) \to (2,1) \to (2,2) \to (3,2) \to (3,3)$.

<img src="https://i.ibb.co/kgJhzGb/explanation.pngg" width="450" height="378" />

- **Test case $2$:** We can't move from the starting point, so it is impossible to reach $(N, N)$.

</details>

## Approach

A monotone path from the top-left to the bottom-right corner is impossible exactly when a chain of blocked cells, connected through edges or corners, links the "upper-right" boundary (the top row or the right column) with the "lower-left" boundary (the bottom row or the left column) - such a chain is a wall between the two corners.

There is exactly one block in every row and in every column, so two blocks can only touch diagonally, and only if they are in consecutive rows with columns that differ by one. The chains are therefore maximal runs of consecutive rows in which the block column changes by exactly $\pm 1$ from row to row.

Scan the rows in order. Start a new chain whenever the column jumps by anything other than 1. A chain touches the upper-right boundary if it contains row 1 or column $N$, and the lower-left boundary if it contains row $N$ or column 1. If some chain touches both, print NO; otherwise YES.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        block_col = [0] * n
        for _ in range(n):
            x = next(tokens) - 1
            y = next(tokens)
            block_col[x] = y
        ok = True
        upper = lower = False
        for i, col in enumerate(block_col):
            if i == 0 or abs(col - block_col[i - 1]) != 1:
                upper = lower = False
            upper = upper or i == 0 or col == n
            lower = lower or i == n - 1 or col == 1
            if upper and lower:
                ok = False
        out.append('YES' if ok else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

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

---

Same problem grouped by topic: [../docs/arrays/RECHEND.md](../docs/arrays/RECHEND.md)
