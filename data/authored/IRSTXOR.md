---
topic: Bit Manipulation
subtopic: Maximising a product under a fixed XOR
time: $O(1)$ per test case
space: $O(1)$
---
Let $d$ be the bit width, so $2^{d-1} \leq C < 2^d$, and let $M = 2^d - 1$ be the all-ones mask.

$A \oplus B = C$ says $A$ and $B$ **differ** exactly on the bits where $C$ is $1$, and **agree** everywhere else. That splits the construction into two independent decisions.

**On $C$'s zero bits**, $A$ and $B$ agree, so setting them all to $1$ raises both numbers and can only increase the product. Those bits are $M \oplus C$, and both $A$ and $B$ receive them.

**On $C$'s one bits**, each bit goes to exactly one of the two. The sum $A + B$ is now fixed at $C + 2(M \oplus C)$ regardless of how they are split, and for a fixed sum the product is largest when the two values are as **close as possible**. The top bit of $C$ is bit $d-1$ and dwarfs all the others combined, so give that single bit to one number and every remaining bit of $C$ to the other — that is the most balanced split achievable.

So, with $h = 2^{d-1}$:

$$A = (M \oplus C) \mid h, \qquad B = (M \oplus C) \mid (C \oplus h)$$

Checking $C = 13 = 1101_2$: here $d = 4$, $M = 1111_2$, and $M \oplus C = 0010_2$. The top bit is $8$, so $A = 0010 \mid 1000 = 10$ and $B = 0010 \mid 0101 = 7$, giving $70$.

For $C = 10 = 1010_2$: $M \oplus C = 0101_2$, $A = 0101 \mid 1000 = 13$, $B = 0101 \mid 0010 = 7$, giving $91$ — larger than for $C = 13$, since the shared ones contribute more.

In Python $d$ is `C.bit_length()`, so the whole thing is a handful of bitwise operations.

## Edge cases

- **The bound $A, B < 2^d$ is what makes the maximum finite.** Without it, both numbers could carry arbitrarily high matching bits — the XOR would be unaffected and the product unbounded.
- **Bits where $C$ is $0$ should be set in both.** $A$ and $B$ must agree there, and setting both to $1$ raises each factor at no cost to the XOR.
- **Bits where $C$ is $1$ must differ**, so they are split — and the product is maximised by balancing the two factors, which means giving $A$ the single top bit of $C$ and $B$ all of $C$'s lower set bits. Since $2^{d-1}$ exceeds the sum of everything below it, any other split is worse.
- **$d = C.\text{bit\_length}()$** is exactly the smallest $d$ with $2^d > C$, for $C \geq 1$.
- **$C$ a power of two** leaves only one differing bit, so one factor gets it and the other gets all the zero-bits below.
- **$C \leq 10^9$** keeps the factors under $2^{30}$ and the product under $2^{60}$ — past 32-bit, inside 64-bit, exact in Python.

## Dry run

Sample: $C = 13 = 1101_2$, so $d = 4$ and both factors are below $16$.

| bit | $2^b$ | $C$ | requirement | $A$ | $B$ |
|---:|---:|---:|---|---:|---:|
| 3 | 8 | 1 | differ — give to $A$ (top bit) | 1 | 0 |
| 2 | 4 | 1 | differ — give to $B$ | 0 | 1 |
| 1 | 2 | 0 | agree — set both | 1 | 1 |
| 0 | 1 | 1 | differ — give to $B$ | 0 | 1 |

$A = 1010_2 = 10$, $B = 0111_2 = 7$, and $10 \oplus 7 = 13$ with product `70`.
