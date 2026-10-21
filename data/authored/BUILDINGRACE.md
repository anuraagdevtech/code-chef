---
topic: Basic Math
subtopic: Comparing ratios by cross-multiplication
time: $O(1)$ per test case
space: $O(1)$
---
Chef descends $A$ floors at $X$ floors per minute and Chefina descends $B$ floors at $Y$, so their times are $A/X$ and $B/Y$ and the **smaller** time wins.

The important modelling decision is that time is **continuous**, not rounded up to whole minutes. Sample case 4 is built to expose this: $A=3, X=2$ gives Chef $1.5$ minutes while $B=2, Y=1$ gives Chefina $2$. Rounding each up to whole minutes would make both $2$ and wrongly print `Both`; the expected answer is `Chef`.

So compare the fractions directly. Both speeds are at least $1$, so multiplying through by the positive quantity $XY$ is safe and gives an exact integer comparison:

$$A \cdot Y \quad\text{versus}\quad B \cdot X$$

Chef is faster when $A \cdot Y < B \cdot X$. Note the cross-pairing — Chef's distance with Chefina's speed — and note too that the inequality points the opposite way from the speed-comparison problems: here a smaller value is better, because this is a time, not a rate.

Floats would mostly work at these bounds but make the tie in sample case 1 a matter of luck; the integer form decides equality exactly.

## Edge cases

- **A tie** ($A = B$, $X = Y$): `Both`, so the equality branch is needed.
- **Time is not rounded to whole minutes.** The sample's last row has Chef at $3/2 = 1.5$ against Chefina at $2$; rounding Chef up to $2$ turns a win into a tie. Cross-multiplication keeps the fractional comparison exact without ever forming a float.
- **The smaller time wins**, which is the opposite direction to a speed comparison — it is easy to invert by reflex.
- **No overflow**: the products are at most $100 \times 10 = 1000$.
- Only the ratios matter, so very different pairs can tie.

## Dry run

| $A$ | $B$ | $X$ | $Y$ | Chef $A \cdot Y$ | Chefina $B \cdot X$ | faster | output |
|---:|---:|---:|---:|---:|---:|---|---|
| 2 | 2 | 2 | 2 | 4 | 4 | neither | `Both` |
| 4 | 2 | 1 | 5 | 20 | 2 | Chefina | `Chefina` |
| 3 | 2 | 4 | 1 | 3 | 8 | Chef | `Chef` |
| 3 | 2 | 2 | 1 | 3 | 4 | Chef | `Chef` |

Row 4 is the fractional case: $1.5$ against $2$.
