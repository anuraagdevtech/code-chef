---
topic: Greedy
subtopic: Pricing each litre by its earliest legal purchase
time: $O(1)$ per test case
space: $O(1)$
---
Think per **litre** rather than per stop. The journey is $N-1$ km, so exactly $N-1$ litres are bought, and the litre that powers the leg from checkpoint $i$ to $i+1$ costs whatever the checkpoint it was bought at is numbered.

**Maximum.** Buy each litre as late as possible: one litre at checkpoint $i$, burned immediately. The tank never holds more than $1 \leq V$ litres, so this is always legal:

$$\text{max} = 1 + 2 + \cdots + (N-1) = \frac{N(N-1)}{2}$$

Note $V$ does not appear — a bigger tank cannot make the trip *more* expensive.

**Minimum.** Buy each litre as early as possible. A litre bought at checkpoint $j$ and burned on leg $i$ sits in the tank across legs $j, \ldots, i$, which is $i - j + 1$ litres on board when leaving $j$, so capacity forces $i - j + 1 \leq V$. The earliest legal purchase is therefore $j = \max(1,\, i - V + 1)$ and

$$\text{min} = \sum_{i=1}^{N-1} \max(1,\, i - V + 1)$$

The first $\min(N-1, V)$ legs cost $1$ each and the rest cost $2, 3, \ldots$, giving the closed form $V + \frac{(N-V)(N-V+1)}{2} - 1$ when $N - 1 > V$, and simply $N-1$ otherwise.

Per-litre accounting is what makes this clean; reasoning stop by stop invites the wrong greedy. With $N = 4, V = 2$, "fill up whenever empty" buys $2$ litres at checkpoint $1$ and $1$ at checkpoint $3$ for $5$, but the optimum buys $2$ at checkpoint $1$ and $1$ at checkpoint $2$ for $4$ — topping up early beats waiting until empty.

The samples confirm both ends: $N = 4$ gives a maximum of $6$ for either tank size, while the minimum drops from $4$ at $V = 2$ to $3$ at $V = 3$, where one tank covers the whole road.
