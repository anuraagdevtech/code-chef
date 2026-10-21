---
topic: Number Theory
subtopic: Divisibility with an upper bound
time: $O(1)$ per test case
space: $O(1)$
---
Every problem contributes either $X$ marks or $0$, so if Chef solved $k$ of them his score is exactly $kX$. The reachable scores are therefore the multiples of $X$ from $0$ up to $NX$, and $Y$ is achievable when **both** of these hold:

1. $Y$ is a multiple of $X$, that is $Y \bmod X = 0$;
2. the implied count $k = Y / X$ does not exceed the number of problems, that is $Y / X \leq N$.

Checking only divisibility is the natural half-answer and it is wrong, because a score can be a valid multiple yet demand more problems than exist. Equally, checking only $Y \leq NX$ is wrong, because a score below the maximum may still not be a multiple. Both conditions are needed.

Sample case 1 fails the first test ($Y = 4$ is not a multiple of $X = 8$) and sample case 5 fails it too ($36$ is not a multiple of $5$). Case 4 is the tight upper end: $100 / 10 = 10$ problems, exactly the $N$ available, so it is achievable.

The case $Y = 0$ deserves a glance. It satisfies $0 \bmod X = 0$ with $k = 0 \leq N$, so it is always achievable — Chef simply solves nothing. Case 3 confirms it. Since $X \geq 1$ the modulo never divides by zero.

## Edge cases

- **$Y = 0$**: zero is divisible by any $X$ and needs no correct answers, so `YES`. The sample's third case is this, and a solution requiring at least one correct answer fails it.
- **$Y = N \cdot X$ exactly** (all questions right): the sample's fourth case, $10 \times 10 = 100$, sits on the boundary and must be `YES`.
- **Divisible but out of reach**: $N = 3$, $X = 5$, $Y = 20$ needs four correct answers out of three questions. **Both conditions are needed** — divisibility alone would wrongly accept it.
- **Not divisible** ($Y = 4$, $X = 8$): no number of correct answers lands on $4$, so `NO`.

## Dry run

| $N$ | $X$ | $Y$ | $Y \bmod X$ | $Y / X$ | $\leq N$? | output |
|---:|---:|---:|---:|---:|:---:|---|
| 1 | 8 | 4 | 4 | — | — | `NO` |
| 3 | 6 | 12 | 0 | 2 | yes | `YES` |
| 4 | 5 | 0 | 0 | 0 | yes | `YES` |
| 10 | 10 | 100 | 0 | 10 | yes (equal) | `YES` |
| 8 | 5 | 36 | 1 | — | — | `NO` |

Rows 1 and 5 fail on divisibility; row 4 is the exact upper limit.
