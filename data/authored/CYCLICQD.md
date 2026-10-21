---
topic: Geometry
subtopic: Cyclic quadrilateral angle condition
time: $O(1)$ per test case
space: $O(1)$
---
A quadrilateral is cyclic — its vertices lie on a common circle — exactly when each pair of **opposite** angles sums to $180°$. The angles arrive in order around the perimeter, so the opposite pairs are $(A, C)$ and $(B, D)$.

The useful observation is that checking one pair is enough. The constraints guarantee

$$A + B + C + D = 360$$

so if $A + C = 180$ then $B + D = 360 - 180 = 180$ automatically. The two conditions are equivalent, and testing `a + c == 180` settles it.

Adjacency is where this goes wrong. Pairing $(A, B)$ and $(C, D)$ — the values that sit next to each other in the input — tests something geometrically meaningless. Sample case 2 distinguishes the two readings: $10 + 170 = 180$ for the opposite pair gives `YES`, while the adjacent pair $10 + 20 = 30$ would give `NO`.

Sample case 3 is a good check that the angle sum alone is not sufficient: $179 + 1 + 179 + 1 = 360$, a perfectly valid quadrilateral, yet $A + C = 358$ and it is not cyclic.

Everything here is integer arithmetic on angles in whole degrees, so there is no tolerance to worry about and the equality test is exact.

## Edge cases

- **The angles arrive in perimeter order**, so $A$ and $C$ are *opposite*, as are $B$ and $D$. Testing an adjacent pair such as $A + B$ is the trap, and it gives a different answer on every sample row.
- **Only one check is needed.** Since $A + B + C + D = 360$ is guaranteed, $A + C = 180$ forces $B + D = 180$ automatically — verifying both is harmless but redundant.
- **Equal opposite angles are not the condition**: the sample's third row has $A = C = 179$, summing to $358$, so `NO`.
- **The bounds** $1 \leq A, B, C, D \leq 357$ keep every angle positive, so there is no degenerate quadrilateral to reject separately.

## Dry run

| $A$ | $B$ | $C$ | $D$ | $A + C$ | $= 180$? | output |
|---:|---:|---:|---:|---:|:---:|---|
| 10 | 20 | 30 | 300 | 40 | no | `NO` |
| 10 | 20 | 170 | 160 | 180 | yes | `YES` |
| 179 | 1 | 179 | 1 | 358 | no | `NO` |

In row 2, $B + D = 20 + 160 = 180$ as well, which the fixed total guarantees.
