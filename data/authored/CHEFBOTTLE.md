---
topic: Basic Math
subtopic: Two competing limits
time: $O(1)$ per test case
space: $O(1)$
---
Two separate things cap how many bottles Chef can fill, and the answer is whichever binds first.

- **Water:** the tank holds $K$ litres and each full bottle takes $X$, so the water allows $\lfloor K/X \rfloor$ bottles. Partially filled bottles do not count, so this floors.
- **Bottles:** he only owns $N$ of them, however much water is left over.

The answer is therefore

$$\min\left(N,\; \left\lfloor \frac{K}{X} \right\rfloor\right)$$

Taking the minimum of independent caps is the pattern here, and both halves are load-bearing. Sample case 3 is capped by bottles — $4$ litres into $1$-litre bottles could fill four, but Chef has only $3$. Sample case 1 is capped by water: five bottles available, but $8$ litres at $2$ litres each fills only four. Dropping either term fails one of these.

Note that $K$ may be $0$ while $N$ and $X$ are at least $1$, so the answer can legitimately be zero and the division never has a zero divisor. Sample case 2 shows the water running out immediately, with $4$ litres unable to fill even one $5$-litre bottle.
