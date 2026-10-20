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
