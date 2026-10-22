# 386. OR Matrix

> [`ORMATRIX`](https://www.codechef.com/problems/ORMATRIX) &middot; difficulty **1656** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Case analysis on the nearest reachable one |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Mathematics`, `Bit Manipulation`, `Algorithms`, `2D Arrays`, `Bitwise Operation`, `Observation`, `Implementation` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(NM)$ per test case |
| **Space** | $O(N + M)$ |

## Question

You are given a matrix of integers $A$ with $N$ rows (numbered $1$ through $N$) and $M$ columns (numbered $1$ through $M$). Each element of this matrix is either $0$ or $1$.

A *move* consists of the following steps:
- Choose two different rows $r_1$ and $r_2$ or two different columns $c_1$ and $c_2$.
- Apply the bitwise OR operation with the second row/column on the first row/column. Formally, if you chose two rows, this means you should change $A_{r_1, k}$ to $A_{r_1, k} \lor A_{r_2, k}$ for each $1 \le k \le M$; if you chose two columns, then you should change $A_{k, c_1}$ to $A_{k, c_1} \lor A_{k, c_2}$ for each $1 \le k \le N$.

For each element of the matrix, compute the minimum number of moves required to make it equal to $1$ or determine that it is impossible. Note that these answers are independent, i.e. we are starting with the initial matrix for each of them.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains $M$ integers $A_{i, 1}, A_{i, 2}, \dots, A_{i, M}$ NOT separated by spaces.

**Output**
For each test case, print $N$ lines. For each valid $i$, the $i$-th of these lines should contain $M$ space-separated integers; for each valid $j$, the $j$-th of these integers should be the minimum number of moves required to make $A_{i, j}$ equal to $1$, or $-1$ if it is impossible.

**Constraints**
- $1 \le T \le 100$
- $1 \le N, M \le 1,000$
- $A_{i, j} \in \{0, 1\}$ for each valid $i, j$
- the sum of $N \cdot M$ for all test cases does not exceed $1,000,000$

## Constraints

- $1 \le T \le 100$
- $1 \le N, M \le 1,000$
- $A_{i, j} \in \{0, 1\}$ for each valid $i, j$
- the sum of $N \cdot M$ for all test cases does not exceed $1,000,000$

## Sample

**Sample input**

```
1
3 3
010
000
001
```

**Sample output**

```
1 0 1
2 1 1
1 1 0
```

## Approach

OR never clears a bit, so a $1$ anywhere can be propagated but never destroyed. Three cases cover every cell, and the answer is never more than $2$.

- **$A_{i,j} = 1$:** zero moves.
- **Row $i$ or column $j$ contains a $1$:** one move. If some $A_{i,c} = 1$, OR column $c$ into column $j$; if some $A_{r,j} = 1$, OR row $r$ into row $i$.
- **Otherwise:** the row and the column are entirely zero, so no single move can help — one move only ORs in another full row or column, and to reach cell $(i,j)$ it must come from row $i$'s or column $j$'s own entries. Two moves always suffice: pick any $A_{r,c} = 1$ (necessarily $r \neq i$ and $c \neq j$), OR row $r$ into row $i$ to plant a $1$ at $(i,c)$, then OR column $c$ into column $j$.

The only impossible case is an **all-zero matrix**, where every answer is $-1$.

So the whole computation is two boolean arrays: does row $i$ contain a $1$, and does column $j$. Each cell is then an $O(1)$ lookup, giving $O(NM)$ overall with $O(N+M)$ extra space rather than any per-cell search.

The sample makes all three cases visible. In
```
010
000
001
```
cell $(1,1)$ sits in a row that has a $1$, so one move. Cell $(2,2)$ has an empty row but column $2$ holds the $1$ from row $1$, so again one. And cell $(2,1)$ has both its row and its column empty, so it needs the two-step route through $(1,2)$ or $(3,3)$.

Note the input rows are digit strings with no separators, so each line is one token to be indexed character by character.

## Solution

```python
import sys

ONE = 0x31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        rows = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        row_has = [ONE in r for r in rows]
        col_has = [False] * m
        for r in rows:
            for j in range(m):
                if r[j] == ONE:
                    col_has[j] = True
        if not any(row_has):
            line = " ".join(["-1"] * m)
            out.extend([line] * n)
            continue
        for i in range(n):
            r = rows[i]
            # 0 if already one, 1 if the row or column has one, else 2.
            out.append(" ".join(
                "0" if r[j] == ONE else ("1" if row_has[i] or col_has[j] else "2")
                for j in range(m)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Four cases, in order of cost.** A cell already holding $1$ needs no move; a cell whose own row or column contains a $1$ needs one move; otherwise two moves bring a $1$ into the row and then into the cell; and an all-zero matrix is impossible.
- **An all-zero matrix never changes**, since OR-ing zeros gives zeros — so every cell answers $-1$, and the whole output is a block of $-1$s.
- **The two-move case is the interesting one.** With a $1$ somewhere else entirely, one move brings it into the cell's row (or column) and a second brings it into the cell — and no single move can do both.
- **One move suffices even when the $1$ is far along the row**, because the move ORs the entire row at once rather than shifting a single bit.
- **Row and column presence must both be checked**, as the second sample row shows: its cells are $2$, $1$, $1$ depending only on whether their *column* holds a $1$.
- **The moves are never actually performed** — the answer is a closed-form case analysis, so no simulation is needed.
- **Sum of $N \cdot M \leq 10^6$**, so the two presence arrays are built in one pass and the output is joined per row.

## Dry run

Sample: a $3 \times 3$ matrix with $1$s at $(1,2)$ and $(3,3)$.

| | row has a 1? |
|---|:---:|
| row 1 | yes |
| row 2 | **no** |
| row 3 | yes |

| | col 1 | col 2 | col 3 |
|---|:---:|:---:|:---:|
| column has a 1? | no | yes | yes |

| cell | reasoning | answer |
|---|---|---:|
| $(2,1)$ | neither row 2 nor column 1 has a $1$ | 2 |
| $(2,2)$ | column 2 has one | 1 |
| $(1,2)$ | already a $1$ | 0 |

---

Same problem grouped by topic: [../docs/arrays/ORMATRIX.md](../docs/arrays/ORMATRIX.md)
