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
