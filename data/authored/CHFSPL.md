---
topic: Basic Math
subtopic: Total minus the extremum
time: $O(1)$ per test case
space: $O(1)$
---
Chef casts exactly two of the three spells and wants the largest total, so he drops the weakest:

$$A + B + C - \min(A, B, C)$$

Phrasing it as "total minus the minimum" rather than "sum of the two largest" keeps it to two cheap passes and avoids sorting or a top-two scan. It is the same shape as the discus and sale problems, and it generalises directly to picking $n-1$ of $n$ items.

Ties need no special handling: `min` returns the value once, so if two spells share the lowest power only one copy is dropped. With powers $5, 5, 9$ the answer is $14$, not $9$.

Note the word **exactly** — Chef must use two spells, not "at most two". Since all powers are positive that distinction never bites here, because using more is always better. It would matter if negative powers were allowed, where the best "at most two" choice might be to cast nothing.

Sample case 1 drops the $2$ from $\{4, 2, 8\}$ for $12$; case 2 drops the $10$ for $32$.

Powers reach $10^8$, so the sum of two reaches $2 \times 10^8$ — inside 32 bits, but worth a glance in a fixed-width language.

## Edge cases

- **Two tied for weakest**: only one is dropped, so the total loses a single copy.
- **All three equal**: the answer is twice the value.
- **The weakest is discarded, not the strongest** — exactly two of the three spells are used, so inverting that gives $\text{sum} - \max$ and a much smaller answer.
- **Largest inputs** ($10^8$ each): the sum reaches $3 \times 10^8$, still inside 32-bit range but worth noting.

## Dry run

| spells | total | weakest | total $-$ min | output |
|---|---:|---:|---:|---|
| $4, 2, 8$ | 14 | 2 | 12 | `12` |
| $10, 14, 18$ | 42 | 10 | 32 | `32` |
