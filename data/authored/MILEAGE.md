---
topic: Basic Math
subtopic: Comparing ratios by cross-multiplication
time: $O(1)$ per test case
space: $O(1)$
---
Travelling $N$ kilometres at $A$ km per litre burns $N/A$ litres of petrol at $X$ rupees each, so the two costs are

$$\text{petrol} = \frac{NX}{A}, \qquad \text{diesel} = \frac{NY}{B}$$

The distance $N$ multiplies both sides equally, so it **cancels** — the cheaper fuel is the same whatever the trip length. That leaves

$$\frac{X}{A} \quad\text{versus}\quad \frac{Y}{B}$$

a comparison of cost per kilometre. Multiplying through by the positive quantity $AB$ gives an exact integer test:

$$X \cdot B \quad\text{versus}\quad Y \cdot A$$

with petrol cheaper when $XB < YA$. Note the cross-pairing: petrol's *price* with diesel's *mileage*.

The statement's remark that Chef may buy fractional litres is what licenses this. With fuel sold only in whole litres the costs would involve ceilings, $N$ would stop cancelling, and the clean ratio comparison would break.

Using floats here would be risky precisely because `ANY` is a possible answer — sample case 3 has both sides at $120$, an exact tie that float division might miss. Integer cross-multiplication decides it exactly.

Sample case 4 is a good check on the cross-pairing: $X \cdot B = 81$ against $Y \cdot A = 18$ makes diesel much cheaper, even though the two fuels cost the same per litre, because diesel goes four and a half times further.

## Edge cases

- **A tie** ($3 \times 40 = 15 \times 8 = 120$): `ANY`, so the equality branch is needed. The sample's third row.
- **$N$ cancels out entirely.** Both costs scale with the distance, so it never affects the comparison — and multiplying it in first would needlessly inflate the operands in a fixed-width language.
- **Equal prices, different mileages** (the second row has $x = y = 12$): the mileage alone decides, so comparing prices without mileage is wrong.
- **Cross-multiplication keeps it exact**: comparing $x/a$ against $y/b$ as floats puts the tie row at risk of a rounding error.
- All values are at most $100$, so the products stay tiny.

## Dry run

| $x$ | $y$ | $a$ | $b$ | petrol $x \cdot b$ | diesel $y \cdot a$ | cheaper | output |
|---:|---:|---:|---:|---:|---:|---|---|
| 10 | 8 | 2 | 4 | 40 | 16 | diesel | `DIESEL` |
| 12 | 12 | 4 | 3 | 36 | 48 | petrol | `PETROL` |
| 3 | 15 | 8 | 40 | 120 | 120 | neither | `ANY` |
| 9 | 9 | 2 | 9 | 81 | 18 | diesel | `DIESEL` |

$N$ appears in none of the columns, because it cancels.
