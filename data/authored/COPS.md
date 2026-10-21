---
topic: Simulation
subtopic: Marking covered ranges over a small domain
time: $O(100 + M)$ per test case
space: $O(1)$
---
A cop at house $c$ runs at $x$ houses per minute for $y$ minutes, so they sweep everything within $x \cdot y$ houses in either direction — the closed interval

$$[\,c - xy,\; c + xy\,]$$

Devu is safe in any house of $1 \ldots 100$ covered by no cop. Since the domain is only $100$ houses, the simplest correct approach is to mark a boolean array: for each cop, flag the intersection of their interval with $[1, 100]$, then count the unflagged houses.

Clamping to $[1, 100]$ is what keeps the marking in bounds — a cop near either end reaches past the street, and those positions simply do not exist. Sample case 1 has cops whose combined reach of $56$ houses blankets the entire street, leaving $0$ safe houses.

The intervals **overlap**, which is why a union (or a marking array) is needed rather than summing interval lengths. Sample case 3 is built on that: cops at $10$ and $51$ with reach $40$ cover $[1,50]$ and $[11,91]$, which overlap heavily; their union is $[1,91]$, leaving $9$ safe houses. Adding the interval sizes would badly overcount the danger and under-report the safe houses.

Sample case 2 leaves two separate safe stretches — $42$–$54$ and $96$–$100$ — showing the answer need not be contiguous.

With $x, y, M \leq 10$ the reach is at most $100$, and the whole simulation is trivially fast even at $T = 10^4$.

## Edge cases

- **The input order is $M$, $X$, $Y$** — the count comes first, before the two speed values. Reading them as $X, Y, M$ transposes the reach and the cop count and passes none of the sample rows.
- **Ranges must be clamped to $[1, 100]$.** In the first row the reach is $7 \times 8 = 56$, so a cop at house $12$ covers from $-44$ — an unclamped index would wrap around to the end of the array in Python and mark the wrong houses.
- **Overlapping ranges must not be double-counted.** The third row has a cop covering $[1, 50]$ and another $[11, 91]$; summing range lengths gives $131$ "covered" houses out of $100$. Marking a boolean array makes the overlap free.
- **Total coverage** (the first row): the answer is $0$.
- **Gaps can be interior as well as at the ends.** The second row leaves $42$–$54$ in the middle *and* $96$–$100$ at the end, totalling $18$ — a solution that only measures the ends of the street misses half of it.
- The street is fixed at $100$ houses regardless of the inputs.

## Dry run

Second sample: $M = 2$, $X = 10$, $Y = 2$, so reach $= 20$; cops at $21$ and $75$.

| cop | raw range | clamped |
|---:|---|---|
| 21 | $[1, 41]$ | $[1, 41]$ |
| 75 | $[55, 95]$ | $[55, 95]$ |

| uncovered stretch | houses |
|---|---:|
| $42$–$54$ | 13 |
| $96$–$100$ | 5 |

Output `18`.
