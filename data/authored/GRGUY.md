---
topic: Dynamic Programming
subtopic: Two-state DP with a zero-cost move
time: $O(n)$ per test case
space: $O(1)$
---
With only two lanes the state is tiny — (lane, column) — and the cost model is what makes it interesting: advancing within a lane is **free**, while the two gravity-switching moves cost $1$. Minimising switches is therefore a shortest path on a graph with $0$- and $1$-weight edges.

Because every move either advances the column or stays in it, a left-to-right DP over columns is a valid order. Let $f[\ell][x]$ be the fewest switches to stand on lane $\ell$, column $x$. At each column, in order:

1. **Settle the free-standing switch:** $f[1-\ell][x] \leftarrow f[\ell][x] + 1$ if that cell is clean. Doing this once in each direction is enough — switching twice in the same column only wastes two moves.
2. **Push forward:** to $(\ell, x{+}1)$ at no cost and to $(1-\ell, x{+}1)$ at cost $1$, in each case only onto a clean block.

Chef may start on either lane and finish on either, so initialise both lanes at column $1$ (whichever are clean) and answer with the minimum over both lanes at column $n$. Unreachable means `No`.

Only two values per column are ever live, so the sweep runs in constant space — worth having with $|L|$ up to $2 \times 10^5$ and $T$ up to $10^5$.

The samples show the range. In `#...#` / `.###.` the blocked ends force a start on lane 2 and a finish on lane 2, with a crossing out and back: $2$ switches. The alternating `#.#.#.` / `.#.#.#` leaves no choice at all — every step must change lane, giving $5$. And two identical lanes starting with `#` block both entrances, so the answer is `No` before any move is considered.
