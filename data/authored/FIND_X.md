---
topic: Number Theory
subtopic: Shared remainder forces a multiple of the LCM
time: $O(\log \min(B,D))$ per test case
space: $O(1)$
---
Let $r = A \bmod B = C \bmod D$. Since $(A + X) \bmod B = (r + X) \bmod B$ and likewise for $D$, substituting $Y = r + X$ reduces the whole problem to

$$Y \bmod B = Y \bmod D$$

Call that common remainder $m$. Then $m < B$ and $m < D$, so $m < \min(B, D)$, and $Y - m$ is divisible by both $B$ and $D$, hence by $L = \mathrm{lcm}(B, D)$. Since $m < \min(B,D) \leq L$, this says exactly

$$Y \bmod L < \min(B, D)$$

So the valid $Y$ form a short window at the start of each multiple of $L$. Note $r$ itself is valid (it is below both moduli), which is the given $X = 0$ — and we need $X > 0$, i.e. the *next* valid $Y$ above $r$:

- if $r + 1 < \min(B, D)$, then $Y = r+1$ is still inside the window, so $X = 1$;
- otherwise $r$ is the last value in the window, and the next window starts at $Y = L$, giving $X = L - r$.

Those are the only two possibilities, which is why no search is needed. Note $L$ can reach $10^{18}$, so computing it as $B / \gcd(B,D) \cdot D$ matters in C++; Python is unbounded.

The samples hit both branches. $A{=}4, B{=}7, C{=}4, D{=}8$ has $r = 4 < 6 = \min - 1$, so $X = 1$. $A{=}5, B{=}1, C{=}8, D{=}2$ has $\min(B,D) = 1$ and $r = 0$, so the window is only $\{0\}$ and $X = \mathrm{lcm}(1,2) - 0 = 2$. And $A{=}3, B{=}2, C{=}4, D{=}3$ has $r = 1 = \min(B,D) - 1$, giving $X = 6 - 1 = 5$.
