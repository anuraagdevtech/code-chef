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
