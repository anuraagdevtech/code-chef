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
