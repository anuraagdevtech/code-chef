[&larr; 600. Equivalent Numbers](600-EQUIVALENT.md) &middot; [Index](README.md) &middot; [602. Segment Three &rarr;](602-SEGTHREE.md)

# 601. Chef and Rectangle Array

> [`CHSQARR`](https://www.codechef.com/problems/CHSQARR) &middot; difficulty **2088** &middot; time limit **5.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | 2D sliding-window maximum with monotone deques plus 2D prefix sums |
| **Complexity class** | Cubic or higher polynomial $O(n^3)$ and above |
| **Time** | $O(Q \cdot N \cdot M)$, with repeated query sizes answered from a cache |
| **Space** | $O(N \cdot M)$ |

## Question

Chef has a two-dimensional matrix **A** of dimensions **N** × **M**, (**N** rows and **M** columns).

He calls the matrix **A** beautiful if there exist an **a**×**b** submatrix, such that all of its elements are equal. In one minute Chef can increase one element of the matrix **A** by 1. Now he asks you to find out minimum time he will need to make the matrix **A** beautiful?

Please note that sub-matrix of a matrix is a **continuous** rectangular block of the matrix. It can be denoted by two pair of indices **(x_1, y_1)** and **(x_2, y_2)** where **x_1 ≤ x_2**, **y_1 ≤ y_2**. The content of the submatrix will be all the cells **(i, j)** such that **x_1 ≤ i ≤ x_2** and **y_1 ≤ j ≤ y_2**.

**Input**

- There is a single test case.

- The first line contains two space-separated integers **N**, **M** denoting the number of rows and columns in the matrix **A**, respectively

- Each of the next **N** lines, contains **M** space-separated integers denoting the **i**-th row of the array

- Next line contains one integer **Q** - amount of questions

- Each of next **Q** lines contains two space-separated integers **a** and **b** denoting sizes of submatrix sought.

- All questions are independent and do not influence each other. It means when you answer question, you don't need to change the array

**Output**

- For each question, output a single line containing the minimum time that Chef needs to make an matrix **A** beautiful (for parameters **a** and **b** from question)

**Constraints**

- **1** ≤ **Q** ≤ **50**

- **1** ≤ **N**, **M**, **A_i, j** ≤ **1000**

- **1** ≤ **a** ≤ **N**

- **1** ≤ **b** ≤ **M**

**Subtasks**

**Subtask #1 (13 pts)**

- **1** ≤ **N**, **M** ≤ **50**

- TL = 1s

**Subtask #2 (35 pts)**

- **1** ≤ **N**, **M** ≤ **200**

- TL = 2s

**Subtask #3 (52 pts)**

- Original constraints

- TL = 4s

## Constraints

- 1 ≤ Q ≤ 50
- 1 ≤ N, M, A_i, j ≤ 1000
- 1 ≤ a ≤ N
- 1 ≤ b ≤ M

## Sample

**Sample input**

```
3 4
1 8 3 4
5 2 3 1
3 6 2 2
4
1 1
2 2
2 3
3 2
```

**Sample output**

```
0
4
15
9
```

<details><summary>Explanation</summary>

**Question #1:**
Chef can choose any 1 × 1 submatrix and it will take his 0 minutes to make it beautiful.

**Question #2:**
The best variant is submatrix

```
3 1
2 2
```

**Question #3:**
The next submatrix Chef can make equal in 15 minutes

```
5 2 3
3 6 2
```

**Question #4:**

```
3 4
3 1
2 2
```

</details>

## Approach

Elements can only be increased, so the cheapest way to equalise an $a \times b$ block is to raise everything to the block maximum. Its cost is $a \cdot b \cdot \max - \text{sum}$, and the answer to a query is the minimum of that over all positions of the block.

The block sum comes from a 2D prefix-sum table in $O(1)$. The block maximum is computed in two passes of the monotone-deque sliding-window maximum: first along every row with window width $b$, then down every column of those row maxima with window height $a$. Each pass is linear in the size of the matrix, so one query costs $O(N \cdot M)$. Queries with the same dimensions are answered from a dictionary.

## Solution

```python
import sys
from collections import deque


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = (next(tokens), next(tokens))
    grid = [[next(tokens) for _ in range(m)] for _ in range(n)]
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        total = 0
        for j in range(m):
            total += grid[i][j]
            prefix[i + 1][j + 1] = prefix[i][j + 1] + total
    out = []
    cache = {}
    for _ in range(next(tokens)):
        height, width = (next(tokens), next(tokens))
        if (height, width) not in cache:
            horizontal = []
            for row in grid:
                window = deque()
                row_maxima = []
                for j, x in enumerate(row):
                    while window and row[window[-1]] <= x:
                        window.pop()
                    window.append(j)
                    while window[0] <= j - width:
                        window.popleft()
                    if j >= width - 1:
                        row_maxima.append(row[window[0]])
                horizontal.append(row_maxima)
            best = 10 ** 30
            for j in range(m - width + 1):
                window = deque()
                for i in range(n):
                    x = horizontal[i][j]
                    while window and horizontal[window[-1]][j] <= x:
                        window.pop()
                    window.append(i)
                    while window[0] <= i - height:
                        window.popleft()
                    if i >= height - 1:
                        top = i - height + 1
                        total = prefix[i + 1][j + width] - prefix[top][j + width] - prefix[i + 1][j] + prefix[top][j]
                        best = min(best, height * width * horizontal[window[0]][j] - total)
            cache[height, width] = best
        out.append(str(cache[height, width]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- A $1 \times 1$ query always costs 0.
- The block may be the whole matrix; then there is a single position.
- The deque comparison uses `<=` so equal values keep only the most recent index, which is safe for a maximum.
- Costs can exceed 32 bits when the block is large and values are spread out.

## Dry run

Sample matrix `1 8 3 4 / 5 2 3 1 / 3 6 2 2`, query `2 2`.

Row maxima for width 2: `8 8 4`, `5 3 3`, `6 6 2`. Column windows of height 2 over them give the block maxima `8 8 4` (rows 1-2) and `6 6 3` (rows 2-3).

The bottom-right block `3 1 / 2 2` has maximum 3 and sum 8, cost $4 \cdot 3 - 8 = 4$; every other block costs more. Answer 4.

---

Same problem grouped by topic: [../docs/arrays/CHSQARR.md](../docs/arrays/CHSQARR.md)
