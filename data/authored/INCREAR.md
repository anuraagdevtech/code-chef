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

## Edge cases

- **Already equal** ($5, 5$): zero operations.
- **$X < Y$**: only the $+1$ move narrows the gap, so it costs $Y - X$ operations — one per unit, which can be the dearer direction in absolute terms even though each step is "cheaper".
- **$X > Y$ with an even gap** ($7, 3$: gap $4$): exactly $\text{gap}/2$ steps of $+2$.
- **$X > Y$ with an odd gap** ($5, 2$: gap $3$) costs **three**, not two. The $+2$ steps preserve the gap's parity, so an odd gap can never be closed by them alone: two $+2$ steps overshoot to a gap of $1$ the other way, and a $+1$ then settles it. The formula $(d+3)/2$ encodes those two extra moves, and the sample's fourth row is the case that catches $(d+1)/2$.

## Dry run

| $X$ | $Y$ | direction | gap | reasoning | output |
|---:|---:|---|---:|---|---|
| 3 | 4 | $X < Y$ | 1 | one $+1$ on $X$ | `1` |
| 5 | 5 | equal | 0 | nothing to do | `0` |
| 7 | 3 | $X > Y$ | 4 | two $+2$ on $Y$ | `2` |
| 5 | 2 | $X > Y$ | 3 | odd gap: two $+2$ then one $+1$ | `3` |
| 7 | 12 | $X < Y$ | 5 | five $+1$ on $X$ | `5` |

Row 4 is the parity case that costs an extra move.
