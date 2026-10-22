[&larr; 108. Area OR Perimeter](AREAPERI.md) &middot; [Index](../../README.md) &middot; [252. Chef and Three Dogs &rarr;](CHDOGS.md)

# 247. Triangle Classification

> CodeChef problem code [`TRIANGCL`](https://www.codechef.com/problems/TRIANGCL) &middot; difficulty **1462** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Classifying with squared lengths |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Triangle classification is an important problem in modern mathematics. Mathematicians have developed many criteria according to which a triangle can be classified. In this problem, you will be asked to classify some triangles according to their sides and angles.

According to their measure, angles may be:

- **Acute** — an angle that is less than 90 degrees

- **Right** — a 90-degrees angle

- **Obtuse** — an angle that is greater than 90 degrees

According to their sides, triangles may be:

- **Scalene** — all sides are different

- **Isosceles** — exactly two sides are equal

According to their angles, triangles may be:

- **Acute** — all angles are acute

- **Right** — one angle is right

- **Obtuse** — one angle is obtuse

**Triangles with three equal sides (equilateral triangles) will not appear in the test data.**

The triangles formed by three collinear points are not considered in this problem. In order to classify a triangle, you should use only the adjactives from the statement. There is no triangle which could be described in two different ways according to the classification characteristics considered above.

**Input**

The first line of input contains an integer **SUBTASK_ID** denoting the subtask id this input belongs to.

The second line of input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains six integers **x_1**, **y_1**, **x_2**, **y_2**, **x_3** and **y_3** denoting Cartesian coordinates of points, that form the triangle to be classified.

It is guaranteed that the points are non-collinear.

**Output**

For each test case, output a single line containing the classification of the given triangle.

If **SUBTASK_ID** equals 1, then the classification should follow the "<*Side classification starting with a capital letter*> triangle" format.

If **SUBTASK_ID** equals 2, then the classification should follow the "<*Side classification starting with a capital letter*> <*angle classification*> triangle" format.

Please, check out the samples section to better understand the format of the output.

**Constraints**

- 1 ≤ **T** ≤ 60

- **|x_i|**, **|y_i|** ≤ 100

- Subtask 1 (50 points): *no additional constraints*

- Subtask 2 (50 points): *no additional constraints*

**Note**

The first test of the first subtask and the first test of the second subtask are the example tests (each in the corresponding subtask). It's made for you to make sure that your solution produces the same verdict both on your machine and our server.

**Tip**

Consider using the following condition in order to check whether two floats or doubles **A** and **B** are equal instead of traditional **A == B**: **|A - B| < 10^-6**.

## Constraints

- 1 ≤ T ≤ 60
- |x_i|, |y_i| ≤ 100
- Subtask 1 (50 points): no additional constraints
- Subtask 2 (50 points): no additional constraints

## Sample

**Sample 1 input**

```
1
2
0 0 1 1 1 2
3 0 0 4 4 7
```

**Sample 1 output**

```
Scalene triangle
Isosceles triangle
```

**Sample 2 input**

```
2
6
0 0 4 1 1 3
0 0 1 0 1 2
0 0 1 1 1 2
0 0 2 1 1 2
3 0 0 4 4 7
0 0 2 1 4 0
```

**Sample 2 output**

```
Scalene acute triangle
Scalene right triangle
Scalene obtuse triangle
Isosceles acute triangle
Isosceles right triangle
Isosceles obtuse triangle
```

## Approach

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

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    subtask = int(data[0])            # not the test count
    t = int(data[1])
    out = []
    for i in range(t):
        x1, y1, x2, y2, x3, y3 = map(int, data[2 + 6 * i:8 + 6 * i])
        # Squared lengths stay exact integers, so no sqrt and no floats.
        d = sorted((
            (x1 - x2) ** 2 + (y1 - y2) ** 2,
            (x2 - x3) ** 2 + (y2 - y3) ** 2,
            (x1 - x3) ** 2 + (y1 - y3) ** 2,
        ))
        by_side = "Isosceles" if d[0] == d[1] or d[1] == d[2] else "Scalene"
        if subtask == 1:
            out.append(f"{by_side} triangle")
        else:
            # The largest side faces the largest angle.
            total = d[0] + d[1]
            by_angle = "right" if total == d[2] else "acute" if total > d[2] else "obtuse"
            out.append(f"{by_side} {by_angle} triangle")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

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

---

Same problem in rating order (#264 of 486): [../../by-rating/264-TRIANGCL.md](../../by-rating/264-TRIANGCL.md)
