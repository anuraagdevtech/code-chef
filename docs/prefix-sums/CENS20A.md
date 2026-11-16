[&larr; 668. Increase 2 consecutive characters](CCD.md) &middot; [Index](../../README.md) &middot; [691. Sum of Cube  &rarr;](SUMOFCUBE.md)

# 670. Cherry and Bits

> CodeChef problem code [`CENS20A`](https://www.codechef.com/problems/CENS20A) &middot; difficulty **2179** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Two-dimensional xor difference array |
| **Time** | $O(N \cdot M + Q)$ |
| **Space** | $O(N \cdot M)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Cherry has a binary matrix $A$ consisting of $N$ rows and $M$ columns. The rows are numbered from $1$ to $N$, columns are numbered from $1$ to $M$. Element at row $i$ ($1$ ≤ $i$ ≤ $N$) and column $j$ ($1$ ≤ $j$ ≤ $M$) is denoted as $A_{ij}$. All elements of $A$ are either $0$ or $1$.

He performs $Q$ queries on matrix. Each query is provided by four integers $x_{1}$, $y_{1}$, $x_{2}$, $y_{2}$ which define the rectangle, where ($x_{1}$, $y_{1}$) stands for the coordinates of the top left cell of the rectangle, while ($x_{2}$, $y_{2}$) stands for the coordinates of the bottom right cell. You need to flip all the bits i.e. ($0$ to $1$, $1$ to $0$) that are located fully inside the query rectangle.

Finally, print the matrix after performing all the queries.

Note: $x_{1}$ represents the row number while $y_{1}$ represents the column number.

**Input:**
- The first line of the input contains two integers $N$ and $M$ — the number of rows and the number of columns in the matrix.
- Each of the next $N$ lines contains a string of length $M$, where the $j^{th}$ character of $i^{th}$ line denotes the value of $A_{i,j}$.
- Next line contains an integer $Q$ — the number of queries.
- Then follow $Q$ lines with queries descriptions. Each of them contains four space-seperated integers $x_{1}$, $y_{1}$, $x_{2}$, $y_{2}$ — coordinates of the up left and bottom right cells of the query rectangle.

**Output:**
Print the matrix, in the form of $N$ strings, after performing all the queries.

**Constraints**
- $1 \leq N,M \leq 1000$
- $0 \leq  A_{ij}  \leq 1$
- $1 \leq Q \leq 10^6$
- $1 \leq x_{1} \leq x_{2} \leq N$
- $1 \leq y_{1} \leq y_{2} \leq M$

## Constraints

- $1 \leq N,M \leq 1000$
- $0 \leq  A_{ij}  \leq 1$
- $1 \leq Q \leq 10^6$
- $1 \leq x_{1} \leq x_{2} \leq N$
- $1 \leq y_{1} \leq y_{2} \leq M$

## Sample

**Sample input**

```
2 2
00
00
3
1 1 1 1
2 2 2 2
1 1 2 2
```

**Sample output**

```
01
10
```

<details><summary>Explanation</summary>

**Example case 1:**

After processing the 1st query **1 1 1 1**, matrix becomes:
$$\begin{bmatrix} 10 \\ 00  \end{bmatrix}$$
After processing the 2nd query **2 2 2 2**, the matrix becomes:
$$\begin{bmatrix} 10 \\ 01  \end{bmatrix}$$
After processing the 3rd query **1 1 2 2**, matrix becomes:
$$\begin{bmatrix} 01 \\ 10  \end{bmatrix}$$
We need to output the matrix after processing all queries.

</details>

## Approach

A query flips every bit of a rectangle, and flips compose by xor, so a cell ends up flipped exactly when an odd number of rectangles cover it. The order of the queries is irrelevant.

Use a 2D difference array over GF(2): for a rectangle with corners $(x_1, y_1)$ and $(x_2, y_2)$ toggle the four cells $(x_1, y_1)$, $(x_1, y_2 + 1)$, $(x_2 + 1, y_1)$ and $(x_2 + 1, y_2 + 1)$. The 2D prefix xor of this array is then 1 exactly on the cells covered an odd number of times.

After all queries, compute the prefix xor row by row (a running xor along the row combined with the finished row above) and xor it with the original matrix.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    grid = [next(tokens) for _ in range(n)]
    diff = [bytearray(m + 1) for _ in range(n + 1)]
    for _ in range(int(next(tokens))):
        x = int(next(tokens)) - 1
        y = int(next(tokens)) - 1
        u = int(next(tokens))
        v = int(next(tokens))
        diff[x][y] ^= 1
        diff[x][v] ^= 1
        diff[u][y] ^= 1
        diff[u][v] ^= 1
    out = []
    for i in range(n):
        run = 0
        row = diff[i]
        above = diff[i - 1] if i else bytearray(m + 1)
        line = []
        for j in range(m):
            run ^= row[j]
            row[j] = run ^ above[j]
            line.append(str(grid[i][j] - 48 ^ row[j]))
        out.append(''.join(line))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \cdot M + Q)$
- **Space:** $O(N \cdot M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A cell flipped twice returns to its original value.
- The difference array needs one extra row and column for the far corners.
- Rows are given as strings without separators and must be printed the same way.
- With up to $10^6$ queries, each must cost $O(1)$.

## Dry run

`2 x 2` zero matrix, queries `(1,1)-(1,1)`, `(2,2)-(2,2)`, `(1,1)-(2,2)`.

Coverage counts per cell: `2 1 / 1 2`. Odd coverage is on the anti-diagonal, so those cells are flipped.

Output `01` / `10`.

> CodeChef tags: `Data Structures`, `Arrays`

---

Same problem in rating order (#630 of 735): [../../by-rating/630-CENS20A.md](../../by-rating/630-CENS20A.md)
