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
