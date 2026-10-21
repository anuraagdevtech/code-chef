---
topic: Basic Math
subtopic: Integer arithmetic, avoiding floats
time: $O(1)$ per test case
space: $O(1)$
---
The question asks whether $\frac{A+B}{2} > C$. The tempting move is to compute the average directly as a float and compare, but that drags floating point into a problem that is purely about integers — and `(a + b) / 2` in Python 3 produces a `float`, which for large inputs can lose precision.

Multiply both sides by $2$ instead. Since $2$ is positive the inequality direction is preserved, so the condition becomes

$$A + B > 2C$$

which uses nothing but integer addition and comparison. This is exact for any input size, and it is the habit worth building: **clear the denominator rather than divide.**

Note the word *strictly*. When $A + B = 2C$ the average equals $C$ exactly and the answer is `NO`, so the comparison must be `>` and not `>=`. Sample case 3 ($5, 7, 6$ → average exactly $6$) is there precisely to catch that off-by-one.

## Edge cases

- **Exact tie**, $A + B = 2C$: the average equals $C$ and the answer must be `NO`, since the question asks for *strictly* greater. Sample case 3 is this case.
- **All values minimal** ($1,1,1$): $2 > 2$ is false, so `NO`.
- **All values maximal** ($10,10,10$): $20 > 20$ is false, so `NO` — the extremes behave like the tie, not like a win.
- **Widest gap** ($A = B = 10$, $C = 1$): $20 > 2$, so `YES`.
- No parity special case is needed: $A + B$ may be odd, which is exactly why multiplying out beats dividing.

## Dry run

| $A$ | $B$ | $C$ | $A + B$ | $2C$ | $A+B > 2C$ | output |
|---:|---:|---:|---:|---:|:---:|---|
| 5 | 9 | 6 | 14 | 12 | yes | `YES` |
| 5 | 8 | 6 | 13 | 12 | yes | `YES` |
| 5 | 7 | 6 | 12 | 12 | no | `NO` |
| 4 | 9 | 8 | 13 | 16 | no | `NO` |
| 3 | 7 | 2 | 10 | 4 | yes | `YES` |

Row 3 is the tie: the true average is exactly $6$, so it fails the strict test.
