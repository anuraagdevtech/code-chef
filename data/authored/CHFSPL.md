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
