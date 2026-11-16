[&larr; 626. Subarray Removal](REMSUBARR.md) &middot; [Index](../../README.md) &middot; [650. Can You Reach The End &rarr;](RECHEND.md)

# 636. Consecutive Adding

> CodeChef problem code [`CONSADD`](https://www.codechef.com/problems/CONSADD) &middot; difficulty **2038** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Greedy elimination with window operations, rows first and then the last columns |
| **Time** | $O(R \cdot C)$ per test case |
| **Space** | $O(R \cdot C)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given two matrices $A$ and $B$, each with $R$ rows (numbered $1$ through $R$) and $C$ columns (numbered $1$ through $C$). Let's denote an element of $A$ or $B$ in row $i$ and column $j$ by $A_{i,j}$ or $B_{i,j}$ respectively.

You are also given an integer $X$. You may perform the following operation on $A$ any number of times:
- Choose an integer $v$.
- Choose $X$ consecutive elements of $A$, either in the same row or in the same column.
- Add $v$ to each of the chosen elements of $A$.

Determine whether it is possible to change $A$ to $B$ in a finite number of operations.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $R$, $C$ and $X$.
- $R$ lines follow. For each valid $i$, the $i$-th of these lines contains $C$ space-separated integers $A_{i,1}, A_{i,2}, \ldots, A_{i,C}$.
- $R$ more lines follow. For each valid $i$, the $i$-th of these lines contains $C$ space-separated integers $B_{i,1}, B_{i,2}, \ldots, B_{i,C}$.

**Output**
For each test case, print a single line containing the string `"Yes"` if there is a sequence of operations that changes the matrix $A$ to $B$, or `"No"` if such a sequence of operations does not exist.

**Constraints**
- $1 \leq T \leq 10^3$
- $2 \leq R,C \leq 10^3$
- $2 \leq X \leq \min(R,C)$
- $|A_{i,j}|, |B_{i,j}| \leq 10^9$ for each valid $i,j$
- the sum of $R$ over all test cases does not exceed $10^3$
- the sum of $C$ over all test cases does not exceed $10^3$

**Subtasks**
**Subtask #1 (5 points):** $X=2$

**Subtask #2 (10 points):** $X=3$

**Subtask #3 (85 points):** original constraints

## Constraints

- $1 \leq T \leq 10^3$
- $2 \leq R,C \leq 10^3$
- $2 \leq X \leq \min(R,C)$
- $|A_{i,j}|, |B_{i,j}| \leq 10^9$ for each valid $i,j$
- the sum of $R$ over all test cases does not exceed $10^3$
- the sum of $C$ over all test cases does not exceed $10^3$

## Sample

**Sample input**

```
3
2 2 2
1 2
0 1
0 0
0 0
2 2 2
1 2
0 1
0 0
-1 0
3 2 2
1 1
2 2
3 3
1 0
2 0
3 0
```

**Sample output**

```
Yes
No
No
```

<details><summary>Explanation</summary>

**Example case 1:** We can add $-1$ to both elements in row $1$ and add $-1$ to both elements in column $2$.

**Example case 2:** After any operation, the sum of elements of $A$ remains even. However, the sum of elements of $B$ is odd, so $A$ cannot be changed to $B$.

</details>

## Approach

Work with the difference $D = A - B$; the goal is to make it all zero.

Sweep each row from left to right. The leftmost non-zero cell of a row can only be fixed (as far as row operations go) by the window that starts there, so apply that window with the right value whenever it fits. A difference array carries the effect of the windows already applied. Afterwards every row is zero except possibly in its last $X - 1$ columns, where no window can start.

Now do the same down each of those last $X - 1$ columns with vertical windows: the topmost non-zero cell is cancelled by the window starting there. What may remain are cells in the last $X - 1$ rows of the last $X - 1$ columns; if any of them is non-zero the answer is No.

Vertical windows in the earlier columns need not be considered: modulo row operations, a unit in column $j$ is an integer combination of units in the last $X - 1$ columns of the same row, so such a window is already a combination of the operations used.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        rows = next(tokens)
        cols = next(tokens)
        width = next(tokens)
        delta = [[next(tokens) for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                delta[i][j] -= next(tokens)
        for row in delta:
            diff = [0] * (cols + 1)
            applied = 0
            for j in range(cols):
                applied += diff[j]
                v = row[j] + applied
                if j + width <= cols:
                    applied -= v
                    diff[j + width] += v
                    row[j] = 0
                else:
                    row[j] = v
        ok = True
        for j in range(cols - width + 1, cols):
            diff = [0] * (rows + 1)
            applied = 0
            for i in range(rows):
                applied += diff[i]
                v = delta[i][j] + applied
                if i + width <= rows:
                    applied -= v
                    diff[i + width] += v
                elif v:
                    ok = False
        out.append('YES' if ok else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(R \cdot C)$ per test case
- **Space:** $O(R \cdot C)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $X = 1$: every single cell can be adjusted and the answer is always Yes.
- $X$ larger than both dimensions: no operation exists, so $A$ must already equal $B$.
- $X$ larger than the row length but not the column length: only vertical windows exist; the row sweep then changes nothing.
- Values of $v$ may be negative and unbounded, so only the linear structure matters.

## Dry run

Sample 1: $A = \begin{pmatrix}1 & 2\\ 0 & 1\end{pmatrix}$, $B = 0$, $X = 2$, so $D = A$.

Rows: in row 1 the window at column 1 cancels the 1 and turns the row into `0 1`; row 2 is already `0 1`.

Last column: the vertical window at the top cancels the 1 in row 1 and, with it, the 1 in row 2. Nothing is left, so the answer is Yes.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#585 of 735): [../../by-rating/585-CONSADD.md](../../by-rating/585-CONSADD.md)
