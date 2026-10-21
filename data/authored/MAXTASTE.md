---
topic: Greedy
subtopic: Independent choices optimised separately
time: $O(1)$ per test case
space: $O(1)$
---
The dish takes one ingredient from $\{A, B\}$ and one from $\{C, D\}$, and its tastiness is the sum of the two. There are only four combinations, so brute force works — but the structure is worth naming, because it generalises.

The two choices are **independent**: picking $A$ over $B$ places no restriction on whether $C$ or $D$ may be used. When a total is a sum of independent parts, maximising the whole is the same as maximising each part on its own. So

$$\max \text{tastiness} = \max(a, b) + \max(c, d)$$

This is the simplest possible greedy argument, and the reason it is valid is exactly the independence. The moment a constraint couples the choices — say, two ingredients that cannot be combined — the decomposition breaks and the four cases must genuinely be compared. Recognising when choices separate is what turns an exponential search into a linear one in larger problems.

Checking sample case 2: $\max(16, 15) + \max(5, 4) = 16 + 5 = 21$.

Note that the first ingredient must come from the first pair — Chef cannot take both $A$ and $B$. Reading it as "pick the two tastiest of the four" would give $16 + 15 = 31$ here, which is wrong.

## Edge cases

- **The two largest values in the same pair** is the trap, and the sample's second row is it: $16, 15, 5, 4$ has $16$ and $15$ as the two biggest overall, but both come from the first pair, so only one may be taken and the answer is $16 + 5 = 21$, not $31$. Sorting all four and adding the top two is wrong.
- **A tie inside a pair** ($a = b$): either choice gives the same total, so no tie-break is needed.
- **All four equal**: the answer is twice that value.
- The two picks are genuinely independent — one from each pair — which is why maximising them separately is optimal rather than merely convenient.

## Dry run

| $a$ | $b$ | $c$ | $d$ | $\max(a,b)$ | $\max(c,d)$ | total | output |
|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 5 | 6 | 2 | 5 | 6 | 11 | `11` |
| 16 | 15 | 5 | 4 | 16 | 5 | 21 | `21` |

Row 2 shows $15$ going unused despite being the second largest value present.
