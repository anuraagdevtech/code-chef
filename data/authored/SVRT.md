---
topic: Basic Math
subtopic: Balance the circular gaps by quotient and remainder
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The $K$ consecutive circular gaps are positive integers summing to $N$. Their maximum is at least $D=\lceil N/K\rceil$, and distributing the gaps as evenly as possible attains it.

To minimise how many gaps equal $D$, let all other gaps be at most $D-1$. If there are $x$ maximum gaps, then $N\le K(D-1)+x$, so $x\ge N-K(D-1)$. Choosing exactly that many gaps of size $D$ and all other gaps of size $D-1$ attains the bound. This is the adjacent-gap distance used by the problem's samples.

## Edge cases

- If $N$ is divisible by $K$, every gap equals $N/K$, so the count is $K$.
- If $N=K$, every gap has length one.
- Use integer ceiling division.

## Dry run

For `N=10,K=6`, `D=2`, and `X=10-6*(2-1)=4`: four gaps of two and two gaps of one.
