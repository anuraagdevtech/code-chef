---
topic: Basic Math
subtopic: Comparing ratios by cross-multiplication
time: $O(1)$ per test case
space: $O(1)$
---
Speed is distance over time, so the comparison is

$$\frac{A}{X} \quad\text{versus}\quad \frac{B}{Y}$$

Computing the two quotients as floats would work at these bounds, but it is the fragile route: `10 / 3` and `20 / 6` are mathematically equal yet can differ in the last bit, which would turn sample case 2 from `EQUAL` into a spurious winner. Equality tests on floats are exactly where this bites.

Multiply out instead. Both $X$ and $Y$ are at least $1$, so multiplying both sides by the positive quantity $XY$ preserves the direction and gives

$$A \cdot Y \quad\text{versus}\quad B \cdot X$$

a comparison of two integers, exact by construction. Note the cross: Alice's distance pairs with **Bob's** time. Multiplying $A \cdot X$ against $B \cdot Y$ is the natural typo and compares something meaningless.

Checking sample case 2: $10 \cdot 6 = 60$ and $20 \cdot 3 = 60$, equal, so `EQUAL` — decided exactly, with no tolerance to tune.

Three outcomes need three branches; collapsing the tie into one of the inequalities would silently report a winner for equal speeds.

## Edge cases

- **Equal speeds** ($10/3$ against $20/6$): the cross-products match, so `EQUAL`. The sample's second row, and it needs its own branch.
- **Cross-multiplication keeps it exact.** Comparing $A/X$ with $B/Y$ as floats invites a rounding error precisely at the tie, which is the case the problem cares about; multiplying out uses only integers.
- **No overflow risk**: both products are at most $1000 \times 1000 = 10^6$.
- **Only the ratios matter**, not the raw distances: $10/3$ and $20/6$ are different pairs of numbers with the same speed.
- **Output case is free.** The statement asks for `ALICE`, `BOB` and `EQUAL` and adds that any mix of upper and lower case is accepted, which is why the sample display shows `Bob` while the solution prints `BOB`.

## Dry run

| $A$ | $X$ | $B$ | $Y$ | Alice $A \cdot Y$ | Bob $B \cdot X$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 20 | 6 | 20 | 5 | 100 | 120 | `BOB` |
| 10 | 3 | 20 | 6 | 60 | 60 | `EQUAL` |
| 9 | 1 | 1 | 1 | 9 | 1 | `ALICE` |

Row 2 is the exact tie that floating point would put at risk.
