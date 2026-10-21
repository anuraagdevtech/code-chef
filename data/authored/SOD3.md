---
topic: Number Theory
subtopic: Digit sum congruent to the value mod 3
time: $O(1)$ per test case
space: $O(1)$
---
The problem looks like it needs digit-DP over an $18$-digit range, but a classical congruence collapses it.

Since $10 \equiv 1 \pmod 3$, every power of ten is also $\equiv 1$, so

$$n = \sum_k d_k 10^k \equiv \sum_k d_k \pmod 3$$

That is the familiar divisibility rule: **a number and its digit sum leave the same remainder mod 3**. So "digit sum divisible by $3$" is simply "$n$ divisible by $3$", and the count over $[L, R]$ is a difference of two floors:

$$\left\lfloor \frac{R}{3} \right\rfloor - \left\lfloor \frac{L-1}{3} \right\rfloor$$

Subtracting the prefix below $L$ is what makes the range inclusive at both ends.

With $R$ up to $10^{18}$ and $T$ up to $10^4$, this is the only viable approach — iterating the range is out of the question, and even a digit DP would be needless work.

Checking the first sample: in $[139, 141]$ only $141 = 3 \times 47$ qualifies, and $\lfloor 141/3 \rfloor - \lfloor 138/3 \rfloor = 47 - 46 = 1$.

The same rule holds for $9$ (since $10 \equiv 1 \pmod 9$) but **not** for other moduli — the trick is specific to divisors of $10 - 1$. For a modulus like $7$ the digit sum tells you nothing, and digit DP would genuinely be required.

The values exceed 32 bits, so this needs 64-bit arithmetic outside Python.

## Edge cases

- **The digit sum never needs computing.** Since $10 \equiv 1 \pmod 3$, every power of ten is $\equiv 1$, so a number is congruent to its digit sum mod $3$ — the condition collapses to plain divisibility by $3$.
- **The lower bound must be included**, which is why the count is $\lfloor R/3 \rfloor - \lfloor (L-1)/3 \rfloor$. Writing $\lfloor L/3 \rfloor$ drops $L$ itself when it is a multiple of $3$, and the first row's range $139 \dots 141$ contains exactly one such number — $141$ — so that slip answers $0$.
- **$L = R$** → the answer is $0$ or $1$.
- **$L \geq 1$ is guaranteed**, so $L - 1$ stays non-negative and no special case is needed at the bottom of the range.
- **$R$ up to $10^{18}$** demands exact integer division; a float divide loses precision above $2^{53}$ and would miscount the last two sample rows.
- **This is a digit-DP problem reduced to one line** — the usual approach is entirely unnecessary once the congruence is noticed.

## Dry run

First sample: $L = 139$, $R = 141$.

| $n$ | digits | digit sum | $\div 3$? | $n \div 3$? |
|---:|---|---:|:---:|:---:|
| 139 | $1,3,9$ | 13 | no | no |
| 140 | $1,4,0$ | 5 | no | no |
| 141 | $1,4,1$ | 6 | **yes** | **yes** |

$\lfloor 141/3 \rfloor - \lfloor 138/3 \rfloor = 47 - 46 = $ `1`. The two columns agree on every row, as the congruence guarantees.
