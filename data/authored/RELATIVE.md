---
topic: Basic Math
subtopic: Rearranging a given formula
time: $O(1)$ per test case
space: $O(1)$
---
The problem hands over the relation $v^2 = 2gH$ and asks for the height at which the falling speed reaches $c$. Substituting $v = c$ and solving for $H$:

$$H = \frac{c^2}{2g}$$

That is the entire problem — the physics is supplied, so the work is purely algebraic rearrangement.

The constraint that **$2g$ divides $c^2$** is what makes the answer an exact integer, as the statement promises. That guarantee is why `c * c // (2 * g)` is safe: the division leaves no remainder, so integer division loses nothing. Without it, the answer would need a rounding rule and the problem would have to say which way.

Using floating point here would be the needless risk. With $c$ up to $3000$, $c^2$ reaches $9 \times 10^6$ and the quotient stays small, so a float would in fact be exact — but integer arithmetic makes that reasoning unnecessary, and the habit matters once values grow past $2^{53}$.

Checking sample 1: $c^2 = 1400^2 = 1{,}960{,}000$ and $2g = 14$, giving $140{,}000$ metres.

The relativity framing is a joke, of course — a real object cannot reach the speed of light, and the Newtonian formula would not apply anywhere near it. The tags mark this as a "Special" problem for that reason, but the computation is unaffected.

## Edge cases

- **$2g$ is guaranteed to divide $c^2$**, so the division is exact and no rounding decision arises. Without that guarantee the problem would have to say which way to round.
- **$g = 1$**: the height is $c^2/2$.
- **Largest $c$** ($3000$): $c^2 = 9 \times 10^6$, comfortably in range.
- **The rearrangement is the whole content.** From $v^2 = 2gH$ with $v = c$ the answer is $H = c^2/(2g)$; multiplying instead of dividing, or forgetting the factor of $2$, gives a plausible-looking but wrong number — and the sample's last two rows differ only in $g$, which catches it.

## Dry run

| $g$ | $c$ | $c^2$ | $2g$ | $c^2/(2g)$ | output |
|---:|---:|---:|---:|---:|---|
| 7 | 1400 | 1960000 | 14 | 140000 | `140000` |
| 5 | 1000 | 1000000 | 10 | 100000 | `100000` |
| 10 | 1000 | 1000000 | 20 | 50000 | `50000` |

Rows 2 and 3 share $c$ and differ only through $g$.
