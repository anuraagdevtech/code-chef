# 002. Greater Average

> [`AVGPROBLEM`](https://www.codechef.com/problems/AVGPROBLEM) &middot; difficulty **500** &middot; complexity class **Constant time** $O(1)$

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Integer arithmetic, avoiding floats |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Problem

You are given $3$ numbers $A, B,$ and $C$.

Determine whether the **average** of $A$ and $B$ is **strictly greater** than $C$ or not?

**NOTE:** Average of $A$ and $B$ is defined as $\frac{(A+B)}{2}$. For example, average of $5$ and $9$ is $7$, average of $5$ and $8$ is $6.5$.

## Problem constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, C \leq 10$

## Approach

The question asks whether $\frac{A+B}{2} > C$. The tempting move is to compute the average directly as a float and compare, but that drags floating point into a problem that is purely about integers — and `(a + b) / 2` in Python 3 produces a `float`, which for large inputs can lose precision.

Multiply both sides by $2$ instead. Since $2$ is positive the inequality direction is preserved, so the condition becomes

$$A + B > 2C$$

which uses nothing but integer addition and comparison. This is exact for any input size, and it is the habit worth building: **clear the denominator rather than divide.**

Note the word *strictly*. When $A + B = 2C$ the average equals $C$ exactly and the answer is `NO`, so the comparison must be `>` and not `>=`. Sample case 3 ($5, 7, 6$ → average exactly $6$) is there precisely to catch that off-by-one.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # (a + b) / 2 > c  <=>  a + b > 2 * c, kept in integers.
        out.append("YES" if a + b > 2 * c else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

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

---

Same problem grouped by topic: [../docs/basic-math/AVGPROBLEM.md](../docs/basic-math/AVGPROBLEM.md)
