---
topic: Arrays
subtopic: Case analysis on the nearest reachable one
time: $O(NM)$ per test case
space: $O(N + M)$
---
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
