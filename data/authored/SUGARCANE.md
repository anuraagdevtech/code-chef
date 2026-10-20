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
