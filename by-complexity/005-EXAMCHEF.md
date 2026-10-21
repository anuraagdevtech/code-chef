# 005. Exams

> [`EXAMCHEF`](https://www.codechef.com/problems/EXAMCHEF) &middot; difficulty **519** &middot; complexity class **Constant time** $O(1)$

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Percentage comparison without division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Problem

In Chefland, there are $X$ schools, and each school has $Y$ students.
The year end results are in and a total of $Z$ students passed the exams.

Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was **strictly greater** than $50\%$.

## Problem constraints

- $1 \leq T \leq 2\cdot 10^4$
- $1 \leq X \leq 5$
- $1 \leq Y \leq 50$
- $0 \leq Z \leq X\cdot Y$

## Approach

There are $X$ schools of $Y$ students each, so $X \cdot Y$ students sat the exams and $Z$ of them passed. The question is whether the pass rate exceeded $50\%$:

$$\frac{Z}{X \cdot Y} > \frac{1}{2}$$

Cross-multiplying by the positive quantity $2 \cdot X \cdot Y$ turns this into

$$2Z > X \cdot Y$$

which is again pure integer arithmetic. Dividing instead would introduce a float and, worse, invite a rounding mistake exactly at the halfway point that the problem cares most about.

The *strictly* greater wording matters. When $2Z = X \cdot Y$ the pass rate is exactly $50\%$ and the answer is `NO`. Sample case 4 is built on this: $X=3, Y=6, Z=9$ gives $18$ students and $9$ passes, precisely half, so `NO`.

With $T$ up to $2 \cdot 10^4$ it is worth reading all input at once rather than calling `input()` per line; the arithmetic itself is free.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # z / (x * y) > 1 / 2  <=>  2 * z > x * y
        out.append("YES" if 2 * z > x * y else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Exactly half pass**, $2Z = XY$: the rate is $50\%$, not above it, so `NO`. Sample case 4 ($3 \times 6 = 18$ students, $9$ passes) is built on this.
- **$Z = 0$**: nobody passed, so `NO` for any $X, Y$.
- **$Z = XY$**: everybody passed, and $2XY > XY$ holds for all $X, Y \geq 1$, so `YES`.
- **Smallest school** ($X = Y = 1$): $Z = 0$ gives `NO` and $Z = 1$ gives `YES` — a single student is either all or nothing.
- $XY$ is at most $250$, so there is no overflow concern; the reason to multiply out is exactness at the halfway point, not range.

## Dry run

| $X$ | $Y$ | $Z$ | students $XY$ | $2Z$ | $2Z > XY$ | output |
|---:|---:|---:|---:|---:|:---:|---|
| 2 | 10 | 12 | 20 | 24 | yes | `YES` |
| 2 | 10 | 3 | 20 | 6 | no | `NO` |
| 1 | 5 | 3 | 5 | 6 | yes | `YES` |
| 3 | 6 | 9 | 18 | 18 | no | `NO` |

Row 3 shows an odd total handled exactly, and row 4 the $50\%$ tie failing.

---

Same problem grouped by topic: [../docs/basic-math/EXAMCHEF.md](../docs/basic-math/EXAMCHEF.md)
