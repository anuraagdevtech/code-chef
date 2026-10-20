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
