---
topic: Number Theory
subtopic: Divisibility test
time: $O(1)$ per test case
space: $O(1)$
---
A nibble is $4$ bits, and a program is *Good* when its size is exactly $X$ nibbles for a positive integer $X$. A program of $N$ bits occupies $N/4$ nibbles, so $N$ must divide evenly by $4$:

$$N \equiv 0 \pmod 4$$

which is the single expression `n % 4 == 0`.

The clause "where $X$ is a **positive** integer" formally rules out $X = 0$, so $N = 0$ would be *Not Good*. The constraints guarantee $N \geq 1$, so this never arises and no extra guard is needed — but it is worth noticing the requirement rather than assuming divisibility alone is the whole condition, because the same wording in a problem allowing $N = 0$ would change the answer.

Since $4$ is a power of two there is a bitwise equivalent, `n & 3 == 0`, which tests that the low two bits are clear. It is the same test and no faster in Python, but it is the idiom to recognise when reading C-style code: `n % 2^k == 0` is `n & (2^k - 1) == 0`.

Checking the samples: $8 = 2 \times 4$ and $52 = 13 \times 4$ are Good, while $17$ and $3$ leave remainders of $1$ and $3$.
