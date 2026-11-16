[&larr; 569. Churu and Balls](CBALLS.md) &middot; [Index](../../README.md) &middot; [597. Kirito in labyrinth &rarr;](KIRLAB.md)

# 572. Destroy Cells

> CodeChef problem code [`DESTCELL`](https://www.codechef.com/problems/DESTCELL) &middot; difficulty **2297** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Enumerate periodic row-major positions and test column-major divisibility |
| **Time** | $O(S\log S)$ per test case for $S=NM$ |
| **Space** | $O(S)$ for the output |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Anas is playing an amazing game on a grid with $N$ rows and $M$ columns. The rows are numbered $1$ through $N$ from top to bottom and the columns are numbered $1$ through $M$ from left to right.

Anas wants to destroy this grid. To do that, he wants to send two heroes from the top left cell to the bottom right cell:
- The first hero visits cells in row-major order: $(1,1) \rightarrow (1,2) \rightarrow \ldots \rightarrow (1,M) \rightarrow (2,1) \rightarrow (2,2) \rightarrow \ldots \rightarrow (2,M) \rightarrow \ldots \rightarrow (N,M)$.
- The second hero visits cells in column-major order: $(1,1) \rightarrow (2,1) \rightarrow \ldots \rightarrow (N,1) \rightarrow (1,2) \rightarrow (2,2) \rightarrow \ldots \rightarrow (N,2) \rightarrow \ldots \rightarrow (N,M)$.

We know that each hero destroys the first cell he visits, rests in the next $K$ cells he visits without destroying them, then destroys the next cell he visits, rests in the next $K$ cells, destroys the next cell, and so on until he reaches (and rests in or destroys) the last cell he visits.

Anas does not know the value of $K$. Therefore, for each value of $K$ between $0$ and $N \cdot M - 1$ inclusive, he wants to calculate the number of cells that will be destroyed by at least one hero. Can you help him?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $M$.

**Output**
For each test case, print a single line containing $N \cdot M$ space-separated integers as described above.

**Constraints**
- $1 \le T \le 100$
- $2 \le N, M \le 1,000$
- the sum of $N \cdot M$ over all test cases does not exceed $2 \cdot 10^6$

**Subtasks**
**Subtask #1 (30 points):**
- $2 \le N, M \le 50$
- the sum of $N \cdot M$ over all test cases does not exceed $5,000$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $2 \le N, M \le 1,000$
- the sum of $N \cdot M$ over all test cases does not exceed $2 \cdot 10^6$

## Sample

**Sample input**

```
1
2 3
```

**Sample output**

```
6 4 3 3 2 1
```

<details><summary>Explanation</summary>

**Example case 1:**
- $K = 0$: All cells will be destroyed by the heroes.
- $K = 1$: The first hero will destroy the cells $[(1,1), (1,3), (2,2)]$, while the second one will destroy the cells $[(1,1), (1,2), (1,3)]$.
- $K = 2$: The first hero will destroy the cells $[(1,1), (2,1)]$, while the second one will destroy the cells $[(1,1), (2,2)]$.
- $K = 3$: The first hero will destroy the cells $[(1,1), (2,2)]$, while the second one will destroy the cells $[(1,1), (1,3)]$.
- $K = 4$: The first hero will destroy the cells $[(1,1), (2,3)]$ and the second one will also destroy the cells $[(1,1), (2,3)]$.
- $K = 5$ : The first hero will destroy the cell $(1,1)$ and the second one will also destroy the cell $(1,1)$.

</details>

## Approach

For step $d=K+1$, each hero destroys indices $0,d,2d,\ldots$ in its own ordering, giving $\lfloor(S-1)/d\rfloor+1$ destroyed cells. Use inclusion-exclusion to subtract their overlap.

For each row-major destroyed index $x$, its row and column are `divmod(x,M)`, so its column-major index is `column*N+row`. The second hero destroys it exactly when that index is divisible by $d$. Enumerating only the first hero's destroyed indices costs $\sum_{d=1}^S O(S/d)=O(S\log S)$ across all answers.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        size = n*m
        answer = []
        for step in range(1,size+1):
            each = (size-1)//step+1
            overlap = 0
            for index in range(0,size,step):
                row,col = divmod(index,m)
                overlap += (col*n+row)%step == 0
            answer.append(2*each-overlap)
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(S\log S)$ per test case for $S=NM$
- **Space:** $O(S)$ for the output
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Both heroes always destroy the top-left cell.
- $K=0$ destroys the whole grid.
- $K=S-1$ destroys only the first cell.
- A cell destroyed twice counts once.

## Dry run

For a two-by-three grid and `K=1`, step two gives three destroyed cells per hero. Their overlap has two cells, so the union size is `3+3-2=4`.

---

Same problem in rating order (#660 of 735): [../../by-rating/660-DESTCELL.md](../../by-rating/660-DESTCELL.md)
