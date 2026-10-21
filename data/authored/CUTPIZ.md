---
topic: Number Theory
subtopic: GCD of angular gaps
time: $O(n + \log 360)$ per test case
space: $O(1)$
---
Equal slices mean the final cuts sit at a fixed angular spacing $d$, at positions $a_0, a_0 + d, a_0 + 2d, \ldots$ all the way round. Two conditions follow: $d$ must divide $360$ so the cuts close up, and $d$ must divide every gap $a_i - a_0$ so the existing cuts land on the grid.

The **largest** such $d$ gives the fewest total cuts, and it is exactly

$$d = \gcd\bigl(360,\ a_1 - a_0,\ a_2 - a_0,\ \ldots,\ a_{n-1} - a_0\bigr)$$

The final pizza then has $360/d$ cuts, of which $n$ already exist, so the answer is

$$\frac{360}{d} - n$$

Including $360$ in the gcd is what ties the pattern to a full revolution — without it, a spacing that divides all the gaps but not $360$ would leave a ragged last slice.

Measuring gaps from a common reference $a_0$ rather than between consecutive cuts is equivalent, since the gcd of the differences is the same either way. Using $a_0$ keeps it to one pass.

Sample case 3 is the extreme: cuts at $0°$ and $1°$ force $d = \gcd(360, 1) = 1$, so the pizza must be sliced into $360$ one-degree wedges, needing $358$ more cuts. A single awkward cut can dominate the whole answer.

Sample case 2 has cuts at $90°$ and $210°$, a gap of $120$, so $d = 120$ and one more cut at $330°$ completes three equal thirds. Sample case 1 is already a perfect quartering.

Note the answer is never negative: $d$ divides every gap, so all $n$ distinct cuts lie on the grid of $360/d$ positions.

## Edge cases

- **$360$ must be seeded into the gcd** so the pattern closes over a full turn. Cuts at $0$ and $240$ have a single difference of $240$, and $360/240$ is not an integer; seeding gives $\gcd(360, 240) = 120$ and the correct answer of one extra cut at $120$.
- **Already evenly spaced** (the first row, every $90^\circ$) → $0$ extra cuts.
- **A one-degree offset forces the finest possible division.** The third row's cuts at $0$ and $1$ give $\gcd = 1$, so all $360$ single-degree slices are needed and $358$ cuts must be added.
- **Differences are taken against a fixed base** rather than between consecutive angles, which gives the same gcd and avoids needing a wrap-around term for the last gap.
- **$n \geq 2$ is guaranteed**, so at least one difference exists and the gcd is never left at $360$ by default.
- **The answer is $360/d - n$**, so the existing cuts are subtracted — forgetting that term reports the total slice count instead of the cuts to add.

## Dry run

Second sample: cuts at $90^\circ$ and $210^\circ$.

| step | value |
|---|---|
| difference from base | $210 - 90 = 120$ |
| $\gcd(360, 120)$ | $120$ |
| total slices needed | $360 / 120 = 3$ |
| cuts already made | $2$ |
| extra cuts | `1` |

The missing cut is at $330^\circ$, completing three $120^\circ$ slices.
