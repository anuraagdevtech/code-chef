---
topic: Number Theory
subtopic: Simultaneous congruences solved by inspection
time: $O(\log \min(X,Y))$ per test case
space: $O(1)$
---
The two divisibility conditions are congruences:

$$N \equiv -Y \pmod X, \qquad N \equiv -X \pmod Y$$

One solution can be read off directly: $N = XY - X - Y$. Reducing mod $X$, both $XY$ and $X$ vanish and $-Y$ remains; reducing mod $Y$, both $XY$ and $Y$ vanish and $-X$ remains. So the conditions are consistent and the solution set is the full arithmetic progression

$$XY - X - Y + t \cdot \mathrm{lcm}(X, Y)$$

since adding the LCM preserves both congruences.

That progression is what fixes the two range problems. $XY - X - Y$ can be non-positive — it is $-1$ for $X = Y = 1$ and $0$ for $X = Y = 2$ — so reduce it modulo $L = \mathrm{lcm}(X,Y)$ into $[0, L)$ and, if the result is $0$, step up to $L$ itself. The answer is then the smallest positive solution, which is at most $L \leq XY \leq 10^{18}$ and so always in range.

Computing the LCM as $X/\gcd(X,Y) \cdot Y$ keeps the intermediate value from exceeding the bound.

Any answer is accepted. For $X = 18, Y = 42$ the LCM is $126$ and $XY - X - Y = 696$ reduces to $66$: indeed $66 + 42 = 108 = 6 \cdot 18$ and $66 + 18 = 84 = 2 \cdot 42$. The sample's $192$ is $66 + 126$, the next term of the same progression. For $X = Y = 1$ the reduction gives $0$, so we print $1$.
