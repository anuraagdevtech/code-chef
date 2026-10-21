---
topic: Number Theory
subtopic: Counting residues in a range
time: $O(1)$ per test case
space: $O(1)$
---
Day $1$ is a Monday, so Saturdays fall on days $6, 13, 20, 27, \ldots$ — that is, the days $d$ with

$$d \equiv 6 \pmod 7$$

Counting them in $[1, N]$ gives $\lfloor (N-6)/7 \rfloor + 1$ when $N \geq 6$, and $0$ otherwise. Both branches collapse into the single expression

$$\left\lfloor \frac{N + 1}{7} \right\rfloor$$

which returns $0$ for $N < 6$ with no guard needed.

This is the same counting pattern as the Dracula problem, with the general form: the number of integers in $[1, N]$ congruent to $r$ modulo $m$ is $\lfloor (N + m - r)/m \rfloor$. Here $m = 7$ and $r = 6$, giving the $+1$.

The samples pin the boundary down precisely. $N = 5$ gives $0$ — the month ends the day before the first Saturday. $N = 6$ gives $1$, catching that Saturday exactly. $N = 8$ still gives $1$, since the second Saturday is day $13$. And $N = 22$ gives $3$, counting days $6, 13, 20$ but not $27$.

With $N$ up to $10^9$ a loop over the days is out of the question, so the closed form is not merely tidier — it is the only workable approach.

## Edge cases

- **$N = 5$ then $N = 6$**: $0$ then $1$. The sample has both, and together they pin the offset — day $6$ is the first Saturday.
- **$N = 7$** (Sunday): still $1$, since no new Saturday has arrived.
- **Largest input** ($N = 10^9$): about $1.43 \times 10^8$.
- **The convention that day $1$ is a Monday fixes the $+1$.** Saturdays are the days congruent to $6 \bmod 7$, so the count is $\lfloor (N+1)/7 \rfloor$; starting the week anywhere else shifts every answer by a day.

## Dry run

| $N$ | $N + 1$ | $//\,7$ | Saturdays (days $6, 13, 20, \ldots$) | output |
|---:|---:|---:|---|---|
| 5 | 6 | 0 | none yet | `0` |
| 6 | 7 | 1 | $6$ | `1` |
| 8 | 9 | 1 | $6$ | `1` |
| 22 | 23 | 3 | $6, 13, 20$ | `3` |
