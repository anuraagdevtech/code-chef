---
topic: Basic Math
subtopic: Factoring a repeated difference
time: $O(1)$ per test case
space: $O(1)$
---
Chef bought $X$ stocks at $Y$ each and sells all of them at $Z$ each, so

$$\text{profit} = XZ - XY = X(Z - Y)$$

Factoring out $X$ is the small simplification worth making: it computes the per-unit margin once and scales it, rather than forming two large products and subtracting. The two forms agree exactly in integer arithmetic, but the factored version makes the structure obvious — profit is margin times volume.

The constraints guarantee $Y \leq Z$, so the margin is never negative and the answer is never a loss. Without that promise the formula would still be correct, just capable of returning a negative number, and no clamping would be appropriate since a loss is a real outcome.

Sample case 1 is the large-margin case: $2$ stocks bought at $5$ and sold at $20$ gives $2 \times 15 = 30$. Cases 2 and 3 both have a margin of exactly $1$, so the profit is simply the share count.

On magnitudes: $X$ and $Z$ each reach $10^4$, so the product stays at $10^8$ — comfortably inside 32 bits, though worth noting for a C implementation that computes `x * z` before subtracting.

## Edge cases

- **Selling at cost** ($Y = Z$): the margin is zero, so the profit is $0$ — the constraint $Y \leq Z$ allows this.
- **$Y \leq Z$ is guaranteed**, so the profit is never negative and no clamp is needed.
- **A margin of one** (the last two sample rows): the answer is just the share count.
- **Largest inputs** ($X = 10^4$ with a margin of $10^4 - 1$): close to $10^8$, inside 32-bit range but worth noting.
- Factoring as $X(Z-Y)$ is one multiplication rather than the two of $XZ - XY$, and keeps the intermediate values small.

## Dry run

| $X$ (shares) | $Y$ (bought at) | $Z$ (sold at) | margin $Z-Y$ | profit $X \cdot {\cdot}$ | output |
|---:|---:|---:|---:|---:|---|
| 2 | 5 | 20 | 15 | 30 | `30` |
| 3 | 1 | 2 | 1 | 3 | `3` |
| 4 | 5 | 6 | 1 | 4 | `4` |
