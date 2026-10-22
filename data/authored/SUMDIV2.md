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

## Edge cases

- **$N = XY - X - Y$ solves both congruences at once**: $N + Y = X(Y-1)$ and $N + X = Y(X-1)$, so each is divisible by the right number — no search or CRT machinery is needed.
- **That value can be negative or zero**, as at $X = Y = 1$ where it is $-1$, so it must be shifted into range by reducing modulo $\operatorname{lcm}(X,Y)$ — the period of the solution set.
- **A remainder of $0$ maps to the lcm**, since $N \geq 1$ is required.
- **The lcm must be built as `x // gcd * y`**, dividing first; the product $XY$ reaches $10^{18}$, exact in Python but an overflow in a 64-bit language.
- **$N \leq 10^{18}$ holds**, because the answer is at most $\operatorname{lcm}(X,Y) \leq XY \leq 10^{18}$.
- **Minimisation is explicitly not required**, which is why the reduced representative is fine even though the sample prints a different one.
- **This answer differs from the sample's** at every row (for $18, 42$ it prints $66$ against $192$), and a special judge checks the two divisibility conditions.

## Dry run

First sample: $X = 18$, $Y = 42$.

| step | value |
|---|---:|
| $XY - X - Y$ | $756 - 60 = 696$ |
| $\operatorname{lcm}(18, 42)$ | 126 |
| $696 \bmod 126$ | 66 |

Check $N = 66$: $66 + 42 = 108 = 6 \cdot 18$ ✓ and $66 + 18 = 84 = 2 \cdot 42$ ✓
