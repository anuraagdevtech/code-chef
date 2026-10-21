---
topic: Bit Manipulation
subtopic: Lift the shared bits, then balance the differing ones
time: $O(N)$ per test case
space: $O(1)$
---
Look at the two factors $A \oplus X$ and $B \oplus X$ bit by bit.

**Where $A$ and $B$ agree**, both factors get the same bit, and we can choose $X$ to make it $1$. So every agreeing bit contributes to *both* factors — pure gain, taken by setting $X_b = 1 - A_b$. Call the resulting common part

$$P = \bigl(2^N - 1\bigr) \oplus (A \oplus B)$$

**Where $A$ and $B$ differ**, exactly one factor gets the bit whatever $X$ does; $X_b$ only chooses *which* one. So with $Q = A \oplus B$ the product is

$$(P + u)(P + v), \qquad u + v = Q$$

where $u$ is the subset of $Q$'s bits handed to the first factor. The sum is fixed, so the product is maximised by making $u$ and $v$ as **close as possible** — and for a set of distinct powers of two the closest split is immediate: give the highest bit to one side and *all* the rest to the other, since $2^h$ exceeds the sum of every lower bit.

So: complement $A$ on the agreeing bits, send $Q$'s top bit to one factor, and send $Q$'s remaining bits to the other. When $A = B$ there are no differing bits and both factors become $2^N - 1$.

Any optimal $X$ is accepted. For $N = 3, A = 4, B = 6$ the differing bit is bit $1$, and our $X = 3$ gives $7 \cdot 5 = 35$ — matching the sample. For $N = 2, A = 2, B = 1$ every bit differs, so $Q = 3$ splits as $2$ against $1$ and $X = 0$ gives $2 \cdot 1 = 2$, which beats the $0$ that any unbalanced split would yield.
