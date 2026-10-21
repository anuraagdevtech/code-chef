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

## Edge cases

- **$N = 4$**: the smallest good size, exactly one nibble.
- **$N = 1, 2, 3$**: smaller than a single nibble, so `Not Good` — the answer is about divisibility, not about being large enough.
- **Largest input** ($N = 1000$, which is $4 \times 250$): `Good`.
- **A nibble is $4$ bits, not $8$.** Testing divisibility by $8$ would wrongly reject $4$, $12$, $20$ and so on; the sample's $52 = 4 \times 13$ is good but not a multiple of $8$.

## Dry run

| $N$ | $N \bmod 4$ | output |
|---:|---:|---|
| 8 | 0 | `Good` |
| 17 | 1 | `Not Good` |
| 52 | 0 | `Good` |
| 3 | 3 | `Not Good` |

$52$ is the row that separates "multiple of $4$" from "multiple of $8$".
