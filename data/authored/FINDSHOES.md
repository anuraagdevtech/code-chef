---
topic: Basic Math
subtopic: Clamping one side of a two-part requirement
time: $O(1)$ per test case
space: $O(1)$
---
Each of the $N$ friends needs a *pair*, so Chef must end up with $N$ left shoes and $N$ right shoes. He already holds $M$ left shoes and no right shoes at all.

The two sides are accounted for separately:

- **Right shoes:** he has none, so he must buy all $N$.
- **Left shoes:** he must buy the shortfall $N - M$, but only if it is positive — surplus left shoes are useless and cannot be converted.

So the answer is

$$N + \max(0,\; N - M)$$

The clamp is the whole difficulty. Sample case 1 has $N = 2$ and $M = 4$: two spare left shoes that help with nothing, so the answer is $2 + 0 = 2$, not $2 + (2 - 4) = 0$. Without `max(0, ...)` the surplus would subtract from the right-shoe count, which is nonsense — a left shoe is not a right shoe.

That asymmetry is the lesson. When a requirement has several components and a surplus in one cannot offset a deficit in another, each component must be clamped at zero **before** summing. The same clamp appeared in the candy-packets problem, and here it matters even more because the unclamped version silently produces a plausible-looking number.

Case 2 ($N = 6$, $M = 0$) is the no-stock extreme: $6 + 6 = 12$ shoes, a full pair for everyone.

## Edge cases

- **More spares than needed** ($N = 2$, $M = 4$): the two surplus shoes are useless, so the clamp is essential — without `max(0, ...)` the shortfall is $-2$ and the answer comes out as $0$ instead of $2$. The sample's first row is this case.
- **No spares at all** ($M = 0$): every shoe must be bought, so $2N$. The sample's second row.
- **Exactly enough spares** ($M = N$): only the other $N$ shoes are needed.
- **The two sides are asymmetric**: all $N$ of one kind must be bought no matter what, and only the other kind benefits from existing stock, which is why the expression is $N + \max(0, N - M)$ rather than symmetric in $M$.

## Dry run

| $N$ | $M$ (spares) | shortfall $N - M$ | clamped | total $N + {\cdot}$ | output |
|---:|---:|---:|---:|---:|---|
| 2 | 4 | $-2$ | 0 | 2 | `2` |
| 6 | 0 | 6 | 6 | 12 | `12` |
| 4 | 3 | 1 | 1 | 5 | `5` |

Row 1 is the one the clamp exists for.
