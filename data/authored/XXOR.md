---
topic: Prefix Sums
subtopic: Per-bit prefix counts, decided bit by bit
time: $O(31(N + Q))$
space: $O(31N)$
---
The sum $\sum_{i=L}^{R} (A_i \oplus X)$ splits across bit positions, and bit $b$ of $X$ affects only the $2^b$ column. So the 31 bits of $X$ are **independent** and each can be decided on its own.

Let $m = R - L + 1$ and let $c_b$ be how many of $A_L \ldots A_R$ have bit $b$ set. XORing with a $1$ at that bit flips every one of them, so the column contributes

$$\begin{cases} c_b \cdot 2^b & \text{if } X_b = 0 \\ (m - c_b) \cdot 2^b & \text{if } X_b = 1 \end{cases}$$

Take whichever is larger, which gives $X_b = 1$ exactly when $2c_b < m$. The tie $2c_b = m$ is where the **"smallest $X$"** requirement bites: both choices give the same sum, so take $X_b = 0$. The strict inequality handles this automatically.

The counts come from 31 prefix-sum arrays, one per bit, so each query is 31 constant-time lookups instead of a scan — essential with $N, Q = 10^5$.

Note the answers are huge because every bit above the data is a free win: with $A_i < 2^{31}$ but the actual values much smaller, all high bits have $c_b = 0 < m - c_b$, so $X$ sets them all. That is why the sample outputs sit just under $2^{31}$. For query `1 3` on $[20, 11, 18]$ the counted bits give $X_0 = X_2 = X_3 = 1$ and $X_1 = X_4 = 0$, i.e. $13$ in the low five bits, and bits $5 \ldots 30$ are all set, giving $2147483616 + 13 = 2147483629$.

The two later queries coincide at $2147483645$ even though the subarrays differ — the per-bit majorities happen to agree.

## Edge cases

- **The bits are independent**, since each contributes $2^b$ times the count of elements whose bit differs from $X$'s — so each bit of $X$ is chosen on its own from the count of ones in the range.
- **Flip a bit only when it strictly helps**: setting $X$'s bit turns the zeros into ones, which is better when fewer than half the elements already have it. The comparison is $2 \cdot \text{ones} < m$.
- **A tie must leave the bit clear**, because the problem asks for the *smallest* such $X$ — a bit that changes nothing must not be set.
- **The high bits dominate but need no special ordering**, since the choices are independent; the per-bit rule is already optimal.
- **$31$ bit planes are prefixed**, which is what makes each query $O(31)$ rather than $O(31 \cdot \text{range})$.
- **Bits above the data are always set**, since no element has them — which is why the answers are close to $2^{31}$.
- **$X < 2^{31}$ is the stated bound**, matching the $31$ planes exactly.

## Dry run

First query of the sample: the range $1 \dots 3$ holds $20, 11, 18$, so $m = 3$.

| bit | ones in range | $2 \cdot \text{ones} < 3$? | $X$'s bit |
|---:|---:|:---:|---:|
| 0 | 1 | yes | 1 |
| 1 | 2 | no | 0 |
| 2 | 1 | yes | 1 |
| 3 | 1 | yes | 1 |
| 4 | 2 | no | 0 |
| 5–30 | 0 | yes | 1 |

$X = 2147483629$, matching the expected output.
