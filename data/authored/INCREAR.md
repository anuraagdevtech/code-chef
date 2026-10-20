---
topic: Basic Math
subtopic: Asymmetric step sizes
time: $O(1)$ per test case
space: $O(1)$
---
The two moves are not symmetric: $X$ grows by $1$, $Y$ grows by $2$, and neither can decrease. That asymmetry splits the problem into cases.

**$X \leq Y$.** Raising $Y$ only widens the gap, so the only sensible move is to raise $X$, one step at a time: $Y - X$ operations. Sample cases 1 and 5 are this shape.

**$X > Y$.** Now $Y$ must catch up across a gap $d = X - Y$, in steps of $2$. If $d$ is even that is $d/2$ moves and nothing else is needed — sample case 3, with $d = 4$ and answer $2$.

If $d$ is **odd**, steps of $2$ can never close an odd gap alone, so $X$ must be nudged too. Raising $Y$ by $2k$ and $X$ by $m$ requires $m = 2k - d$, with total cost $m + k = 3k - d$. Minimising means taking the smallest valid $k = \lceil d/2 \rceil = \frac{d+1}{2}$, giving

$$\frac{3(d+1)}{2} - d = \frac{d+3}{2}$$

Sample case 4 is exactly this: $d = 3$ costs $3$ moves — two steps of $+2$ on $Y$ and one $+1$ on $X$, meeting at $6$. The naive reading, $\lceil d/2 \rceil = 2$, is wrong, and that case is in the samples to catch it.

The parity of the gap is what this problem is really testing: a step of size $2$ preserves parity, so an odd difference cannot be closed without involving the step of size $1$.
