---
topic: Number Theory
subtopic: Divisor pairs under a box constraint
time: $O(\sqrt{c})$ per test case
space: $O(1)$
---
Every pixel of the painted rectangle gets a different colour and all $c$ colours are used, so an $x \times y$ section is paintable exactly when it has $c$ pixels and fits on the screen:

$$x \cdot y = c, \qquad x \leq n, \qquad y \leq m$$

So the question is how many **divisor pairs** of $c$ fit inside the $n \times m$ box. Orientation is fixed, so $(x,y)$ and $(y,x)$ are counted separately whenever both fit — the asymmetry of the box is the whole point.

Enumerate divisors up to $\sqrt{c}$. Each divisor $d \leq \sqrt{c}$ yields the pair $(d, c/d)$, and its partner $(c/d, d)$ unless $d^2 = c$, in which case the two coincide and must be counted once. Both are tested against the box independently.

$$\text{answer} = \#\{d \mid c : d \leq n \text{ and } c/d \leq m\}$$

At $\sqrt{10^6} = 1000$ iterations per test and $T \leq 100$, this is trivial — far better than scanning all $x \leq n$ with $n$ up to $10^6$.

The samples show both outcomes. With $n = 4, m = 6, c = 12$ the fitting pairs are $(2,6)$, $(3,4)$ and $(4,3)$, giving $3$; $(1,12)$ is too wide and $(6,2)$, $(12,1)$ too tall. With $n = m = 3$ and $c = 10$, the divisors of $10$ are $1, 2, 5, 10$ and every pair needs a side of at least $5$, so nothing fits and the answer is $0$ — note that a screen having $9 \geq c$ is not enough on its own.

## Edge cases

- **Both orientations are distinct sections.** The first row's answer of $3$ is $2 \times 6$, $3 \times 4$ and $4 \times 3$ — the same divisor pair $\{3, 4\}$ counted twice, once each way.
- **A square section must not be double-counted**, which the `other != d` guard handles; at $c = 1$ the single $1 \times 1$ section is counted once.
- **An orientation can fit while its mirror does not.** $2 \times 6$ fits in $4 \times 6$ but $6 \times 2$ does not, since $6 > n = 4$ — so each orientation needs its own pair of comparisons.
- **No valid section** (the second row): $0$.
- **$c$ may exceed $n \cdot m$**, in which case nothing fits and the loop finds nothing.
- **The loop to $\mathrm{isqrt}(c)$ visits each divisor pair exactly once**, which keeps the work at $10^3$ per case for $c \leq 10^6$.

## Dry run

First sample: $n = 4$, $m = 6$, $c = 12$.

| $d$ | $c/d$ | $d \times (c/d)$ fits $4 \times 6$? | mirror fits? | running count |
|---:|---:|:---:|:---:|---:|
| 1 | 12 | no ($12 > 6$) | no ($12 > 4$) | 0 |
| 2 | 6 | **yes** | no ($6 > 4$) | 1 |
| 3 | 4 | **yes** | **yes** | 3 |

Output `3`.
