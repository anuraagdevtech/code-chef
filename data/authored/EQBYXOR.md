---
topic: Bit Manipulation
subtopic: The XOR span of an initial segment
time: $O(1)$ per test case
space: $O(1)$
---
Let $D = A \oplus B$. Applying several operations XORs $A$ by the combined XOR of the chosen values, so the question is: in how few picks from $\{1, \ldots, N-1\}$ can we XOR to exactly $D$?

- $D = 0$ → **0** operations, $A$ already equals $B$.
- $1 \leq D < N$ → **1**, since $D$ itself is a legal choice.
- Otherwise, two may suffice — and the bound comes from the **XOR span** of the allowed set.

The set $\{1, \ldots, N-1\}$ contains every power of two up to $2^{b-1}$, where $b$ is the bit length of $N-1$. Those powers span all values below $2^b$, and nothing larger is reachable, since every element has at most $b$ bits. So $D$ is reachable at all exactly when

$$D < 2^{\,b}, \qquad b = \text{bit\_length}(N-1)$$

and otherwise the answer is $-1$.

When $D$ is reachable but $D \geq N$, two operations always work. Take $X_1 = 2^{b-1}$, which is at most $N-1$, and $X_2 = D \oplus 2^{b-1} = D - 2^{b-1}$, which is below $2^{b-1}$ and hence also legal — and non-zero because $D \geq N > 2^{b-1}$.

$N = 1$ is the degenerate case: the range $1 \leq X < 1$ is empty, so no operation exists and the answer is $-1$ unless $A$ already equals $B$. Sample case 3 is exactly this, with $N = 1$ and $D = 3$.

Sample case 2 has $D = 3 \oplus 7 = 4 < 8$, so one operation does it.

## Edge cases

- **Already equal** → $0$ operations (the first row).
- **$N = 1$ permits no operation at all**, since $X$ must satisfy $1 \leq X < 1$. So anything but $A = B$ is impossible — the third row, where $A \oplus B = 3$ and the answer is $-1$.
- **One operation works exactly when $1 \leq A \oplus B < N$**, because that difference is itself a legal $X$.
- **Two operations extend the reach to the whole bit width of $N-1$.** Picking $X_1 = 2^{b-1}$ (the top bit of $N-1$, itself a legal value) and $X_2 = d \oplus 2^{b-1}$ covers every $d < 2^b$, which is why the second threshold is $2^{\text{bit\_length}(N-1)}$ rather than $N$ again.
- **Beyond that width nothing is reachable**, however many operations are used: every legal $X$ is below $2^b$, so every XOR of them is too.
- **The answer is never more than $2$** when it is finite.
- **$A, B < 2^{30}$**, so the bit-length arithmetic stays in a comfortable range.

## Dry run

| $A$ | $B$ | $d = A \oplus B$ | $N$ | $d < N$? | $d < 2^{\text{bits}(N-1)}$? | output |
|---:|---:|---:|---:|:---:|:---:|---:|
| 5 | 5 | 0 | 2 | — | — | `0` |
| 3 | 7 | 4 | 8 | yes | — | `1` |
| 8 | 11 | 3 | 1 | no | $3 < 1$ no | `-1` |
| 24 | 27 | 3 | 3 | no | $3 < 4$ yes | `2` |

The last row uses $X_1 = 2$ and $X_2 = 1$, both legal since $N = 3$, and $2 \oplus 1 = 3$.
