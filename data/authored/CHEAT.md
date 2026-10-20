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
