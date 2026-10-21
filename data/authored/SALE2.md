---
topic: Basic Math
subtopic: Counting free items in a repeating group
time: $O(1)$ per test case
space: $O(1)$
---
Items come in blocks of three: pay for two, get the third free. Out of $N$ items, the number that are free is the number of complete blocks, $\lfloor N/3 \rfloor$, so the bill is

$$\left(N - \left\lfloor \frac{N}{3} \right\rfloor\right) \cdot X$$

This is the same structure as the Presents problem, with a block of three instead of five.

The phrase "at least $N$ items" invites a worry: could buying *more* than $N$ ever be cheaper? It cannot be cheaper, though it can tie. With $N = 5$ the formula charges for $4$ items; buying $6$ also charges for $4$ and yields an extra item for free. Since the question asks only for the money spent, both give $4X$ and the formula is already optimal. Rounding $N$ up to the next multiple of three before applying the discount would be wrong in the other direction — for $N = 4$ it would charge for $4$ rather than $3$.

The samples check both residues. $N = 3$ gives one free item, paying for $2$; $N = 4$ still gives one free, paying for $3$; $N = 6$ gives two free, paying for $4$. The free count advances only on complete blocks, which is exactly what the floor expresses.

Multiplying by $X$ at the end keeps everything in integers — the per-item price never participates in the rounding.

## Edge cases

- **Exactly one block** ($N = 3$): one item free, two paid.
- **$N = 4$ and $N = 5$**: still only one free, since a partial block earns nothing — both sample rows confirm the step does not move until $N = 6$.
- **$N = 6$**: two free.
- **$N = 1$ or $2$**: nothing free.
- The price multiplies only *after* counting paid items; multiplying first and then discounting would need the same division anyway.

## Dry run

| $N$ | free $N//3$ | paid | $X$ | total | output |
|---:|---:|---:|---:|---:|---|
| 3 | 1 | 2 | 4 | 8 | `8` |
| 4 | 1 | 3 | 2 | 6 | `6` |
| 5 | 1 | 4 | 3 | 12 | `12` |
| 6 | 2 | 4 | 1 | 4 | `4` |

Rows 2 and 3 show the free count stalling at one across $N = 4, 5$.
