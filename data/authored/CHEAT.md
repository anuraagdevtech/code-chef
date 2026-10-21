---
topic: Number Theory
subtopic: Counting residues in a range
time: $O(1)$ per test case
space: $O(1)$
---
Today is Monday and that counts as day $1$, so day $d$ is a Tuesday exactly when

$$d \equiv 2 \pmod 7$$

The question becomes: how many integers in $[1, N]$ leave remainder $2$ on division by $7$? Those are $2, 9, 16, 23, \ldots$, and counting them up to $N$ gives

$$\left\lfloor \frac{N - 2}{7} \right\rfloor + 1 \quad\text{for } N \geq 2,\qquad 0 \text{ otherwise}$$

which collapses neatly into the single expression

$$\left\lfloor \frac{N + 5}{7} \right\rfloor$$

with no special case. The shift by $5$ works because it slides the first Tuesday down to the multiple-of-seven boundary, and it returns $0$ for $N = 1$ automatically — sample case 1.

The general form is worth remembering: the count of integers in $[1, N]$ congruent to $r$ modulo $m$ is $\lfloor (N + m - r)/m \rfloor$. Here $m = 7$ and $r = 2$, giving the $+5$.

Samples 3 and 4 fix the boundary precisely. $N = 15$ still gives $2$, because day $16$ — the third Tuesday — has not arrived; $N = 16$ includes it and gives $3$. An off-by-one would shift both.

The phrase "including today" is what makes Monday day $1$ rather than day $0$; reading it the other way moves every Tuesday by one and breaks all four samples.

## Edge cases

- **$N = 1$**: today is Monday, so no Tuesday has arrived yet and the answer is $0$. The sample's first row.
- **$N = 2$**: the first Tuesday, giving $1$.
- **$N = 15$ against $N = 16$**: $2$ then $3$. The sample has both, and they straddle the third Tuesday on day $16$ — an off-by-one in the offset moves this step by a day.
- **Largest input** ($N = 1000$): $143$ Tuesdays.
- **The convention that day $1$ is Monday is what fixes the $+5$.** Tuesdays are the days congruent to $2 \bmod 7$, so the count is $\lfloor (N + 5)/7 \rfloor$; starting the week anywhere else shifts every answer.

## Dry run

| $N$ | $N + 5$ | $//\,7$ | Tuesdays (days $2, 9, 16, \ldots$) | output |
|---:|---:|---:|---|---|
| 1 | 6 | 0 | none yet | `0` |
| 10 | 15 | 2 | $2, 9$ | `2` |
| 15 | 20 | 2 | $2, 9$ | `2` |
| 16 | 21 | 3 | $2, 9, 16$ | `3` |

Rows 3 and 4 are consecutive days either side of the third Tuesday.
