---
topic: Basic Math
subtopic: Chaining unit conversions
time: $O(1)$ per test case
space: $O(1)$
---
This is a two-step unit conversion. One kilogram of pulp yields $1000$ pages, and one notebook consumes $100$ pages, so

$$N \text{ kg} \;\longrightarrow\; 1000N \text{ pages} \;\longrightarrow\; \frac{1000N}{100} = 10N \text{ notebooks}$$

The two constants cancel to a single factor of $10$, so the answer is simply `10 * n`.

It is worth noticing *why* no rounding appears. Because $1000$ is an exact multiple of $100$, every kilogram produces a whole number of notebooks and no pages are ever left stranded. Had a notebook taken, say, $300$ pages, the answer would have needed a floor — $\lfloor 1000N / 300 \rfloor$ — since a partial notebook cannot be sold. Spotting that the division is clean is what licenses the simplification.

Chaining the conversion in one expression, rather than computing pages into a variable and dividing afterwards, keeps the arithmetic in integers throughout.

## Edge cases

- **$N = 1$**: one kilogram gives $10$ notebooks, which is the conversion factor itself.
- **Largest input** ($N = 100$): $1000$ notebooks.
- **The two conversions compose exactly.** $1000$ pages per kilogram divided by $100$ pages per notebook is exactly $10$, so no rounding enters anywhere. Had the numbers not divided evenly, the chain would need a floor at the end and *only* at the end — flooring each step separately loses paper.
- Nothing here can be fractional, so there is no ceiling-versus-floor decision to make.

## Dry run

| $N$ (kg) | pages $1000N$ | notebooks $/100$ | output |
|---:|---:|---:|---:|
| 1 | 1000 | 10 | `10` |
| 100 | 100000 | 1000 | `1000` |
| 50 | 50000 | 500 | `500` |

The code folds both steps into the single multiplier $10$.
