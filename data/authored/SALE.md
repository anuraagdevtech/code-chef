---
topic: Basic Math
subtopic: Total minus the extremum
time: $O(1)$ per test case
space: $O(1)$
---
Three items are bought and the cheapest is free, so Chef pays for the other two:

$$A + B + C - \min(A, B, C)$$

Expressing it as "total minus the minimum" rather than "sum of the two largest" is the move worth internalising. Both are correct, but the subtraction form needs only two passes over the values — one to add, one to find the minimum — and it extends unchanged to $n$ items with the cheapest free, whereas "add the two largest" would need a sort or a running top-two.

Ties are handled correctly without any special case. Sample case 2 has three items priced $3$; exactly one of them is free, so the answer is $6$ rather than $3$ or $9$. `min` returns the value, not every element equal to it, so only one copy is deducted. The same applies to sample case 3, where two items share the lowest price of $4$ and only one is discounted, giving $8 + 4 = 12$.

That subtlety — *one* free item, even when several are tied for cheapest — is where an approach built on filtering out the minimum value would go wrong, since it would remove both $4$s and answer $8$.

## Edge cases

- **Several items tie for cheapest** ($3, 3, 3$ and $8, 4, 4$): **exactly one** item is free, so only a single minimum is subtracted. Removing every tied minimum would give $3$ and $8$ instead of $6$ and $12$, and both sample rows test this.
- **All three prices equal**: the answer is twice the price.
- **The cheapest item in any position** — first, middle or last — must be found, so a hard-coded position fails.
- The answer is the total minus one extremum, which is why no sorting is needed.

## Dry run

| prices | total | cheapest | total $-$ min | output |
|---|---:|---:|---:|---|
| $6, 2, 4$ | 12 | 2 | 10 | `10` |
| $3, 3, 3$ | 9 | 3 | 6 | `6` |
| $8, 4, 4$ | 16 | 4 | 12 | `12` |

Rows 2 and 3 have ties for cheapest, and only one copy is discounted.
