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

## Edge cases

- **Advancing is free and switching lanes costs one**, so the DP tracks the cheapest way to stand in each lane at each column — two states, rolled forward.
- **A switch within the same column must be allowed**, which is the second pair of updates: the guy can flip gravity and then advance, so arriving in one lane lets him reach the other at $+1$ in that same column. Without it the second sample is unsolvable.
- **One in-column switch each way is enough**, since switching twice returns to the start at a strictly higher cost.
- **Obstacles make a state unreachable**, marked `INF` — and `INF` must never be treated as $0$, or the path would tunnel through walls.
- **Both lanes blocked at the start** (the third sample, with `#` atop `#`) → `No` immediately, and the sentinel propagates it to the end.
- **The answer is the better of the two lanes at the last column**, since finishing in either is acceptable.
- **The output is two lines on success** — `Yes` then the count — and one line on failure.
- **Sum of lengths up to $2 \times 10^5$** with $T$ up to $10^5$, so the state is two scalars rather than arrays.

## Dry run

First sample: top `#...#`, bottom `.###.`

| column | top reachable at | bottom reachable at |
|---:|---|---|
| 0 | blocked | **0** |
| 1 | $0 + 1 = 1$ (switch) | blocked |
| 2 | 1 | blocked |
| 3 | 1 | blocked |
| 4 | blocked | $1 + 1 = $ **2** (switch) |

Output `Yes` then `2`: one switch down at column 1 and one back up at column 4.
