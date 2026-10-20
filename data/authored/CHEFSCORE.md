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
