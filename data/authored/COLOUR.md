---
topic: Brute Force
subtopic: Enumerating a tiny decision space
time: $O(1)$ per test case — eight combinations
space: $O(1)$
---
There are exactly three secondary colours — yellow (red+green), cyan (green+blue), magenta (red+blue) — and making a second drop of one already-made secondary adds nothing, since only **distinct** colours are counted. So each secondary is a yes/no decision, giving $2^3 = 8$ combinations to try.

For a choice $(y, c, m) \in \{0,1\}^3$, the drops consumed are $y + m$ red, $y + c$ green, and $c + m$ blue. The total distinct colours is then

$$\underbrace{[\,X - (y{+}m) \geq 1\,] + [\,Y - (y{+}c) \geq 1\,] + [\,Z - (c{+}m) \geq 1\,]}_{\text{primaries still in hand}} \;+\; y + c + m$$

subject to every remainder being non-negative. Taking the maximum over the eight combinations answers it.

The tension is that a secondary **consumes** the primaries it is made from, so a colour can be lost to gain one. Sample case 3 is exactly that trade: with one drop each, keeping all three primaries scores $3$, while mixing any pair destroys two primaries to gain one secondary and scores only $2$.

Sample case 2 shows when the trade pays: three drops each of red and green leave plenty spare, so mixing one of each yields yellow *and* keeps both primaries, for $3$.

Sample case 1 is the opposite: one red and one blue can make magenta, but doing so consumes both, leaving a single colour instead of two.

Enumerating beats case analysis here — the interactions between the three decisions are fiddly, and eight evaluations cost nothing even at $T = 10^5$.

## Edge cases

- **Making a secondary can lose you colours.** Each one consumes a unit of each of its two primaries, so with $1, 1, 1$ the best move is to make nothing and keep three distinct colours; mixing yellow drops red and green and leaves only two.
- **Leftover primaries count once each**, however many units remain — hence `(r >= 1)` rather than `r`. The second row keeps red and green with two units each and still scores them as one apiece.
- **All zeros** → $0$, with every combination either infeasible or empty.
- **At most one of each secondary is ever worth making**, because a second copy adds nothing to the distinct count while consuming more primaries — which is why the search is over $\{0,1\}^3$ and not over quantities.
- **Infeasible combinations must be rejected, not clamped.** A negative remainder means the primaries were over-spent, and treating it as zero would invent colours.
- **$X$, $Y$, $Z$ may be zero independently**, which rules out several secondaries at once — the first row has no green, so neither yellow nor cyan is possible.

## Dry run

Third sample: $X = Y = Z = 1$.

| yellow | cyan | magenta | red left | green left | blue left | feasible | distinct colours |
|:---:|:---:|:---:|---:|---:|---:|:---:|---:|
| 0 | 0 | 0 | 1 | 1 | 1 | yes | **3** |
| 1 | 0 | 0 | 0 | 0 | 1 | yes | 2 |
| 0 | 1 | 0 | 1 | 0 | 0 | yes | 2 |
| 0 | 0 | 1 | 0 | 1 | 0 | yes | 2 |
| 1 | 1 | 0 | 0 | $-1$ | — | no | — |

Output `3`: mixing anything here is a loss.
