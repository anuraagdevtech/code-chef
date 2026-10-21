---
topic: Game Theory
subtopic: Counting the forced number of moves
time: $O(N)$ per test case
space: $O(1)$
---
Every move deletes one `0` and one `1`, because the chosen pair must differ. So each move reduces both counts by exactly one, and the total number of moves is fixed no matter how either player plays.

The game ends when one character runs out, so the move count is

$$\min(c_0,\ c_1)$$

Crucially, a move is **always available while both characters remain**: a string containing both a `0` and a `1` must have them adjacent somewhere, since scanning from a `0` to a `1` has to cross a boundary. So play never stalls early.

With the move count forced, the winner is pure parity. Zlatan moves first, so he makes moves $1, 3, 5, \ldots$ and wins exactly when $\min(c_0, c_1)$ is **odd**; otherwise Ramos makes the last move and Zlatan is the one left unable to play.

"Both play optimally" turns out to be vacuous here — there are no choices that matter. Recognising that a game is *move-count-determined* is the whole insight, and it saves any search over strategies.

The samples sweep the small cases: `0` and `11` offer no move at all (count $0$, even) so Zlatan loses immediately; `10` gives exactly one move; `101` has $c_0 = 1$ and $c_1 = 2$, so one move, and Zlatan wins. `111` has no `0` at all.

## Edge cases

- **The move count is forced, so there is no strategy to analyse.** Every move deletes one `0` and one `1`, and while both characters remain some adjacent unequal pair must exist — so exactly $\min(\#0, \#1)$ moves happen whatever either player does, and only its parity matters.
- **A string of one character** (rows $1$, $2$ and $4$): no move exists, so Zlatan loses immediately and Ramos wins with zero moves played.
- **$N = 1$**: always Ramos, for the same reason.
- **Zlatan moves first**, so an odd move count means he makes the last one and Ramos is stuck — hence `Zlatan` on odd parity.
- **Unequal counts** (the fifth row, one `0` against two `1`s): the smaller count caps the moves, and the leftover `1`s are unusable.
- **Sum of $N \leq 3 \cdot 10^5$**: a single `count` call per case on the byte string, with no per-character Python loop.

## Dry run

| $S$ | zeros | ones | moves $\min$ | parity | winner |
|---|---:|---:|---:|---|---|
| `0` | 1 | 0 | 0 | even | `Ramos` |
| `11` | 0 | 2 | 0 | even | `Ramos` |
| `10` | 1 | 1 | 1 | odd | `Zlatan` |
| `111` | 0 | 3 | 0 | even | `Ramos` |
| `101` | 1 | 2 | 1 | odd | `Zlatan` |

In the last row Zlatan deletes either `10` or `01`, leaving a single `1` that Ramos cannot touch.
