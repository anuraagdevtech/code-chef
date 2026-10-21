---
topic: Arrays
subtopic: Sign of a product from the count of negatives
time: $O(N)$ per test case
space: $O(1)$
---
The sign of a product depends only on how many negative factors it has — and on whether any factor is zero. So the array falls into three cases:

**Contains a zero.** The product is $0$, which is non-negative. Remove nothing: answer $0$. Sample case 3 is this, and it is the case most easily missed, because the array also has an odd number of negatives and would otherwise look like it needs a removal.

**Even number of negatives, no zero.** The negatives pair up and the product is positive. Answer $0$ — samples 1 and 4.

**Odd number of negatives, no zero.** The product is negative. Removing a single negative element flips the count to even and fixes it, so the answer is $1$ — sample 2. One removal is clearly minimal, since removing nothing leaves it negative.

The check order matters: the zero test must come **first**, because a zero overrides the parity entirely. Counting negatives and branching on parity alone fails sample case 3.

Only two cheap scans are needed — whether any element is zero and how many are negative — so this is $O(N)$ time and $O(1)$ space. The product itself is never computed, which is just as well: with $N$ up to $10^4$ and values to $1000$, it would be an astronomically large number, and in a fixed-width language it would overflow long before telling you its sign.

## Edge cases

- **A zero overrides the parity.** The third row has one negative *and* a zero: the product is already $0$, which is non-negative, so the answer is $0$ operations. A solution that only counts negatives answers $1$ there, which is why the zero test must come first.
- **An even number of negatives** (the fourth row, two of them): already non-negative, so $0$.
- **An odd number of negatives** (the second row, one): a single sign flip, so $1$.
- **No negatives at all** (the first row): $0$.
- The answer is therefore only ever $0$ or $1$ — one flip always suffices to fix the sign.

## Dry run

| array | contains $0$? | negatives | parity | output |
|---|:---:|---:|---|---|
| $1, 9, 8$ | no | 0 | even | `0` |
| $2, -1, 9, 100$ | no | 1 | odd | `1` |
| $2, -1, 0, 100$ | **yes** | — | — | `0` |
| $2, -1, -1, 100$ | no | 2 | even | `0` |

Row 3 short-circuits on the zero before the parity is ever considered.
