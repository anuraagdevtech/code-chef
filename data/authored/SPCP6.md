---
topic: Dynamic Programming
subtopic: Ways by lines cleared and whose turn it is
time: $O(\max L + T)$
space: $O(\max L)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let `chef[i]` be the number of move sequences after which exactly $i$ lines are cleared and it is Chef's turn, and `chefina[i]` the same with Chefina to move. A move of 1 line passes the turn; moves of 2, 3 or 4 lines keep it:

$$\text{chef}[i] = \text{chefina}[i-1] + \text{chef}[i-2] + \text{chef}[i-3] + \text{chef}[i-4],$$

and symmetrically for Chefina, with `chef[0] = 1`.

The game ends as soon as the total reaches $L$, and Chef must end it with a 4-line move. So the game is at some total $i < L$ with Chef to move and $i + 4 \ge L$: the answer is $\text{chef}[L-4] + \dots + \text{chef}[L-1]$ (indices below 0 skipped). States with $i < L$ are exactly the unfinished games, so nothing is counted after the end.

All queries share one table built up to the largest $L$.

## Edge cases

- For $L \le 4$ the window is cut off at 0 and includes the empty game (an immediate Tetris).
- The finishing move must be exactly a 4, even when fewer lines would be enough to reach $L$.
- A 1-line move changes the player; this is the only link between the two arrays.
- Results are modulo $10^9 + 7$.

## Dry run

`L = 3`.

`chef[0] = 1`; `chefina[1] = chef[0] = 1`, `chef[1] = chefina[0] = 0`; `chef[2] = chefina[1] + chef[0] = 2`.

Answer `chef[0] + chef[1] + chef[2] = 3`: a Tetris at once; 2 lines then a Tetris; or 1 line, Chefina clears 1 line, then a Tetris.
