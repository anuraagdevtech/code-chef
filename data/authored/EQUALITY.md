---
topic: Basic Math
subtopic: Solving a symmetric linear system by summing
time: $O(N)$ per test case
space: $O(N)$
---
Each equation omits exactly one variable, so writing $S = x_1 + \cdots + x_N$ the $i$-th equation is simply

$$S - x_i = a_i \quad\Longrightarrow\quad x_i = S - a_i$$

The only unknown left is $S$. Summing all $N$ equations counts every variable exactly $N-1$ times:

$$\sum_i a_i = \sum_i (S - x_i) = NS - S = (N-1)S
\quad\Longrightarrow\quad
S = \frac{\sum_i a_i}{N-1}$$

So one pass to total the $a_i$, one division, then $x_i = S - a_i$ for each. No Gaussian elimination, which on an $N \times N$ system would be $O(N^3)$ and hopeless at $N = 50{,}000$.

Exploiting the **symmetry** — every equation has the same shape — is what collapses the system. The statement's remark that a unique solution always exists for $N > 1$ is explained by the same algebra: the division by $N - 1$ is well defined precisely when $N \geq 2$.

Checking the first sample: $a = [9,6,5]$ sums to $20$, so $S = 20/2 = 10$ and $x = [1, 4, 5]$. Indeed $4+5 = 9$, $1+5 = 6$, $1+4 = 5$.

Two practical notes. The $a_i$ reach $5 \times 10^{12}$ and there may be $50{,}000$ of them, so the total needs **64-bit** arithmetic outside Python. And the division is guaranteed exact, so integer division is right — using floating point would lose precision at this magnitude.

## Edge cases

- **Summing all $N$ equations counts each variable exactly $N - 1$ times**, which recovers $\sum x$ in a single step — no elimination or substitution is needed.
- **The division must be exact**, and the problem guarantees a solvable system, so $\sum a$ is divisible by $N - 1$. Integer division is the right tool.
- **Float division would be wrong, not merely slow.** With $a_i$ up to $5 \cdot 10^{12}$ and $N$ up to $5 \cdot 10^4$, the sum reaches $2.5 \cdot 10^{17}$ — beyond the $2^{53}$ exact range of a double, so `/` can round and produce an off-by-one answer.
- **$N = 2$**: the divisor is $1$, so $\sum x = a_1 + a_2$ and the answer is simply the two values swapped.
- **$x_i \geq 1$ is guaranteed** by the constraints, so valid input never yields a non-positive output.
- **$T$ up to $25{,}000$ with $\sum N \leq 50{,}000$** means most cases are tiny, so the per-case overhead matters as much as the per-element work.

## Dry run

Second sample: $a = 13, 11, 10, 8$, so $N = 4$.

| step | value |
|---|---|
| $\sum a$ | $42$ |
| $\sum x = \sum a / (N-1)$ | $42 / 3 = 14$ |
| $x_i = 14 - a_i$ | $1, 3, 4, 6$ |

Check: $x_2 + x_3 + x_4 = 3 + 4 + 6 = 13 = a_1$. ✓
