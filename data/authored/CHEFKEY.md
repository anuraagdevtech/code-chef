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
