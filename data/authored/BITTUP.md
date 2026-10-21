---
topic: Combinatorics
subtopic: Independent bits, each a complement count
time: $O(\log N + \log M)$ per test case
space: $O(1)$
---
The AND is computed bit by bit and each $A_i$ ranges over all of $[0, 2^M - 1]$, so the $M$ bit positions are **completely independent** — choosing the tuple is the same as choosing, for each bit, the column of $N$ bits.

For one bit, the AND is $0$ unless every one of the $N$ entries has it set. So of the $2^N$ possible columns, exactly one is forbidden, leaving $2^N - 1$. Multiplying over the $M$ positions:

$$\text{answer} = (2^N - 1)^M \bmod (10^9 + 7)$$

The complementary counting is what keeps this simple: counting the valid columns directly would mean summing over how many entries have the bit set, whereas "all but one" is immediate.

Two modular-exponentiation calls answer each query — one for $2^N$ and one for the outer power — so $T = 10^5$ with $N, M$ up to $10^6$ costs nothing. Note $2^N - 1$ must be reduced modulo $p$ *before* the outer exponentiation, and since $p$ is prime and $2^N \not\equiv 1$ in general, no special case arises. (Were $2^N \equiv 1 \pmod p$ the base would be $0$ and the answer $0$, which the formula still handles.)

The samples confirm the shape: $N = 1, M = 2$ gives $1^2 = 1$ — the only tuple is $(0)$, since a single element must itself be $0$. $N = 2, M = 2$ gives $3^2 = 9$, and $N = 4, M = 2$ gives $15^2 = 225$. The last one, $255^4 = 4{,}228{,}250{,}625$, reduces to $228{,}250{,}597$ and shows the modulus actually biting.

## Edge cases

- **The $M$ bit positions are independent**, since the AND is computed bitwise — so the count is a per-bit count raised to the $M$-th power.
- **Per bit, every column of $N$ values works except the all-ones one**, giving $2^N - 1$ choices: the AND bit is $0$ unless all $N$ have it set.
- **The answer is therefore $(2^N - 1)^M$**, a doubly-nested modular power and nothing more.
- **$N = 1$** forces $A_1 = 0$, and $(2^1 - 1)^M = 1$ confirms it — the single tuple of all zeros.
- **$2^N - 1$ must be reduced before the outer power**, which `pow(pow(2, n, MOD) - 1, m, MOD)` does; computing $2^N$ exactly at $N = 10^6$ would be a $300{,}000$-digit number.
- **The subtraction cannot go negative** in practice, since $2^N \bmod p$ is $0$ only when $p \mid 2^N$, impossible for the prime $10^9+7$.
- **$N, M$ up to $10^6$** with $T$ up to $10^5$: two modular exponentiations per case, each $O(\log)$.

## Dry run

| $N$ | $M$ | $2^N - 1$ | $(2^N-1)^M$ | output |
|---:|---:|---:|---|---:|
| 1 | 2 | 1 | $1^2$ | `1` |
| 2 | 2 | 3 | $3^2$ | `9` |
| 4 | 2 | 15 | $15^2$ | `225` |
| 8 | 4 | 255 | $255^4 = 4228250625$ | `228250597` |

The last row reduces modulo $10^9+7$: $4228250625 - 4(10^9+7) = 228250597$.
