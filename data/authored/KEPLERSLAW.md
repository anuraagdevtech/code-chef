---
topic: Basic Math
subtopic: Testing proportionality by cross-multiplication
time: $O(1)$ per test case
space: $O(1)$
---
Kepler's third law says $T^2 \propto R^3$, so the constant $T^2/R^3$ must match for both planets:

$$\frac{T_1^2}{R_1^3} = \frac{T_2^2}{R_2^3}$$

Cross-multiplying by the positive quantity $R_1^3 R_2^3$ turns this into an exact integer identity:

$$T_1^2 \cdot R_2^3 = T_2^2 \cdot R_1^3$$

This is the right way to test any proportionality. Computing the two ratios as floats and comparing with `==` is unreliable — the quotients are rarely representable exactly, and sample case 3 ($1, 8, 2, 8$) would hinge on whether $1/8$ and $64/512$ happen to round identically. The integer form decides it exactly: $1 \cdot 512 = 512$ and $64 \cdot 8 = 512$.

Note the **cross** again: planet 1's period pairs with planet 2's axis. Writing $T_1^2 R_1^3 = T_2^2 R_2^3$ tests a different and meaningless relation.

The exponents must also be the right way round — period **squared** against axis **cubed**. Swapping them would pass sample case 1, where every value is $1$, but fail the others.

With all inputs at most $10$, the products stay below $10^5$, so there is no magnitude concern even in a fixed-width language.

## Edge cases

- **Identical pairs** ($1\,1\,1\,1$): trivially `Yes`.
- **The exponents must be the right way round** — $T$ squared against $R$ cubed. Swapping them changes the third row's answer from `Yes` to `No`, since $1 \cdot 8^2 = 64$ against $8^3 \cdot 2^2 = 2048$.
- **Cross-multiplication keeps the exact case exact.** Comparing $T^2/R^3$ as floats risks a false negative precisely on the third row, where the equality holds exactly ($512 = 512$).
- **No overflow**: the cubes reach $1000$ and the squares $100$, so the products stay around $10^5$.

## Dry run

| $T_1$ | $T_2$ | $R_1$ | $R_2$ | $T_1^2 R_2^3$ | $T_2^2 R_1^3$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | 1 | 1 | `Yes` |
| 1 | 2 | 3 | 4 | 64 | 108 | `No` |
| 1 | 8 | 2 | 8 | 512 | 512 | `Yes` |

Row 3 is the exact equality that floating point would endanger.
