---
topic: Number Theory
subtopic: Divisibility as an exact-fit condition
time: $O(1)$ per test case
space: $O(1)$
---
Each round consumes exactly $N$ tiles, one per player. After $r$ complete rounds, $rN$ tiles have been placed. The two validity rules say that every round must be complete (so the count is always a whole multiple of $N$) and that no tiles may be left over (so that multiple must equal $X$).

Putting them together, the game is valid exactly when $X = rN$ for some non-negative integer $r$ — that is, when

$$X \equiv 0 \pmod N$$

So the whole problem is `x % n == 0`.

The reason both rules collapse into one test is worth seeing. "Every round complete" alone would allow leftovers; "all tiles used" alone would allow a final partial round. Requiring both is precisely the statement that $N$ divides $X$ exactly.

Note the asymmetry that makes sample case 3 surprising at first glance: $N = 2$ players with $X = 4$ tiles is valid because they play two full rounds. There is no requirement that the game last only one round, nor that $X \leq N$. Conversely case 2 has more players than tiles, so not even the first round completes.

Watch the argument order — the input is $N$ then $X$, and computing `n % x` instead would pass case 1 (where both are $3$) while failing the rest.
