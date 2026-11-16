[&larr; 686. One or All](686-ONEORALL.md) &middot; [Index](README.md) &middot; [688. GCD Queries &rarr;](688-GCD_QUERIES.md)

# 687. Smallest Difference

> [`SMALLESTDIFF`](https://www.codechef.com/problems/SMALLESTDIFF) &middot; difficulty **2421** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A tight window of sorted values for the path, with decoys beside it |
| **CodeChef tags** | `Algorithms`, `Constructive`, `Sorting`, `Observation` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N M \log (N M))$ per test case |
| **Space** | $O(N M)$ |

## Question

Consider a grid $A$ with dimensions $N \times M$, such that all elements of the grid are **distinct**.

A remote controlled car is present at cell $(1,1)$. Chef and Chefina will alternatively move the car with Chef starting first.

- If it is Chef's turn, he will move the car to either right or down by $1$ cell. He moves the car to the cell having **larger** element.
- If it is Chefina's turn, she will move the car to either right or down by $1$ cell. She moves the car to the cell having **smaller** element.

The car stops once it reaches the cell $(N, M)$.

Let us denote the largest element visited by the car by $A_{max}$ and the smallest element as $A_{min}$. Then, the score of the grid is defined as $A_{max} - A_{min}$.

Charlie has an array $B$ containing $N \cdot M$ **distinct** elements. He wants to arrange the elements as a grid of size $N\times M$ such that the score of the grid is **minimised**.

Help Charlie to construct **any such** grid.

Note: **Please use fast I/O for input and pypy for python submissions.**

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — dimensions of the grid $A$.
    - The next line contains $N \cdot M$ distinct elements denoting the array $B$.

**Output**

For each test case, output $N$ lines each containing $M$ spaced integers denoting the grid $A$.

If there are multiple possible answers, print **any** of them.

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N, M \leq 1000$
- $1 \leq B_i \leq 10^9$
- All elements of the array $B$ are distinct.
- Sum of $N \cdot M$ over all test cases do not exceed $10^6$.

## Sample

**Sample input**

```
2
2 2
5 10 20 40
3 2
2 6 4 1 9 20
```

**Sample output**

```
10 5 
20 40 
2 4 
1 6 
20 9
```

<details><summary>Explanation</summary>

**Test case $1$:** The car starts from $(1, 1)$. Let us consider the moves based on the grid $[[10, 5], [20, 40]]$.
- In Chef's turn, he will move the car to $(2, 1)$ since $A_{(2, 1)} \gt A_{(1, 2)}$.
- In Chefina's turn, she will move the car to $(2, 2)$ as it is the only available choice.

Thus, the car covers the elements $[10, 20, 40]$. The largest element in the path is $40$ while the smallest element is $10$. Thus, the score is $40-10 = 30$. It can be shown that this is the minimum possible score that can be achieved in any configuration of grid.

**Test case $2$:** The car starts from $(1, 1)$. Let us consider the moves based on the grid $[[2, 4], [1, 6], [20, 9]]$.
- In Chef's turn, he will move the car to $(1, 2)$ since $A_{(1, 2)} \gt A_{(2, 1)}$.
- In Chefina's turn, she will move the car to $(2, 2)$ as it is the only available choice.
- In Chef's turn, he will move the car to $(3, 2)$ as it is the only available choice.

Thus, the car covers the elements $[2, 4, 6, 9]$. The largest element in the path is $9$ while the smallest element is $2$. Thus, the score is $9 - 2 = 7$. It can be shown that this is the minimum possible score that can be achieved in any configuration of grid.

</details>

## Approach

The car visits exactly $L = N + M - 1$ cells, and the aim is to make the difference between the largest and the smallest visited value as small as possible. The best conceivable choice is a window of $L$ consecutive values in sorted order - but the grid has to force the car along the cells holding them.

Assume $N \le M$ (otherwise build the transposed grid). Lay the window down the first column and then along the last row. While the car is in the first column, at row $i$ the mover chooses between the cell below (on the path) and the cell to the right (a decoy). Chef moves on even steps and takes the larger value, so the decoy must be smaller than the path cell; Chefina moves on odd steps and takes the smaller, so the decoy must be larger. In the last row only moves to the right exist.

So $\lceil (N-1)/2 \rceil$ decoys must be smaller than the whole window and $\lfloor (N-1)/2 \rfloor$ larger. Among all windows of $L$ consecutive sorted values that leave enough smaller values before them and enough larger values after them, take the one with the smallest spread. Place the window on the path, the decoys in the second column, and fill the other cells with the remaining values in any order.

At least $\min(N, M) - 1$ decisions are made before the car first touches the far boundary, each needing a rejected neighbour on the appropriate side, which is why no arrangement can do better than such a window.

## Solution

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    values = sorted((next(tokens) for _ in range(n * m)))
    transpose = n > m
    if transpose:
        n, m = (m, n)
    length = n + m - 1
    need_small = n // 2
    need_large = (n - 1) // 2
    start = min(range(need_small, len(values) - length - need_large + 1), key=lambda j: values[j + length - 1] - values[j])
    path = values[start:start + length]
    small = values[:start]
    large = values[start + length:]
    grid = [[0] * m for _ in range(n)]
    cursor = 0
    for i in range(n):
        grid[i][0] = path[cursor]
        cursor += 1
    for j in range(1, m):
        grid[n - 1][j] = path[cursor]
        cursor += 1
    for i in range(n - 1):
        grid[i][1] = small.pop() if i % 2 == 0 else large.pop()
    rest = iter(small + large)
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                grid[i][j] = next(rest)
    if transpose:
        grid = [list(row) for row in zip(*grid)]
    return '\n'.join((' '.join(map(str, row)) for row in grid))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cursor = int(next(tokens))
    out = [solve(tokens) for _ in range(cursor)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- All values are distinct, so every decision is unambiguous.
- For $N > M$ the roles of rows and columns are swapped by transposing at the end.
- With $N = 2$ only one decoy, a smaller value, is needed.
- Several grids are optimal, so the output is validated by a checker.

## Dry run

`2 x 2` with values `5 10 20 40`. $L = 3$; one smaller decoy is needed and no larger one.

The only window leaving one value below it is `10 20 40`. Path: `10` at $(1,1)$, `20` at $(2,1)$, `40` at $(2,2)$. Decoy `5` at $(1,2)$.

Grid `10 5 / 20 40`: Chef moves down to 20 (larger than 5), Chefina then has only the move to 40. Spread $40 - 10 = 30$.

---

Same problem grouped by topic: [../docs/constructive/SMALLESTDIFF.md](../docs/constructive/SMALLESTDIFF.md)
