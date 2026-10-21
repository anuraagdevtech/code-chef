---
topic: Basic Math
subtopic: Percentages that cancel
time: $O(1)$ per test case
space: $O(1)$
---
Selling $N$ glasses at $50$ coins each gives a total income of $50N$. The three costs are all quoted as percentages **of that same income**, which is what makes the problem collapse:

$$20\% + 20\% + 30\% = 70\%$$

So $70\%$ of income is spent and $30\%$ remains as profit:

$$\text{profit} = 0.30 \times 50N = 15N$$

The entire problem is the single expression `15 * n`. The useful habit is to sum the percentage *rates* before touching the money, rather than computing three separate costs and subtracting them one at a time — fewer operations, and no intermediate rounding to worry about.

That rounding point matters here. Because $30\%$ of $50$ is exactly $15$, the profit is always a whole number of coins and integer arithmetic is exact. Had the rate produced a fraction of a coin, the problem would have had to say how to round, and computing `0.3 * 50 * n` in floating point could then drift for large $N$. Sticking to the pre-simplified integer coefficient avoids the issue entirely.

## Edge cases

- **$N = 1$**: $15$ rupees of profit — the per-litre margin itself.
- **Largest input** ($N = 10^6$): $1.5 \times 10^7$, well inside integer range.
- **The percentages cancel exactly.** Income is $50N$ and costs take $20 + 20 + 30 = 70\%$ of it, leaving $30\%$; and $30\%$ of $50$ is exactly $15$, an integer. So no rounding question arises at any $N$. Had the margin not divided evenly, the answer would have to settle whether paise are rounded or truncated.
- There is nothing to clamp: the margin is positive, so the profit never goes negative.

## Dry run

| $N$ | income $50N$ | costs $70\%$ | profit $15N$ | output |
|---:|---:|---:|---:|---:|
| 2 | 100 | 70 | 30 | `30` |
| 4 | 200 | 140 | 60 | `60` |
| 5 | 250 | 175 | 75 | `75` |
| 10 | 500 | 350 | 150 | `150` |

The code jumps straight to the last column; the middle two are only there to show the rate collapsing to $15$.
