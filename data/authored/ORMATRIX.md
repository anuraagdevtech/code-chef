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
