[&larr; 587. Girl Friend and String Gift](CHGLSTGT.md) &middot; [Index](../../README.md) &middot; [589. Dessert Wizard &rarr;](DELISH.md)

# 588. Matrix

> CodeChef problem code [`MATRIX2`](https://www.codechef.com/problems/MATRIX2) &middot; difficulty **2209** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Largest upper-triangular square from the row run and the diagonal neighbour |
| **Time** | $O(N \cdot M)$ |
| **Space** | $O(M)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are given a matrix **A** that consists of **N** rows and **M** columns. Every number in the matrix is either zero or one. Calculate the number of such triples (**i**, **j**, **h**) where for all the pairs (**x**, **y**), where both **x** and **y** belong to [**1**; **h**] if **y >= x**, **A[i+x-1][j+y-1]** equals to one. Of course, the square (**i**, **j**, **i+h-1**, **j+h-1**) should be inside of this matrix. In other words, we're asking you to calculate the amount of square submatrices of a given matrix which have ones on and above their main diagonal.

**Input**

The first line of the input consists of two integers - **N** and **M**.

The following **N** lines describe the matrix. Each line consists of **M** characters that are either zero or one.

**Output**

Output should consist of a single integer - the answer to the problem.

**Example**

```
**Input:**
2 3
011
111

**Output:**
6
```

**Scoring**

Subtask 1 (9 points): 1 <= **N,M** <= 2000, All the numbers in the matrix are equal to one.

Subtask 2 (12 points): 1 <= **N,M** <= 10.

Subtask 3 (34 points): 1 <= **N,M** <= 30.

Subtask 4 (17 points): 1 <= **N,M** <= 150.

Subtask 5 (28 points): 1 <= **N,M** <= 2000.

## Constraints

- The statement publishes no numeric limits.
- One test case: an N x M matrix given as N strings of M characters, each 0 or 1.

## Approach

Let $f(i, j)$ be the largest $h$ for which the square with top-left corner $(i, j)$ has ones on and above its main diagonal. Every smaller $h$ works as well, so the answer is the sum of $f$ over all cells.

Such a square of size $h$ is its first row - $h$ consecutive ones starting at $(i, j)$ - together with an upper-triangular square of size $h-1$ whose corner is $(i+1, j+1)$. Hence

$$f(i, j) = \min(\text{run}(i, j),\; f(i+1, j+1) + 1),$$

where $\text{run}(i, j)$ is the number of consecutive ones to the right starting at $(i, j)$. Process rows from the bottom up and columns from right to left, keeping only the previous row of $f$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n, m = (int(next(tokens)), int(next(tokens)))
    grid = [next(tokens) for _ in range(n)]
    below = [0] * (m + 1)
    total = 0
    for row in reversed(grid):
        current = [0] * (m + 1)
        run = 0
        for j in range(m - 1, -1, -1):
            run = run + 1 if row[j] == 49 else 0
            current[j] = min(run, below[j + 1] + 1)
            total += current[j]
        below = current
    print(total)


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \cdot M)$
- **Space:** $O(M)$
- Auxiliary space excludes the buffered input and output.

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

---

Same problem in rating order (#640 of 735): [../../by-rating/640-MATRIX2.md](../../by-rating/640-MATRIX2.md)
