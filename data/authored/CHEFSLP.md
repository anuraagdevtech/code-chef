---
topic: Basic Math
subtopic: Pairing limited by the scarcer side
time: $O(1)$ per test case
space: $O(1)$
---
Of the $N$ slippers, $L$ are left and the remaining $N - L$ are right. A sellable pair needs one of each, so the number of pairs is limited by whichever side is scarcer:

$$\text{pairs} = \min(L,\; N - L)$$

and the revenue is that count times $X$.

Taking the minimum is the whole idea — surplus slippers on the abundant side are unsellable, exactly as the spare left shoes were useless in the shoes problem. Sample case 4 shows it: $7$ left and $3$ right out of $10$ yields only $3$ pairs, stranding four left slippers.

Sample case 3 is the opposite imbalance, with $10$ left against $990$ right giving $10$ pairs — the small side binds, whichever side it happens to be, which is why `min` is used rather than assuming lefts are scarce.

Two degenerate inputs are inside the constraints and both work without special handling. $N = 0$ gives zero pairs, and $X = 0$ makes the revenue zero regardless of how many pairs exist — sample cases 1 and 2 respectively. Neither needs a guard, but it is worth noticing that a zero answer can arise for two quite different reasons.

## Edge cases

- **No slippers at all** ($N = 0$): zero revenue.
- **A price of zero** ($X = 0$): zero revenue even though pairs exist. The sample's second row.
- **The scarcer side caps the pairs.** The fourth row has $7$ left and $3$ right, so only $3$ pairs sell and the four surplus left shoes are worthless — using $L$ alone would report $7$.
- **All of one kind** ($L = 0$ or $L = N$): no pairs at all.
- **Largest input** ($N = X = 1000$): $500 \times 1000 = 5 \times 10^5$.

## Dry run

| $N$ | $L$ (left) | right $N-L$ | pairs $\min$ | $X$ | output |
|---:|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 0 | 100 | `0` |
| 10 | 1 | 9 | 1 | 0 | `0` |
| 1000 | 10 | 990 | 10 | 1000 | `10000` |
| 10 | 7 | 3 | 3 | 1 | `3` |

Row 4 is limited by the right shoes; row 2 by the price.
