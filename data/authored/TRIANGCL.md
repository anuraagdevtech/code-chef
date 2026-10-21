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

## Edge cases

- **The first token is the subtask number, not the test count.** Reading it as $T$ swallows the real $T$ and shifts every coordinate — the single most likely way to fail this problem.
- **The same input feeds two different output formats**: subtask $1$ wants only the side classification, subtask $2$ adds the angle.
- **Squared lengths keep everything exact.** The right-angle test is an equality, and taking square roots would turn it into a float comparison that can miss — a $3$–$4$–$5$ triangle is detected as $9 + 16 = 25$ with no rounding at all.
- **Equilateral triangles cannot occur on an integer grid**, so `Isosceles` covers every non-scalene case and no third side-category is needed.
- **The largest angle faces the largest side**, which is why only the two smaller squares are summed and compared against the largest — testing an arbitrary pair would misclassify.
- **Coordinates may be negative** ($|x_i| \leq 100$), which squaring handles; the sorted triple is all that matters afterwards.

## Dry run

Subtask 2, second case: $(0,0)$, $(1,0)$, $(1,2)$.

| side | squared length |
|---|---:|
| $(0,0)$–$(1,0)$ | 1 |
| $(1,0)$–$(1,2)$ | 4 |
| $(0,0)$–$(1,2)$ | 5 |

Sorted $1, 4, 5$: no two equal, so **Scalene**; and $1 + 4 = 5$ exactly, so **right**. Output `Scalene right triangle`.
