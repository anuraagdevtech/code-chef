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

## Edge cases

- **$N = 2$ and $N = 3$ give the same answer** ($3$), because $\lfloor N/2 \rfloor$ is $1$ for both — the floor means an odd team count adds nothing over the even number below it. The sample has both, which is what pins the floor down rather than a ceiling.
- **$N = 4$**: $6$.
- **Every answer is a multiple of $3$**, since a win is worth three points — a result not divisible by $3$ would signal an arithmetic slip.
- **Largest input** ($N = 10^9$): about $1.5 \times 10^9$, which overflows a 32-bit integer in C++ and needs `long long`.

## Dry run

| $N$ | $\lfloor N/2 \rfloor$ | $3 \lfloor N/2 \rfloor$ | output |
|---:|---:|---:|---|
| 2 | 1 | 3 | `3` |
| 3 | 1 | 3 | `3` |
| 4 | 2 | 6 | `6` |
| 9 | 4 | 12 | `12` |

Rows 1 and 2 share an answer, and so would rows 3 and the unlisted $N = 5$.
