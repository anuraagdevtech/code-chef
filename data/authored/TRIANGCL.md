---
topic: Geometry
subtopic: Classifying with squared lengths
time: $O(1)$ per test case
space: $O(1)$
---
Both classifications can be decided from the three **squared** side lengths, so no square roots and no floating point are needed — the coordinates are integers, so every squared length is an exact integer.

**By sides.** Two sides are equal exactly when their squared lengths are equal, since lengths are non-negative. So the triangle is *Isosceles* if any two squared lengths match and *Scalene* otherwise. Equilateral triangles are excluded by the statement, so no third case arises.

**By angles.** Sort the squared lengths as $a \leq b \leq c$; the largest side faces the largest angle. The law of cosines gives $c^2 = a^2 + b^2 - 2ab\cos C$, so the sign of $a + b - c$ (in squared terms) decides it:

- $a + b = c$ → *Right*
- $a + b > c$ → *Acute*
- $a + b < c$ → *Obtuse*

This is the Pythagorean comparison generalised, and working in squares keeps it exact — a float version could misclassify a right triangle whose sides are large integers.

The first input line is `SUBTASK_ID`, and it selects the **output format**, not a different computation:

- subtask $1$ → the side classification only: `Scalene triangle`
- subtask $2$ → both, side first and angle second: `Scalene acute triangle`

Note the capitalisation differs between the two words — the side adjective is capitalised and the angle adjective is not. That line is also easy to mistake for the test count, which would consume the real $T$ and desynchronise the whole input.

The first sample runs subtask $1$: squared sides $2, 1, 5$ are all different, giving `Scalene triangle`, while $25, 25, 32$ gives `Isosceles triangle`.

Under subtask $2$ those same two shapes would report more. The first has $2 + 1 = 3 < 5$, so it is obtuse: `Scalene obtuse triangle`. The second has $25 + 25 = 50 > 32$, so it is acute: `Isosceles acute triangle`. Same geometry, different amount of it reported — which is the point of the selector.
