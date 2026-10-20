---
topic: Combinatorics
subtopic: Extremal construction in a round robin
time: $O(1)$ per test case
space: $O(1)$
---
To maximise the gap, push the winner as high as possible and the runner-up as low as possible.

**The winner** can take every one of its $N - 1$ games, for $3(N-1)$ points. Nothing constrains this.

**The runner-up** is the best of the remaining $N - 1$ teams, and here is the constraint that makes the problem interesting: those teams still play each other, and every game produces a winner. Among themselves they contest $\binom{N-1}{2}$ games, so they share $N-1 \choose 2$ wins between $N - 1$ teams. By the pigeonhole principle the best of them has at least

$$\left\lceil \frac{\binom{N-1}{2}}{N-1} \right\rceil = \left\lceil \frac{N-2}{2} \right\rceil$$

wins, and that bound is achievable by spreading the results as evenly as possible. So the runner-up can be held to $3\left\lceil \frac{N-2}{2} \right\rceil$ points and no lower.

The difference simplifies neatly:

$$3(N-1) - 3\left\lceil \frac{N-2}{2} \right\rceil = 3 \left\lfloor \frac{N}{2} \right\rfloor$$

so the whole answer is `3 * (n // 2)`.

The pigeonhole step is the part worth dwelling on. The instinct is to say the runner-up could lose everything and score $0$ — but that is impossible once $N \geq 3$, because the non-winning teams must distribute wins among themselves. Sample case 3 shows it: with $N = 4$ the answer is $6$, not $9$, because the other three teams play three games and someone must win at least one.

Sample case 1 is the exception where the instinct holds: with $N = 2$ the loser really does score $0$, and $3 \lfloor 2/2 \rfloor = 3$.

With $N$ up to $10^9$ and $T$ up to $10^5$, only a closed form is viable.
