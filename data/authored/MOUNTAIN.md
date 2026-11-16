---
topic: Constructive
subtopic: Shortest block of top rows, then greedy top-up from the heaviest row
time: $O(N)$ per query
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A cell in row $i$ is worth $i$, so a mountain on rows $P \dots P+K-1$ with lengths $L_i$ has sum $\sum (P + i - 1) L_i$. Always start at $P = 1$: then row $i$ is worth $i$ per cell and the unit-valued first row makes every remainder payable.

Take the smallest $K$ whose full capacity $M \cdot K(K+1)/2$ reaches $S$; the constraint on $S$ guarantees $K \le N$. Give every row one cell, costing $K(K+1)/2$, which is at most $S$ because $K - 1$ full rows were not enough. The remaining amount has to be paid with "coins" of value $1, 2, \dots, K$, each available $M - 1$ times. Go from the largest row down and take as many extra cells as fit. The greedy never gets stuck: the smaller rows together can cover any remainder up to their full capacity, and by the choice of $K$ the remainder never exceeds it.

So a mountain always exists and $-1$ is never printed.

## Edge cases

- Each selected row needs at least one cell, which is why the base cost is taken first.
- $S = 1$: a single cell in row 1.
- $S$ equal to the full matrix sum uses all rows completely.
- Several mountains can have the same sum, so the output is validated by a checker.

## Dry run

`N = 5, M = 4, S = 20`.

Capacities: one row 4, two rows 12, three rows 24, so $K = 3$. Base cost $1 + 2 + 3 = 6$, leaving 14.

- row 3: $\min(3, \lfloor 14 / 3 \rfloor) = 3$ extra cells, leaving 5
- row 2: $\min(3, \lfloor 5 / 2 \rfloor) = 2$, leaving 1
- row 1: 1, leaving 0

Lengths `2 3 4`: $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 = 20$. Output `1 3` and `2 3 4`.
