---
topic: Basic Math
subtopic: Comparing ratios by cross-multiplication
time: $O(1)$ per test case
space: $O(1)$
---
The constraint $X_1 < X_3 < X_2$ places the bottle strictly between the two restaurants, so each cook runs directly toward it and the distances are

$$d_{\text{Chef}} = X_3 - X_1, \qquad d_{\text{Kefa}} = X_2 - X_3$$

both automatically positive — no absolute values needed, which is exactly what that ordering constraint buys.

Comparing arrival times $d_1/V_1$ against $d_2/V_2$ and cross-multiplying by the positive quantity $V_1 V_2$ gives the exact integer test

$$d_1 \cdot V_2 \quad\text{versus}\quad d_2 \cdot V_1$$

with Chef first when $d_1 V_2 < d_2 V_1$. Note the cross: Chef's distance pairs with **Kefa's** speed.

Float division would be the risky route precisely because `Draw` is a possible answer — sample case 3 is an exact tie, and a float comparison could miss it. Integers decide equality cleanly.

The magnitudes are worth a glance for a C solution: coordinates reach $10^5$ in absolute value so a distance can reach $2 \times 10^5$, and multiplying by a speed up to $10^5$ gives $2 \times 10^{10}$ — past the 32-bit limit and needing a 64-bit type. Python handles it without comment.

Sample case 2 shows the shorter distance winning despite the slower speed: Chef covers $1$ unit at speed $1$ in one second, while Kefa needs $1.5$ seconds for $3$ units at speed $2$.

## Edge cases

- **A draw** (third row: both products equal $4$): needs its own branch.
- **$X_1 < X_3 < X_2$ is guaranteed**, so both distances are strictly positive — there is no zero-distance or sign case to handle.
- **Coordinates may be negative** ($|X_i| \leq 10^5$), so the distances must come from the differences rather than from the coordinates themselves.
- **Cross-multiplication keeps the tie exact.** The comparison is between the times $\frac{X_3 - X_1}{V_1}$ and $\frac{X_2 - X_3}{V_2}$; multiplying out avoids a float rounding error at precisely the `Draw` case.
- The **lower** time wins, so the inequality runs the opposite way to a speed comparison.

## Dry run

| $X_1$ | $X_2$ | $X_3$ | $V_1$ | $V_2$ | Chef $(X_3{-}X_1)V_2$ | Kefa $(X_2{-}X_3)V_1$ | output |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3 | 2 | 1 | 2 | 2 | 1 | `Kefa` |
| 1 | 5 | 2 | 1 | 2 | 2 | 3 | `Chef` |
| 1 | 5 | 3 | 2 | 2 | 4 | 4 | `Draw` |
