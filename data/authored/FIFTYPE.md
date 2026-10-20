---
topic: Brute Force
subtopic: Searching one variable of a linear Diophantine equation
time: $O(1)$ per test case — the search is bounded by a small constant
space: $O(1)$
---
Charging adds $2$ and discharging subtracts $3$, so with $a$ charging minutes and $b$ discharging minutes the battery changes by $2a - 3b$. Reaching exactly $50\%$ from $N$ requires

$$2a - 3b = 50 - N$$

with $a, b \geq 0$, minimising $a + b$. This is a linear Diophantine equation in two unknowns.

Fixing $b$ determines $a$, so the search runs over $b$ alone: for each candidate, $a = \frac{(50 - N) + 3b}{2}$ is valid when the numerator is non-negative and even. Since $N \leq 100$, the gap never exceeds $50$ and a small bound on $b$ suffices — the loop below runs to $200$, far past any optimum, and still costs nothing.

Working out the structure by hand is instructive. Let $d = 50 - N$.

- $d$ **even and positive**: pure charging, $d/2$ minutes. Sample case 4 ($N = 0$) gives $25$.
- $d$ **odd**: parity blocks pure charging, since $2a$ is always even. One discharge flips the parity, costing $1 + \frac{d+3}{2}$ minutes in total. Sample case 3 ($N = 23$, $d = 27$) gives $1 + 15 = 16$.
- $d$ **negative**: the battery must come down, which only discharging does, but $-3$ steps may overshoot and need charging to correct. Sample case 1 ($N = 51$, $d = -1$) needs one of each: $51 \to 48 \to 50$, two minutes.

That last case is the one that defeats a naive "just divide the gap" solution. Searching over $b$ handles all three shapes uniformly without case analysis, which is why it is preferred here over deriving each branch.

The requirement that the level stay within $[0, 100]$ never forces extra moves at these bounds, since the charging and discharging minutes can be interleaved to keep the battery inside the range.
