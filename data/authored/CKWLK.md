---
topic: Number Theory
subtopic: Prime factorisation into a two-variable range test
time: $O(\log N)$ per test case
space: $O(1)$
---
Order does not matter, so a sequence of cheats is just a count of each: applying $\times 10$ $a$ times and $\times 20$ $b$ times gives

$$N = 10^a \cdot 20^b = 2^{a + 2b} \cdot 5^{a + b}$$

So $N$ must be $2^x 5^y$ with no other prime factor, and we need non-negative integers $a, b$ with $x = a + 2b$ and $y = a + b$. Subtracting gives $b = x - y$ and then $a = y - b = 2y - x$. Both must be non-negative, which is a single sandwich:

$$y \leq x \leq 2y$$

So the test is: strip every factor of $2$ and of $5$ from $N$; the remainder must be $1$; and the two exponents must satisfy that inequality. The lower bound says there are at least as many $2$s as $5$s (every cheat contributes at least one of each), and the upper bound says no more than twice as many (even using $\times 20$ exclusively).

Both samples that fail do so for different reasons, which is the point of the pair. $90 = 2 \cdot 3^2 \cdot 5$ leaves $9$ behind, so the factorisation itself is wrong. But $1024000000000 = 2^{19} \cdot 5^{9}$ is a clean $2$-$5$ number and still fails, because $19 > 18 = 2y$ — it has one factor of $2$ too many, so no combination of cheats produces it.

Meanwhile $200 = 2^3 \cdot 5^2$ satisfies $2 \leq 3 \leq 4$ (take $a = 1, b = 1$), and $10^{12} = 2^{12} 5^{12}$ satisfies $12 \leq 12 \leq 24$ (take $a = 12, b = 0$). Note $N = 1$ is also `Yes`, by using no cheats at all.
