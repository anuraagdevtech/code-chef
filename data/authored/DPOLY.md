---
topic: Arrays
subtopic: Last index satisfying a predicate
time: $O(N)$ per test case
space: $O(1)$
---
Coefficient $A_i$ belongs to the term $x^i$, so the array index *is* the exponent. The degree is the highest power with a non-zero coefficient, which makes this a scan for the **last non-zero entry** and a report of its index.

Scanning from the right and stopping at the first non-zero is the natural phrasing and exits early. Scanning left to right while remembering the most recent non-zero index works equally well and is what the code below does, since it reads cleanly and still costs one pass.

Three things make this less trivial than it looks.

**Trailing zeros are not part of the polynomial.** Sample case 4 is $1 + 2x + 4x^2 + 0x^3$, whose degree is $2$, not $3$. Taking $N - 1$ as the answer ignores the actual coefficients and fails exactly here.

**Leading zeros are fine.** Sample case 3 is $0 + 0x + 5x^2$, degree $2$ — zeros below the top term are irrelevant, so the scan must look at the highest non-zero index rather than the first.

**Coefficients may be negative.** The test is `!= 0`, not `> 0`. Sample case 2 has $A_0 = -3$, and a truthiness-style check for "positive" would mishandle such terms in general.

The guarantee that at least one coefficient is non-zero means the scan always finds something, so the zero polynomial — whose degree is conventionally undefined or $-\infty$ — never arises. Sample case 1 is the constant polynomial $5$, of degree $0$.

## Edge cases

- **Trailing zero coefficients** ($1, 2, 4, 0$): the degree is $2$, not $3$. Returning $N - 1$ is the trap, and the sample's last row catches it.
- **Leading zeros** ($0, 0, 5$): the degree is $2$ — low-order zeros are irrelevant, only the highest nonzero index matters.
- **Negative coefficients count as nonzero** ($-3$): testing `a > 0` instead of `a != 0` misses them, and the sample's second row has one.
- **A constant polynomial** ($5$): degree $0$.
- **At least one coefficient is nonzero** by the constraints, so the answer is always well defined; the initial value of $0$ would otherwise be a silently wrong default for an all-zero input.

## Dry run

| coefficients (index = exponent) | nonzero indices | highest | output |
|---|---|---:|---|
| $5$ | $0$ | 0 | `0` |
| $-3, 3$ | $0, 1$ | 1 | `1` |
| $0, 0, 5$ | $2$ | 2 | `2` |
| $1, 2, 4, 0$ | $0, 1, 2$ | 2 | `2` |

Row 4 has four coefficients but degree $2$.
