---
topic: Basic Math
subtopic: Distance on a circle
time: $O(1)$ per test case
space: $O(1)$
---
The track is a cycle of $M$ checkpoints joined by unit-length roads, and the roads are **bidirectional** — so Chef may walk either way around. The two routes between $A$ and $B$ partition the whole loop, so their lengths sum to $M$:

$$d = |A - B|, \qquad \text{answer} = \min(d,\; M - d)$$

Bidirectionality is the hinge. On a one-way track the answer would be $(B - A) \bmod M$, direction-dependent and often much larger. Sample case 2 shows the difference starkly: from checkpoint $1$ to $98$ on a $100$-track, the forward walk is $97$ but going backwards is only $3$.

The `min` also means the answer never exceeds $\lfloor M/2 \rfloor$ — the furthest two points on a cycle are diametrically opposite.

Sample case 4 is the tightest case: $M = 2$, so the two checkpoints are adjacent both ways and $d = M - d = 1$. The `min` is indifferent, which is correct — both routes are one road long.

The absolute value handles $B < A$ without a branch, as in sample case 3 where the walk runs from $40$ down to $30$. And since $A \neq B$ is guaranteed, the answer is always at least $1$.

With $M$ up to $10^9$ the arithmetic is trivial for Python, and no modular reduction is needed because $A$ and $B$ already lie in $[1, M]$.

## Edge cases

- **The long way round is shorter** ($A = 1$, $B = 98$, $M = 100$): going backwards costs $3$ against $97$ forwards. Returning $|A - B|$ alone fails here, and the sample's second row is exactly this.
- **Exactly antipodal** ($A = 2$, $B = 1$, $M = 2$): both arcs measure $1$, so the tie is harmless.
- **$A \neq B$ is guaranteed**, so the distance is never zero.
- **Largest track** ($M = 10^9$): no overflow, and the two arcs always sum to $M$.
- Roads are bidirectional, which is the fact that makes the answer a minimum of two arcs rather than one directed distance.

## Dry run

| $A$ | $B$ | $M$ | one way $|A-B|$ | the other $M - d$ | output |
|---:|---:|---:|---:|---:|---|
| 1 | 3 | 100 | 2 | 98 | `2` |
| 1 | 98 | 100 | 97 | 3 | `3` |
| 40 | 30 | 50 | 10 | 40 | `10` |
| 2 | 1 | 2 | 1 | 1 | `1` |

Row 2 takes the back route; row 4 is the tie.
