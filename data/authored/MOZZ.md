---
topic: Basic Math
subtopic: Inverting a reward, then a ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
Two steps, run in sequence.

**Recover the sticks eaten.** Chef is paid $30$ rupees for each stick beyond $X$, so $R$ rupees means $R/30$ extra sticks and a total of

$$S = X + \frac{R}{30}$$

The guarantee that $R$ is a multiple of $30$ makes this exact. Note that $R = 0$ does not mean Chef ate nothing — it means he ate no *extra*, so $S = X$, which is the most he could have eaten without earning anything. Sample case 2 is exactly this, with $S = 16$.

**Convert sticks to plates.** Plates hold $Y$ sticks, and the rules say Chef finishes each plate before ordering the next but may leave the **final** plate unfinished. The question asks for the *maximum* possible number of plates, so assume he abandoned the last one after a single stick:

$$\left\lceil \frac{S}{Y} \right\rceil$$

The "maximum" wording is what makes this a ceiling. Were the question the minimum number of plates, the answer would be the same ceiling for a different reason — but here the subtlety is that any partially eaten plate still counts as ordered, which is precisely what rounding up expresses.

Sample case 3 shows it: $S = 15 + 4 = 19$ sticks at $9$ per plate means two full plates and one stick from a third, so $3$ plates.

## Edge cases

- **No reward sticks** ($R = 0$): the order is just $X$ sticks. The sample's second row.
- **$R$ is guaranteed a multiple of $30$**, so $R/30$ is exact and no part-earned stick is stranded.
- **The last plate may be left unfinished but was still ordered**, so the division rounds *up*. The sample's first and third rows both have a part-used final plate.
- **$Y = 1$** (one stick per plate): the plate count equals the stick count, as in the last sample row with $94$.
- **An exact fit** (stick count a multiple of $Y$): no extra plate, which is what the $+Y-1$ form has to avoid adding.

## Dry run

| $X$ | $Y$ | $R$ | reward sticks $R/30$ | total sticks | plates $\lceil \cdot / Y \rceil$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 7 | 5 | 30 | 1 | 8 | 2 | `2` |
| 16 | 5 | 0 | 0 | 16 | 4 | `4` |
| 15 | 9 | 120 | 4 | 19 | 3 | `3` |
| 23 | 1 | 2130 | 71 | 94 | 94 | `94` |

Row 2 has no reward at all; row 4 has one stick per plate.
