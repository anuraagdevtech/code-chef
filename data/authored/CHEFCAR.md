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

## Edge cases

- **Each litre is priced by where it is bought**, and the litre burned on leg $i$ must be bought at a checkpoint between $\max(1, i - V + 1)$ and $i$ — the tank only holds $V$ litres, so it cannot be bought too early.
- **The minimum therefore prices each litre at $\max(1, i - V + 1)$**, which gives $V$ litres at price $1$ and then prices $2, 3, \dots, N-V$ for the rest.
- **A large tank makes everything cost $1$.** When $N - 1 \leq V$ the whole trip can be fuelled at checkpoint $1$, so the minimum is just the number of legs (the third sample).
- **The maximum buys each litre as late as possible**, one at every checkpoint $1 \dots N-1$, costing $1 + 2 + \dots + (N-1) = N(N-1)/2$ — independent of $V$, since one litre always fits.
- **Per-litre accounting is what makes this clean**; reasoning stop by stop invites the wrong greedy, as "fill up only when empty" overpays.
- **No water may be left at the end and none poured out**, which is why exactly $N-1$ litres are bought in total.
- **$N, V$ up to $10^9$** put the maximum near $5 \times 10^{17}$ — past 32-bit, so the closed forms must stay in exact integers.

## Dry run

Second sample: $N = 4$ checkpoints (three legs), tank $V = 2$.

| leg | earliest checkpoint it can be bought at | cheapest price | dearest price |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 2 | 3 |

Minimum $1 + 1 + 2 = 4$, maximum $1 + 2 + 3 = 6$. Output `6 4`.
