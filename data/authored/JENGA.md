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

## Edge cases

- **Fewer tiles than one round needs** ($N = 4$, $X = 2$): $2 \bmod 4 = 2$, so `NO` — not even one round completes. The sample's second row covers it, and it is also the row that catches swapping the operands, since $4 \bmod 2 = 0$ would wrongly say `YES`.
- **Exactly one round's worth** ($N = X$): `YES`.
- **$N = 1$**: every $X$ is divisible by $1$, so always `YES`.
- **Largest inputs** ($N = X = 1000$): `YES`.
- The condition is an exact fit, not "enough tiles": leftovers are a failure, so divisibility is the whole test.

## Dry run

| $N$ (per round) | $X$ (tiles) | $X \bmod N$ | output |
|---:|---:|---:|---|
| 3 | 3 | 0 | `YES` |
| 4 | 2 | 2 | `NO` |
| 2 | 4 | 0 | `YES` |

Rows 2 and 3 are the same pair of numbers swapped, and they give opposite answers.
