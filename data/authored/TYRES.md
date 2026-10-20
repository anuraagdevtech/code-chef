---
topic: Number Theory
subtopic: Remainder modulo 4
time: $O(1)$ per test case
space: $O(1)$
---
Chef builds as many cars as possible first, each taking $4$ tyres, so $\lfloor N/4 \rfloor$ cars are made and $N \bmod 4$ tyres remain. Bikes take $2$ tyres each, so the friend can buy one exactly when the leftover is at least $2$.

Because $N$ is guaranteed **even**, the remainder $N \bmod 4$ is either $0$ or $2$ — never $1$ or $3$. So the whole question collapses to

$$N \equiv 2 \pmod 4$$

In words: an even number that is *not* a multiple of four leaves exactly two tyres over, which is precisely one bike. A multiple of four is consumed entirely by cars and leaves nothing.

The evenness guarantee is what makes this clean, and it is worth seeing why. Without it, $N = 7$ would leave $3$ tyres, still enough for one bike, and the test would have to be $N \bmod 4 \geq 2$. That more general form is also correct here, just redundant.

The samples cover both residues: $N = 8$ is $0 \bmod 4$ and yields no bike, while $N = 2$ and $N = 6$ are both $2 \bmod 4$ and yield one. Note $N = 2$ produces zero cars and a single bike — building cars first does not mean a car is always built.
