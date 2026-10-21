---
topic: Basic Math
subtopic: Independent requirements summed
time: $O(1)$ per test case
space: $O(1)$
---
Type A coconuts supply only water and type B supply only pulp, so the two requirements are completely **independent** — neither type can help with the other's quota. Chef needs

$$\frac{X_a}{x_a} + \frac{X_b}{x_b}$$

coconuts in total.

The constraints promise that $x_a$ divides $X_a$ and $x_b$ divides $X_b$, so both divisions are exact and no rounding question arises. That guarantee is doing real work: without it each term would need a ceiling, since a partial coconut cannot be bought, and the answer would be larger.

Because the two types are disjoint in what they provide, there is no optimisation to perform — no trade-off, no minimum to search for. Summing the two independently computed counts is the whole solution. This is the same "independent components" idea as the shoes problem, minus the clamping, because here neither side can overshoot and spill into the other.

Sample case 2 is a good check that the two divisions must be kept separate: $1000/100 = 10$ and $1350/450 = 3$, giving $13$. Mixing the quantities — dividing total volume by total capacity, say — would produce nonsense, because millilitres of water and grams of pulp are not the same unit.

## Edge cases

- **Both divisions are guaranteed exact** ($x_a$ divides $X_a$ and $x_b$ divides $X_b$), so no rounding decision arises. Without that guarantee each would need a ceiling, since a part-used coconut still has to be bought.
- **The two requirements are independent**: water and pulp come from different coconuts, so the counts *add*. Taking the maximum — as one would for two demands met from the same source — under-orders.
- **The same total from different splits**: the first two sample rows both answer $13$ through different numbers.
- The bounds keep every quantity positive, so neither term can vanish.

## Dry run

| $x_a$ | $x_b$ | $X_a$ | $X_b$ | for water $X_a/x_a$ | for pulp $X_b/x_b$ | total | output |
|---:|---:|---:|---:|---:|---:|---:|---|
| 100 | 400 | 1000 | 1200 | 10 | 3 | 13 | `13` |
| 100 | 450 | 1000 | 1350 | 10 | 3 | 13 | `13` |
| 150 | 400 | 1200 | 1200 | 8 | 3 | 11 | `11` |
