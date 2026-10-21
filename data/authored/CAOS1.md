---
topic: Arrays
subtopic: Contiguous runs in four directions
time: $O(R \cdot C)$ per test case
space: $O(R \cdot C)$
---
A cell is a *centre of Prime-Cross* when some prime $P$ satisfies $P \leq \min(L, R, T, B)$. Since the **smallest prime is $2$**, such a $P$ exists exactly when

$$\min(L, R, T, B) \geq 2$$

That reduction is the whole trick — no primality testing is needed, and the word "prime" in the statement is a misdirection.

So compute, for every cell, how many contiguous `^` lie immediately to its left, right, above and below (not counting the cell itself), and count the cells whose smallest of the four reaches $2$.

All four tables come from running prefix scans, each in $O(RC)$:

- sweeping each row left to right gives $L$;
- right to left gives $R$;
- each column top to bottom gives $T$;
- bottom to top gives $B$.

In each case the recurrence is "previous run $+ 1$ if the neighbour is `^`, else $0$". Computing the runs by walking outward from every cell instead would be $O(RC \cdot \max(R,C))$ — fine at $50 \times 50$, but the prefix version is the habit worth keeping.

Sample case 1 is instructive: in a $5\times5$ grid only the very centre has room for two cells on every side, and the single `#` at row $2$ sits in its row, cutting $R$ to $1$. So the answer is $0$ despite the grid being almost entirely open.

Wall cells are never centres, and their run values are $0$ by construction, so no separate guard is needed beyond skipping them.

## Edge cases

- **"Some prime $P \leq \min$" is just $\min \geq 2$**, because $2$ is the smallest prime — so no primality testing is needed at all.
- **The cell itself is excluded from every arm**, as the statement's note insists; the recurrence encodes that by reading the *neighbour's* arm and adding one only when that neighbour is open.
- **A wall truncates the arm to zero at that point**, which is what the reset in the recurrence does — and it is why the first sample answers $0$: the lone `#` leaves the centre cell with a right-arm of only $1$.
- **A cell within one step of any border fails on that arm**, so the outer two rings of the grid never contribute and need no special-casing.
- **The cell must itself be open**; a wall is never a monster's home however long its arms would be.
- **Four separate passes** build the arms — two row sweeps in opposite directions and two column sweeps — because each direction needs the neighbour already computed.
- **$R, C \leq 50$** with $T \leq 100$, so the five grids per case are cheap.

## Dry run

First sample: a $5 \times 5$ grid of `^` with a single `#` at row $3$, column $5$.

Only the centre cell $(3,3)$ is far enough from every border to have a chance:

| direction | contiguous `^` (excluding the cell) |
|---|---:|
| left | 2 |
| right | 1 — blocked by the `#` at column $5$ |
| top | 2 |
| bottom | 2 |

$\min = 1 < 2$, so it is not a CPC and the answer is `0`.
