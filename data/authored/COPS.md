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
