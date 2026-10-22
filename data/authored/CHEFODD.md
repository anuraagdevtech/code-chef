---
topic: Number Theory
subtopic: Parity and capacity constraints together
time: $O(1)$ per test case
space: $O(1)$
---
Two independent requirements must both hold.

**Capacity.** Every part needs at least $2$ elements, so $K$ parts consume at least $2K$ of the $N$ available:

$$N \geq 2K$$

**Parity.** A subset has an odd sum exactly when it contains an **odd number of odd elements**. The set $\{1, \ldots, N\}$ contains $O = \lceil N/2 \rceil$ odd numbers, and each of the $K$ parts must take an odd count of them. Summing $K$ odd numbers gives a total with the same parity as $K$, so

$$O \equiv K \pmod 2$$

Those two conditions are also sufficient. Give each part one odd number — possible since $N \geq 2K$ forces $O \geq K$ — then the remaining $O - K$ odds are even in number and can be handed out two at a time without disturbing any part's parity. The evens are unconstrained and fill the parts up to size $2$.

Sample case 1 fails the parity test: $N = 5$ has $O = 3$ odd numbers against $K = 2$ parts, and $3 \not\equiv 2 \pmod 2$. The capacity is fine ($5 \geq 4$), so a solution checking only sizes would wrongly say yes.

Sample case 2 passes both: $N = 14$ gives $O = 7 \equiv 5 \pmod 2$, and $14 \geq 10$.

Note the parity condition is equivalent to saying the total $\frac{N(N+1)}{2}$ has the same parity as $K$ — the evens contribute nothing, so the grand total's parity is just $O \bmod 2$.

With $N, K$ up to $10^{18}$, only this $O(1)$ test is viable; $2K$ can reach $2 \times 10^{18}$, which still fits a 64-bit signed integer but only just.

## Edge cases

- **Two independent necessary conditions**, and both must be checked. Each part needs at least two elements, so $N \geq 2K$; and each part needs an odd number of odd elements, so the total count of odds must match $K$ in parity.
- **The parity condition is what fails the first row.** $N = 5$ has three odd numbers and $K = 2$: three odd counts cannot be split into two odd pieces, since a sum of two odd numbers is even.
- **The size condition is independent** — $N = 5$ with $K = 3$ would fail on $5 < 6$ instead, even though $3$ and $3$ agree in parity.
- **The odd count is $\lceil N/2 \rceil$**, so it is $(N+1)/2$ for odd $N$ and $N/2$ for even $N$; writing $N/2$ throughout breaks every odd case.
- **Even elements are free padding**, which is why they never enter the conditions: they can be distributed anywhere without affecting any sum's parity.
- **$N$ up to $10^{18}$** demands exact integer arithmetic, with no floating-point halving.

## Dry run

| $N$ | $K$ | odds $\lceil N/2 \rceil$ | $N \geq 2K$? | parity match? | output |
|---:|---:|---:|:---:|:---:|---|
| 5 | 2 | 3 | $5 \geq 4$ ✓ | $3$ odd vs $2$ even **✗** | `NO` |
| 14 | 5 | 7 | $14 \geq 10$ ✓ | $7$ odd, $5$ odd ✓ | `YES` |

For the second row, the seven odds split across five parts with an odd count each — for instance $1 + 1 + 1 + 1 + 3 = 7$ — and the seven evens pad the parts out to size $2$ or more.
